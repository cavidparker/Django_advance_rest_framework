from django.urls import path
from .views import firstAPI,registrationAPI, ContactAPIView

urlpatterns =[
    path('first/',firstAPI),
    path('registration/',registrationAPI),
    path('contact/',ContactAPIView.as_view(),name='contact'),


]