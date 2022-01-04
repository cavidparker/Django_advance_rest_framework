from django.urls import path
from .views import firstAPI,registrationAPI

urlpatterns =[
    path('first/',firstAPI),
    path('reg/',registrationAPI),

]