from django.db import models
# from fontawesome_5.fields import IconField
from ckeditor.fields import RichTextField
from django.shortcuts import reverse

# Create your models here.
class ServiceItem(models.Model):
    # icon = IconField(blank=True, null=True)
    icon_v2 = models.ImageField(upload_to="icon/img", blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    details = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title


class ServicePrice(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("order", kwargs={"id": self.id})
    

# class ServiceContact(models.Model):
#     item = models.ForeignKey(ServicePrice, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(blank=True, null=True , max_length=50)   

    def __str__(self):
        return self.name

class StrategicWork(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)   
    title = models.CharField(max_length=250, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to="work/image", blank=True, null=True)
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("service_item", kwargs={"id": self.id})


class TermsAndConditions(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

        

class PrivacyAndPolicy(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

        

class RefundPolicy(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

        
class LeadGeneration(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title    

class ClientsFeedback(models.Model):
    work_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, blank=True, null=True)
    message = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to="client/image")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class OurCorporateClient(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="corporate/client")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name
