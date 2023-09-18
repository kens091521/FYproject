from django.contrib import admin
from django.urls import path
from django.urls import include 

urlpatterns = [
    path('admin/', admin.site.urls), # 別忘記逗點囉!
    path("", include("client.urls")), # 和多這一行
  
]