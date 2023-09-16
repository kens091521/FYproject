from django.urls import path
from client import views
 
urlpatterns = [
    path("Confucianism/<int:lucky_number>", views.confucianism_detail, name="confucianism"),
    path("Taoism/<int:lucky_number>", views.taoism_detail, name="taosim"),
    path('query/', views.query_view, name='query-view'),
    path('', views.home, name='home'),
]