from django.urls import path
from artykul.views import artykuly,artykul, artykul_create

urlpatterns = [
    path('',artykuly, name="artykul-list"),
    path('<int:pk>/',artykul, name="artykul-details"),
    path("create/", artykul_create, name="artykul-create")
]