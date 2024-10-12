from django.urls import path
from . import views
from django.conf.urls import handler404
from django.conf.urls import handler500
from .views import custom_handler404, custom_handler500

urlpatterns = [
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('booking/edit/<int:pk>/',
         views.BookingEdit.as_view(),
         name='booking-edit'),
    path('booking/delete/<int:pk>/',
         views.DeleteBooking.as_view(), name='booking-delete'),
]

handler404 = custom_handler404
handler500 = custom_handler500
