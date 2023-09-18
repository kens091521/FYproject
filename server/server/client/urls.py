from django.urls import path
from client import views
 
urlpatterns = [
    path("Confucianism/<int:lucky_number>", views.confucianism_detail, name="confucianism"),
    path("Taoism/<int:lucky_number>", views.taoism_detail, name="taosim"),
    path("", views.api_overview, name="api_overview"),
    path("displayList/<str:table>", views.user_list, name="user_list"),
    path("userSignUp", views.signUp, name="school_create"),
    #path("school_update/<int:id>", views.school_update, name="school_update"),
    #path("school_delete/<int:id>", views.school_delete, name="school_delete")
]