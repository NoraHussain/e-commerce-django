
from django.urls import path, include
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.products_list),
    path('<slug:slug>', views.product_details, name='product_details')

]
