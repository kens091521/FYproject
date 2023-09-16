from django.shortcuts import render
import requests
from django.http import HttpResponse 

# Create your views here.
def taoism_detail(request, id): #擴充 input variable
    return HttpResponse(f"Taoism 是道家的英文。道家的學派的幸運數字是{lucky_number}")
 
def confucianism_detail(request, id): #擴充 input variable
    return HttpResponse(f"Confucianism 是儒家的英文。儒家的學派幸運數字是{lucky_number}")


def query_view(request):
    database = 'db.sqlite3'
    table = 'client_user_detail'

    # 从请求中获取查询参数
    query_params = request.GET

    return HttpResponse("查询完成。")

def home(request):
    response = requests.get('http://ip-api.com/json/?fields=61439')
    geodata = response.json()
    return render(request, 'core/home.html', {
        'ip': geodata['query'],
        'country': geodata['country'],
        
    })