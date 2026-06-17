from django.urls import path
from .import views
urlpatterns=[ 
  path('', views.index,name="home"),
  path('delete/<int:id>', views.deletetask,name='delete'),
  path('update/<int:id>', views.updatetask,name='update')
]