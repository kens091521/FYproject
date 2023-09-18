from django.shortcuts import render, redirect
from django.http import HttpResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from client.serializers import user_detail_Serializer
from client.models import *
from django.core import serializers



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
def user_list(request, table):
    response = user_detail.objects.all()
    geodata = serializers.serialize('json', response)
    context = {
        'geodata': geodata,
    }
    return render(request, 'database/index.html', context)

@api_view(['POST'])
def signUp(request):
   
        params = request.GET
        
        # 取得模型名稱
        model_name = params.get('model')
        
        # 檢查模型是否存在
        model = apps.get_model(app_label='your_app', model_name=model_name)
        
        if not model:
            return HttpResponse(f"Model '{model_name}' does not exist.")
        
        # 檢查參數是否合法
        valid_fields = model._meta.get_fields()
        insert_data = {}
        
        for field in valid_fields:
            field_name = field.name
            field_value = params.get(field_name)
            
            if field_value is not None:
                insert_data[field_name] = field_value
        
        # 插入資料到資料庫
        model.objects.create(**insert_data)
        
        return HttpResponse("Data inserted successfully.")
