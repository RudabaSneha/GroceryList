from django.urls import path 
from . import views
#from .forms import LoginForm
app_name = 'main'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('item/list/', views.items, name="itemList"),
    path('item/create', views.itemCreate.as_view(), name="itemCreate"),
    path('item/update/<pk>', views.itemUpdate.as_view(),name='itemUpdate'),
    path('item/delete/<pk>', views.itemDelete.as_view(),name='itemDelete'),
]