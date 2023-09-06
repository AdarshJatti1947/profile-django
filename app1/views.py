from django.shortcuts import render, redirect

# Create your views here.
from .models import personal_information, profesional_details, Projects
# Create your views here.

def index_page(request):
    tasks = personal_information.objects.all()
    tasks2 = profesional_details.objects.all()
    tasks3 = Projects.objects.all()
    return render(request, 'index.html', {'tasks': tasks,'tasks2':tasks2,'tasks3':tasks3})

#def index_page2(request):
#    tasks2=profesional_details.objects.all()
#    return render(request, 'index.html', {'tasks2': tasks2})





