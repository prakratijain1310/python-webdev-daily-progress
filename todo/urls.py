from django.urls import path
from todo.views import home ,update,delete

urlpatterns=[
    path('',home,name='hometodo'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),   
]
