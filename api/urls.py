from.views import (TestingApiView)
from django.urls import path

urlpatterns = [
    path('store-data', TestingApiView.as_view(), name='store-data'),
]