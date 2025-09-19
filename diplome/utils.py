import os
import hashlib
from hedera import Client, PrivateKey, AccountId, TopicId, TopicMessageSubmitTransaction, TopicMessageQuery
from django.conf import settings

def publier_hash(pdf_file):
    # Lire le fichier PDF
    pdf_bytes = pdf_file.read()
    pdf_hash = hashlib.sha256(pdf_bytes).hexdigest()

    # Config Hedera depuis settings ou env
    client = Client.forTestnet()
    client.setOperator(
        AccountId.fromString(settings.HEDERA_ACCOUNT_ID),
        PrivateKey.fromString(settings.HEDERA_PRIVATE_KEY)
    )
    topic_id = TopicId.fromString(settings.HEDERA_TOPIC_ID)

    # Publier le hash sur Hedera
    tx = TopicMessageSubmitTransaction().setTopicId(topic_id).setMessage(pdf_hash)
    tx_response = tx.execute(client)
    receipt = tx_response.getReceipt(client)
    status = receipt.status
    tx_id = tx_response.transactionId.toString()

    return {"hash": pdf_hash, "status": str(status), "tx_id": tx_id}


import requests
import base64
from django.conf import settings

def verifier_hash_hedera(hash_value):
    topic_id = settings.HEDERA_TOPIC_ID
    url = f"https://testnet.mirrornode.hedera.com/api/v1/topics/{topic_id}/messages?limit=100"
    
    response = requests.get(url)
    if response.status_code != 200:
        return {"valid": False, "all_hashes": [], "error": "Impossible de contacter le Mirror Node"}

    messages = response.json().get("messages", [])
    all_hashes = []

    for msg in messages:
        try:
            decoded = base64.b64decode(msg["message"]).decode()
            all_hashes.append(decoded)
        except Exception:
            continue  # ignorer les messages non valides

    print("Liste de tous les hashes décodés :", all_hashes)  # <-- ici
    valid = hash_value in all_hashes
    return {"valid": valid, "all_hashes": all_hashes}
