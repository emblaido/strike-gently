from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('therapy/', views.Therapy.as_view(), name="therapy"),
    path('journal/', views.JournalList.as_view(), name="journal_list"),
    path('journalists/new/', views.JournalCreate.as_view(), name="journal_create"),
    path('journal/<int:pk>/', views.JournalDetail.as_view(), name="journal_detail"),
    path('journal/<int:pk>/update',views.JournalUpdate.as_view(), name="journal_update"),
    path('journal/<int:pk>/delete',views.JournalDelete.as_view(), name="journal_delete"),
    path('therapy/', views.Therapy.as_view(), name="therapy"),
]