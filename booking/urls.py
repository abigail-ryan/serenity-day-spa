from django.urls import path
from . import views

urlpatterns = [
    path('booking', views.BookingView.as_view(), name='booking'),
    path('booking/edit/int:pk>/', views.BookingEdit.as_view(), name='booking_edit'),
    path('booking/delete/<int:pk>/', views.DeleteBooking.as_view(), name='booking_delete'),
]