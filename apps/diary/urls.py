from django.urls import path

from . import views


app_name = 'diary'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('add/', views.PostCreateView.as_view(), name='add'),
    path('entry/<int:pk>/', views.EntryDetailView.as_view(), name='entry'),
    path('archive/', views.ArchiveView.as_view(), name='archive'),
    

]

