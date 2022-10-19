from django.urls import path
from django.contrib import admin
from bmstu_lab import views

urlpatterns = [
    path('admin/', admin.site.urls),



path('', views.medicineList),
path('medicine/<int:id>/', views.GetMedicine, name='medicine_url'),

path('', views.clientList),
path('client/<int:id>/', views.GetClient, name='client_url'),

path('', views.chartList),
path('chart/<int:id>/', views.GetCharts, name='chart_url')
]