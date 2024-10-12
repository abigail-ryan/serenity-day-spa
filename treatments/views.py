from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Treatment


# Create your views here.
class TreatmentList(generic.ListView):
    queryset = Treatment.objects.filter(status=1)
    template_name = "treatments/treatments.html"
    paginate_by = 6


def treatment_details(request, slug):

    queryset = Treatment.objects.filter(status=1)
    treatment = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "treatments/treatment_details.html",
        {"treatment": treatment},
    )
