from django.urls import path
from user.api.views import LegalHomiyCreationView, HomiyCreationView


urlpatterns = [
    path('legalentity/create/', LegalHomiyCreationView.as_view()),
    path('homiy/create/', HomiyCreationView.as_view()),
]
