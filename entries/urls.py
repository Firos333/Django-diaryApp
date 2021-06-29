from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.logg, name='login'),
    path('add/', views.add, name='add'),
    path('viewdiary/<int:id>', views.viewdiary, name='viewdiary'),
    path('logout',views.logout,name='logout'),
    path('home',views.index,name='home'),
    path('registerr',views.registerr,name='registerr'),
]
