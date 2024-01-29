from django.urls import path
from user.api.views import (LegalHomiyCreationView, HomiyCreationView, HomiylarView, HomiySingleRetrieveView,
                            HomiyRetrieveUpdateView, TalabaListCreateView)


urlpatterns = [
    path('legalentity/create/', LegalHomiyCreationView.as_view()),
    path('homiy/create/', HomiyCreationView.as_view()),
    path('homiylar/', HomiylarView.as_view()),

    path('homiy/<int:pk>/', HomiySingleRetrieveView.as_view()),
    path('homiy-update/<int:pk>/', HomiyRetrieveUpdateView.as_view()),

    path('talaba/list-create/', TalabaListCreateView.as_view()),
]
