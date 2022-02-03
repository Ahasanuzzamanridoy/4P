from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Receivebook
import datetime

# Create your views here.


def home(request):
    Receivebooks = Receivebook.get_all_Receivebooks();
    data = {}
    data['Receivebooks'] = Receivebooks
    data['datetime'] = datetime.datetime.now()
    #return render(request, 'myapp/received.html', context={"now": now})
    return render(request, 'myapp/received.html', data)




def receivetable(request):
    Bookid1 = request.POST.get("book")
    Ficode1 = request.POST.get("fi")
    Date1 = request.POST.get("date")

    o_ref = Receivebook(id=[0], Bookid=Bookid1, Ficode=Ficode1, Date=Date1)
    o_ref.save()

    return render(request, 'myapp/received.html', {"message": "Save Sucessfully"})







