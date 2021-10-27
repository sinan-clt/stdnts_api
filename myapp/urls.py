from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('studnts',views.studnts,name='studnts'),
    path('studnts/<int:id>',views.studnts,name='studnts'),

   



]