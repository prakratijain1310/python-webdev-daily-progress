from django.urls import path
from Inventory.views import home_inventory , update, delete

urlpatterns=[
    path('',home_inventory,name='home_inventory'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
]