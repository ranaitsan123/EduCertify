from django.urls import path
from .views import upload_page, verifier_page
from .api import upload_diplome_api, verifier_diplome_api

urlpatterns = [
    path('upload/', upload_page, name='upload_page'),  # page HTML
    path('verifier_page/', verifier_page, name='verifier_page'),
    path('api/upload/', upload_diplome_api, name='api_upload'),  # API
    path('api/verifier/', verifier_diplome_api, name='api_verifier'),
]
