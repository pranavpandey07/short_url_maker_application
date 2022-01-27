from django.urls import path,include
from url_app import views
from url_app.views import home

urlpatterns = [
    path('',views.home,name='homepage'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('login/home/',views.home,name="redirectedhome"),
    path('logout/',views.logout,name='logout'),
    path('logout/login/',views.login,name='redirectedlogin')
    
    

]