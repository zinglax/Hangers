from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, QueryDict

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

# All Models and Forms Imported
from .models import *
from .forms import *


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
  
  
  
  form_names = ['Hanger_Form', 'Str_Hanger_Form', 'IntegerField_Hanger_Form', 'BooleanField_Hanger_Form', 'BigIntegerField_Hanger_Form', 'CharField_Hanger_Form', 'CommaSeparatedIntegerField_Hanger_Form', 'DateField_Hanger_Form', 'DateTimeField_Hanger_Form', 'DecimalField_Hanger_Form', 'EmailField_Hanger_Form', 'FileField_Hanger_Form', 'FilePathField_Hanger_Form', 'FloatField_Hanger_Form', 'ImageField_Hanger_Form', 'IPAddressField_Hanger_Form', 'GenericIPAddressField_Hanger_Form', 'NullBooleanField_Hanger_Form', 'PositiveIntegerField_Hanger_Form', 'PositiveSmallIntegerField_Hanger_Form', 'SlugField_Hanger_Form', 'SmallIntegerField_Hanger_Form', 'TextField_Hanger_Form', 'TimeField_Hanger_Form', 'URLField_Hanger_Form', 'ForeignKey_Hanger_Form', 'ManyToManyField_Hanger_Form']

  forms = []
  for f in form_names:
    forms.append(eval(f+"()"))
  
  form_dic = {} # name and form
  for i,v in enumerate(forms[:]):
    form_dic[form_names[i]] = v
  
  script_args['forms'] = form_dic
  
  usr_name = Hanger.objects.get(name='USR_EMAIL')
  print usr_name.__class__.__name__
  
    
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
  