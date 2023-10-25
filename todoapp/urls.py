from django.urls import path
from todoapp import views

urlpatterns = [
    path('', views.new2, name='new2'),
    path('tasks',views.tasks, name='tasks'),
    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('update/<int:id>',views.update, name='update'),
    path('update/updaterecord/<int:id>',views.updaterecord, name='updaterecord'),
    
]