import os.path
import time

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.
from .models import Item
from toDoList_backend import settings


#@cache_page(60)

def test_cache(request):
    t=time.time()
    item=Item.objects.filter(title="你好")
    return JsonResponse({'msg':"获取成功",'item':item})
#协商缓存 怎么做
def test_(request):
    t=time.time()
    item=Item.objects.filter(title="你好")
    #响应304表示继续使用 200表示不可用，需要最新资源
    return JsonResponse({'msg':"获取成功",'item':item},status=200)

def test_upload(request):
    file=request.FILES.get("file")
    if not file :
        return JsonResponse({'msg':'文件未上传','errno':1},safe=False)
    file_name=os.path.join(settings.MEDIA_ROOT,file.name)
    with open(file_name,'wb')as f:
        data=file.file.read()
        f.write(data)
    return JsonResponse({'msg':"接收成功"},safe=False)