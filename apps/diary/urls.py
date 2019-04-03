from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('addentry/', views.EntryCreateView.as_view(), name='addentry'),
    path('entry/<int:pk>/', views.EntryDetailView.as_view(), name='entry'),
    #timeline should be in home
    #path('timeline/', views.TimelineView.as_view(), name='timeline'),
    path('archive/', views.ArchiveView.as_view(), name='archive'),
    

]

