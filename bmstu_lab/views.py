
from django.shortcuts import render
from datetime import date
from bmstu_lab.models import Medicines
from bmstu_lab.models import Clients
from bmstu_lab.models import Charts

def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})
image=['k', 'https://api.meet-market.ru/images/2193345.jpg?q=100&h=2000&w=2000', 'https://avatars.mds.yandex.net/get-mpic/5268102/img_id8587941560124486628.jpeg/orig', 'https://avatars.mds.yandex.net/get-mpic/5362248/img_id8905869643384084506.jpeg/orig'];

def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': [
            {'title': 'Nike air force 1', 'id': 1, 'img': 'https://api.meet-market.ru/images/2193345.jpg?q=100&h=2000&w=2000'},
            {'title': 'Adidas ozweego', 'id': 2, 'img': 'https://avatars.mds.yandex.net/get-mpic/5268102/img_id8587941560124486628.jpeg/orig'},
            {'title': 'Diadora heritage', 'id': 3, 'img': 'https://avatars.mds.yandex.net/get-mpic/5362248/img_id8905869643384084506.jpeg/orig'},
        ]
    }})

def GetOrder(request, id):
    return render(request, 'order.html', {'data': {
        'current_date': date.today(),
        'img': image[id],
        'id': id
    }})



def medicineList(request):
    return render(request, 'medicines.html', {'data' : {
        'current_date': date.today(),
        'medicines': Medicines.objects.all()
    }})

def GetMedicine(request, id):
    return render(request, 'medicine.html', {'data' : {
        'current_date': date.today(),
        'medicine': Medicines.objects.filter(id=id)[0],
    }})

def clientList(request):
    return render(request, 'clients.html', {'data' : {
        'current_date': date.today(),
        'clients': Clients.objects.all()
    }})

def GetClient(request, id):
    return render(request, 'client.html', {'data' : {
        'current_date': date.today(),
        'client': Clients.objects.filter(id=id)[0],
    }})

def chartList(request):
    return render(request, 'charts.html', {'data' : {
        'current_date': date.today(),
        'charts': Charts.objects.all()
    }})

def GetCharts(request, id):
    return render(request, 'chart.html', {'data' : {
        'current_date': date.today(),
        'chart': Charts.objects.filter(id=id)[0],
    }})

