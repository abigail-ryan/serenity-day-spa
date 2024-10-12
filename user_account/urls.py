from .views import UserAccount
from django.urls import path

urlpatterns = [
    path("my-account/", UserAccount.as_view(), name='my-account'),
]
