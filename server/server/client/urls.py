from django.urls import path
from client import views
 
urlpatterns = [
    path("Confucianism", views.confucianism_detail, name="confucianism"),
    path("Taoism", views.taoism_detail, name="taosim")
]