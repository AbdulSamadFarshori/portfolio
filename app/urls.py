from.views import (HomeView)
from django.urls import path

urlpatterns = [
    path('index',HomeView.as_view(), name='home'),
]