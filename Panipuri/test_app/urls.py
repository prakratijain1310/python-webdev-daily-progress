from django.urls import path
from test_app.views import home , about_us, contact_us

urlpatterns=[
    path('',home,name='home'),
    path('about_us',about_us,name='about_us'),
    path('contact_us',contact_us,name='contact_us'),
    
]
