from django.shortcuts import render
from .models import Studio

# Create your views here.
def studio(request):
    studios = Studio.objects.all()
    return render(request, 'studio/studio.html', {'studios':studios})