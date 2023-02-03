from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('therapy/', views.TherapyList.as_view(), name="therapy"),
    path('therapy/<int:pk>/', views.TherapyDetail.as_view(), name="therapy_detail"),
    path('journal/', views.JournalList.as_view(), name="journal_list"),
    path('journalists/new/', views.JournalCreate.as_view(), name="journal_create"),
    path('journal/<int:pk>/', views.JournalDetail.as_view(), name="journal_detail"),
    path('journal/<int:pk>/update',views.JournalUpdate.as_view(), name="journal_update"),
    path('journal/<int:pk>/delete',views.JournalDelete.as_view(), name="journal_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]