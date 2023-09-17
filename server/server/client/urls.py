from django.urls import path
from client import views
 
urlpatterns = [
    path("Confucianism/<int:lucky_number>", views.confucianism_detail, name="confucianism"),
    path("Taoism/<int:lucky_number>", views.taoism_detail, name="taosim"),
    path("", views.api_overview, name="api_overview"),
    path("user_list", views.user_list, name="user_list"),
    #path("school_create", views.school_create, name="school_create"),
    #path("school_update/<int:id>", views.school_update, name="school_update"),
    #path("school_delete/<int:id>", views.school_delete, name="school_delete")
]