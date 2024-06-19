from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='account_login'),
    path('signup', views.signup_view, name='account_signup'),
    path('logout/', views.logout_view, name='account_logout'),
    path('add/', views.record_add, name='record_add'),
    path('delete/<int:id>', views.record_delete, name='record_delete'),
    path('edit/<int:id>', views.record_edit, name='record_edit'),
]