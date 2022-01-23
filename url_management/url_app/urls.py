from django.urls import path,include
from url_app import views

urlpatterns = [
    path('', views.home,name='homepage'),
    
    

]