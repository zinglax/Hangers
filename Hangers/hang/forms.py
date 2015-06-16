from django import forms
from hang.models import *

class Hanger_Form(forms.Form):
    
    # Name of Hanger
    name = forms.CharField(max_length=150, min_length=None)
    
    # Where is this Hanger Hung
    hung_on = forms.ModelChoiceField(queryset=Hanger.objects.all(), empty_label="None")
        
    def __unicode__(self):        
        return unicode(self.name)

class Str_Hanger_Form(Hanger_Form):
    # String (ex. hello)
    data = forms.CharField(max_length=500) 

     

class IntegerField_Hanger_Form(Hanger_Form):
    # int (ex. hello)
    data = forms.IntegerField()
             

class BooleanField_Hanger_Form(Hanger_Form):
    # Boolean Value (ex. True)
    data = forms.BooleanField

 

class BigIntegerField_Hanger_Form(Hanger_Form):
    data = forms.IntegerField(max_value=9223372036854775807, min_value=-9223372036854775808)
                    
    
class CharField_Hanger_Form(Hanger_Form):
    data = forms.CharField(max_length=255)    

     

class CommaSeparatedIntegerField_Hanger_Form(Hanger_Form):
    data = forms.CharField()
    
     


class DateField_Hanger_Form(Hanger_Form):
    data = forms.DateField()
    
     

class DateTimeField_Hanger_Form(Hanger_Form):
    data = forms.DateTimeField()
    
     


class DecimalField_Hanger_Form(Hanger_Form):
    data = forms.DecimalField()
    
     


class EmailField_Hanger_Form(Hanger_Form):
    data = forms.EmailField()
    
     

class FileField_Hanger_Form(Hanger_Form):
    data = forms.FileField()
    
     

class FilePathField_Hanger_Form(Hanger_Form):
    data = forms.FilePathField(path='.', match=None, recursive=False, 
                              allow_files=True, 
                              allow_folders=False, 
                              required=True, 
                              widget=None, 
                              label=None, 
                              initial=None, 
                              help_text=None)
    
     

class FloatField_Hanger_Form(Hanger_Form):
    data = forms.FloatField()
    
     

class ImageField_Hanger_Form(Hanger_Form):
    data = forms.ImageField()
    
     

class IPAddressField_Hanger_Form(Hanger_Form):
    data = forms.IPAddressField()
    
     

class GenericIPAddressField_Hanger_Form(Hanger_Form):
    data = forms.GenericIPAddressField()
    
     

class NullBooleanField_Hanger_Form(Hanger_Form):
    data = forms.CharField()
    
     

class PositiveIntegerField_Hanger_Form(Hanger_Form):
    data = forms.IntegerField()
    
     

class PositiveSmallIntegerField_Hanger_Form(Hanger_Form):
    data = forms.IntegerField()
    
     

class SlugField_Hanger_Form(Hanger_Form):
    data = forms.SlugField()
    
     

class SmallIntegerField_Hanger_Form(Hanger_Form):
    data = forms.IntegerField()
     

    
   

class TextField_Hanger_Form(Hanger_Form):
    data = forms.CharField(widget=forms.Textarea)
    
     

class TimeField_Hanger_Form(Hanger_Form):
    data = forms.TimeField()
    
     


class URLField_Hanger_Form(Hanger_Form):
    data = forms.URLField()
    
     

class ForeignKey_Hanger_Form(Hanger_Form):
    data = forms.ModelChoiceField(queryset=ForeignKey_Hanger.objects.all())


class ManyToManyField_Hanger_Form(Hanger_Form):
    data = forms.ModelMultipleChoiceField(queryset=ManyToManyField_Hanger.objects.all())