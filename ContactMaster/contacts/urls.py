from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_contact, name='add_contact'),
    path('list/', views.list_contacts, name='list_contacts'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('search/', views.search_contacts, name='search_contacts'),
]

