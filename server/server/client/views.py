from django.shortcuts import render
from django.http import HttpResponse
 
def taoism_detail(request):
    return HttpResponse("Taoism 是道家的英文。")
 
def confucianism_detail(request):
    return HttpResponse("Confucianism 是儒家的英文")