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

from  bmmiici.forms import DoctorForm

def index(request):
    #conn = getConnection()
    return render(request, 'index.html')

def doctor_signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        doctor_form = DoctorForm(request.POST)
        #print doctor_form
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
