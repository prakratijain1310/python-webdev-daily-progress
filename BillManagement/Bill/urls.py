from django.urls import path
from Bill.views import home_bill 

urlpatterns=[
    path('',home_bill,name='home_bill'),
    
]