from django.urls import path 
from . import views
urlpatterns = [
    path('home/',views.employee_view),
    path('agg/',views.aggregate_view),
]
