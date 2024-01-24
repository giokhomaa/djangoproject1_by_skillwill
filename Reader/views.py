from django.shortcuts import render
from Reader.models import Reader

def personal_data(request):
    return render(request, 'personal.html')
