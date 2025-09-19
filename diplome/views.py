from django.shortcuts import render

def upload_page(request):
    return render(request, 'upload.html')

def verifier_page(request):
    return render(request, 'verifier.html')
