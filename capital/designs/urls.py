from django.urls import path
from . import views

urlpatterns = [
    path('designs',views.designs,name='designs')
]
