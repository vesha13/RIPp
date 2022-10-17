from django.urls import path
from django.contrib import admin
from bmstu_lab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetOrders),
    path('order/<int:id>/', views.GetOrder, name='order_url'),
]

path('', views.sneakersList),
path('sneaker1/<int:id>/', views.GetSneakers, name='sneaker1_url')