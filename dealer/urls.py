from django.urls import path
from . import views


urlpatterns = [
    path('',views.login,name = 'login'),
    path('dealer_dashboard',views.dealer_dashboard,name = 'dealer_dashboard'),
    path('logout',views.logout,name = 'logout'),
    
]