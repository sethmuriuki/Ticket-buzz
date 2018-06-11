from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Tickets, Categories, Location, Events
# Create your views here.

def index(request):
    tickets = Tickets.objects.all()
    return render(request, 'index.html', {'tickets':tickets})