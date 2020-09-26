from django.shortcuts import render
from .models import Texts

# Create your views here.
def texts(request):
    texts = Texts.objects.all()
    return render(request, 'texts/texts.html', {'texts':texts})