from django.urls import path

from poincare_quotes import views

urlpatterns = [
    path('', views.index),
]
