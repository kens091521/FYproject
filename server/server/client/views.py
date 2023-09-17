from django.shortcuts import render, redirect
from django.http import HttpResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from client.serializers import user_detail_Serializer


# Create your views here.
def taoism_detail(request, id): #擴充 input variable
    return HttpResponse(f"Taoism 是道家的英文。道家的學派的幸運數字是{lucky_number}")
 
def confucianism_detail(request, id): #擴充 input variable
    return HttpResponse(f"Confucianism 是儒家的英文。儒家的學派幸運數字是{lucky_number}")

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Schools List':'/school_list',
        'School Detail View':'/school_detail/<int:id>',
        'School Create':'/school_create',
        'School Update':'/school_update/<int:id>',
        'School Delete':'/task-delete/<int:id>'
    }
    return Response(api_urls)
    
@api_view(['GET'])
def user_list(request):
    schools = user_detail.objects.all()
    serializer = user_detail_Serializer(schools, many=True)
    return Response(serializer.data)
 
@api_view(['GET'])
def user_detail(request, id):
    one_school = user_detail.objects.get(id=id)
    serializer = user_detail_Serializer(one_school, many=False)
    return Response(serializer.data)