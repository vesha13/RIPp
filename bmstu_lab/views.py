
from django.shortcuts import render
from datetime import date
from bmstu_lab.models import Sneakers

def sneakersList(request):
    return render(request, 'sneakers.html', {'data' : {
        'current_date': date.today(),
        'sneakers': Sneakers.objects.all()
    }})

def GetSneakers(request, id):
    return render(request, 'sneaker1.html', {'data' : {
        'current_date': date.today(),
        'sneaker1': Sneakers.objects.filter(id=id)[0]
    }})




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
