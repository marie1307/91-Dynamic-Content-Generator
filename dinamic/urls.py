from django.urls import path
from .import views

urlpatterns = [
    path('main/<str:name>', views.main, name='name'),
]
