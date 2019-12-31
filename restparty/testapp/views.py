from django.shortcuts import render
import requests

# Create your views here.
def get_geographic_info(request):
    ip=request.META.get('HTTP_X_FORWARDED_FOR',"")or request.META.get('REMOTE_ADDR')
    print(ip)
    url='http://api.ipstack.com/'+str(ip)+'?access_key=ef203899c2db8422435b02e9420b8151'

    response=requests.get(url)
    data=response.json()
    return render(request,'testapp/info.html',data)
#http://api.ipstack.com/106.210.175.122?access_key=ef203899c2db8422435b02e9420b8151
