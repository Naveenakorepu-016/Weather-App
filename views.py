from django.shortcuts import render
import requests

# Create your views here.
def weather(request):
    e=''
    name=request.GET.get('name')
    api_keys="1844f66645a1045ef731cfd3574c2d99"
    URL=f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api_keys}"
    res=requests.get(url=URL)
    data=res.json()
    temp1=data['main']['temp']-273.15
    temp=int(temp1)
    if  10<=temp <30:
        e='🌞'
    elif 0<=temp <10:
        e='⛅'
    elif temp <0:
        e='❄️'
    else:
        e=' Heavy heat'
    mintemp=data['main']['temp_min']-273.15
    maxtemp=data['main']['temp_max']-273.15

    

    context={
        'e':e,
        'name':name,
        'data':data,
        'temp':temp,
        'min':mintemp,
        'max':maxtemp
    }
    
    return render(request,'weather.html',context)
