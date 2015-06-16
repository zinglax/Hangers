from django.db import models

####################################################
## Hangers: Objects that store only one type of django data field that can also point to eachother
##
class Hanger(models.Model):
    
    # Name of Hanger
    name = models.CharField(max_length=150, blank=True, null=True) 
    
    # Where is this Hanger Hung
    hung_on = models.ForeignKey('self', blank=True, null=True,on_delete=models.SET_NULL, related_name='Hanger' )
    
        
    def __unicode__(self):        
        return unicode(self.name)

class Str_Hanger(Hanger):
    # String (ex. hello)
    data = models.CharField(max_length=500, blank=True, null=True) 

    def __unicode__(self):        
        return unicode(self.data)

class IntegerField_Hanger(Hanger):
    # int (ex. hello)
    data = models.IntegerField(blank=True, null=True)

    def __unicode__(self):        
        return unicode(self.data)
    
    

class BooleanField_Hanger(Hanger):
    # Uses null boolean because it is not required and must be able to be Null
    data = models.NullBooleanField(blank=True, null=True)

    def __unicode__(self):        
        return unicode(self.data)

   

class BigIntegerField_Hanger(Hanger):
    data = models.BigIntegerField(blank=True, null=True)
    
    
    def __unicode__(self):        
        return unicode(self.data)
    
    
    
class CharField_Hanger(Hanger):
    data = models.CharField(max_length=255, blank=True, null=True)    

    def __unicode__(self):        
        return unicode(self.data)

class CommaSeparatedIntegerField_Hanger(Hanger):
    data = models.CommaSeparatedIntegerField(max_length=255, blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)


class DateField_Hanger(Hanger):
    data = models.DateField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class DateTimeField_Hanger(Hanger):
    data = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)


class DecimalField_Hanger(Hanger):
    data = models.DecimalField(decimal_places=255, max_digits=255, blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)


class EmailField_Hanger(Hanger):
    data = models.EmailField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class FileField_Hanger(Hanger):
    data = models.FileField(upload_to='/Hangers/FileField_Hanger', blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class FilePathField_Hanger(Hanger):
    data = models.FilePathField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class FloatField_Hanger(Hanger):
    data = models.FloatField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class ImageField_Hanger(Hanger):
    data = models.ImageField(upload_to='/Hangers/FileField_Hanger', blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class IPAddressField_Hanger(Hanger):
    data = models.IPAddressField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class GenericIPAddressField_Hanger(Hanger):
    data = models.GenericIPAddressField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class NullBooleanField_Hanger(Hanger):
    data = models.NullBooleanField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class PositiveIntegerField_Hanger(Hanger):
    data = models.PositiveIntegerField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class PositiveSmallIntegerField_Hanger(Hanger):
    data = models.PositiveSmallIntegerField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class SlugField_Hanger(Hanger):
    data = models.SlugField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class SmallIntegerField_Hanger(Hanger):
    data = models.SmallIntegerField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

    
   

class TextField_Hanger(Hanger):
    data = models.TextField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class TimeField_Hanger(Hanger):
    data = models.TimeField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)


class URLField_Hanger(Hanger):
    data = models.URLField(blank=True, null=True)
    
    def __unicode__(self):        
        return unicode(self.data)

class ForeignKey_Hanger(Hanger):
    data = models.ForeignKey("Hanger", related_name='ForeignKey_Hanger',
                                     verbose_name=('data'))
    
    def __unicode__(self):        
        return unicode(self.data)

class ManyToManyField_Hanger(Hanger):
    data = models.ManyToManyField("Hanger", related_name='ManyToManyField_Hanger',
                                     verbose_name=('data'))
    
    def __unicode__(self):        
        return unicode(self.data)

class OneToOneField_Hanger(Hanger):
    data = models.OneToOneField("Hanger", related_name='OneToOneField_Hanger',
                                     verbose_name=('data'))
    
    def __unicode__(self):        
        return unicode(self.data)

#class _Hanger(Hanger):
    #data = models. (blank=True, null=True)
    
    #def __unicode__(self):        
        #return unicode(self.data)
