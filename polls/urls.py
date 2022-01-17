from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.FormView.as_view(),name="formpage"),
    path('doui/', views.ChoiceView.as_view(), name="doui"),
    path('welcome/', views.PrivacyView, name='welcome'),
]