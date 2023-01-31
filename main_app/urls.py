from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('art/', views.ArtList.as_view(), name="art_list"),
    path('artists/new/', views.ArtCreate.as_view(), name="art_create"),
    path('art/<int:pk>/', views.ArtDetail.as_view(), name="art_detail"),
    path('art/<int:pk>/update',views.ArtUpdate.as_view(), name="art_update"),
]