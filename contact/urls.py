from django.urls import path
from .views import contact, apply

urlpatterns = [
    path('', contact),
    path('apply/', apply),
]
