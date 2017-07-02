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



def index(request):
    #conn = getConnection()
    return render(request, 'index.html')