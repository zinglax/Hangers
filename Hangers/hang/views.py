from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, QueryDict

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

from hang.models import *


# Dictionary to add objects passed to the through to the HTML
script_args = {}

# Theme
script_args['theme'] = "a"

# Object_Mesh
obj_mesh = []

# Decorators
# 
# Must be logged in
# @login_required
#
# Must be staff
# @user_passes_test(lambda u: u.is_staff)




#Item.objects.all()

#Item.objects.all().filter((Q(name__icontains=search)|Q(description__icontains=search))| (Q(name__icontains=search)&Q(description__icontains=search)))    


#@login_required
#@user_passes_test(lambda u: u.is_staff)
def home(request):
  
  script_args['objects'] = Hanger.objects.all().filter(name='objects')
    
  return render_to_response("hang/home.html", script_args)


# Hangers Methods
def parts(obj):
  ## Gets the parts list of a object
  o = Hanger.objects.all().get(name=obj+'_OBJ')
  parts = Hanger.objects.all().filter(hung_on=o)
  
  parts_list = []
  
  for p in parts:
    parts_list.append(str(p.name))
  
  return parts_list
  