from django.urls import path,include
from urlhandler import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('generate/',views.generate,name='generate'),
    path('<str:query>/',views.home,name='home')
    
    

]