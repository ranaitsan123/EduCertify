from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import publier_hash

@api_view(['POST'])
def upload_diplome_api(request):
    pdf_file = request.FILES.get('file')
    if not pdf_file:
        return Response({"error": "Aucun fichier fourni"}, status=400)
    try:
        result = publier_hash(pdf_file)
        return Response(result)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


from django.http import JsonResponse
from .utils import verifier_hash_hedera

@api_view(['GET'])
def verifier_diplome_api(request):
    hash_value = request.GET.get("hash")
    if not hash_value:
        return JsonResponse({"error": "Hash manquant"}, status=400)

    try:
        is_valid = verifier_hash_hedera(hash_value)
        return JsonResponse({"valid": is_valid})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
