from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.core import serializers
#from healthcareweb.db.mysqlconn import getConnection
#from healthcareweb.models.doctor import Doctor
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import Http404,HttpRequest,HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
import json
from django.db import connection
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from  bmmiici.forms import DoctorForm, PatientForm
from  bmmiici.models import Specialization
from  bmmiici.models import Doctor

def index(request):
    #conn = getConnection()
    return render(request, 'index.html')

def doctor_signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        doctor_form = DoctorForm(request.POST)
        print doctor_form
        # check whether it's valid:
        if doctor_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            doctor_form.save()
            print 'form saved'
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        doctor_form = DoctorForm()

    return render(request, 'index.html', {'doctor_form': doctor_form})

def add_patient(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        patient_form = PatientForm(request.POST)
        print patient_form
        # check whether it's valid:
        if patient_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            patient_form.save()
            print 'form saved'
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        patient_form = PatientForm()

    return render(request, 'index.html', {'patient_form': patient_form})



@require_http_methods(["GET"])
def getAllSpecializations(request):
    queryStr = request.GET['queryStr']
    allSpecializationsOb = Specialization.objects.filter(Q(name__icontains=queryStr))
    allSpecializations = []
    for sp in allSpecializationsOb:
        allSpecializations.append(sp.name)
    return HttpResponse(json.dumps(allSpecializations), content_type="application/json")
