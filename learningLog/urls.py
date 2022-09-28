from django.urls import path
from . import views

urlpatterns = [
    path("<str:month>", views.monthly_learning),
    path("<int:month>", views.monthly_learning_by_number)
]