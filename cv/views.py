from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import CV

def cv_view(request):
    cv = CV.objects.first() # On récupère le premier CV enregistré en base de données
    context = {
        'cv': cv
    }
    return render(request, 'cv/cv.html', context)
