from django.urls import path
from .views import DataList

urlpatterns = [
    path('data/', DataList.as_view(), name="data-list")
]
