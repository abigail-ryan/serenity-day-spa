from . import views
from django.urls import path

urlpatterns = [
    path("treatments/", views.TreatmentList.as_view(), name='treatments'),
    path('<slug:slug>/', views.treatment_details, name="treatment_details")
]