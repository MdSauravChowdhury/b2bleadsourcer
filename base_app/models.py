from django.db import models
from django.contrib.auth.models import User
from service.models import Category
from ckeditor.fields import RichTextField
from django.shortcuts import reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ContactWithItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)    
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} need by || {self.category}"

class About(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    sub_content = models.TextField(blank=True, null=True)
    Project_Complete = models.IntegerField(default=1, blank=True, null=True)
    Happy_Clients = models.IntegerField(default=1, blank=True, null=True)
    Business_Partners = models.IntegerField(default=1, blank=True, null=True)
    B2b_Consultant = models.IntegerField(default=1, blank=True, null=True) 
    left_banner_image = models.ImageField(upload_to="promo/img", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title

class AboutPromoTitle(models.Model):
    promo_head_title = models.CharField(max_length=50, blank=True, null=True)
    promo_head_sub_content = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.promo_head_title     

class AboutPromoBanner(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="banner/img", blank=True, null=True)

    def __str__(self):
        return self.title
    

class AboutPromoLeftItem(models.Model):
    icon = models.ImageField(upload_to="img/icon", blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    sub_content = models.CharField(max_length=100, blank=True, null=True)
    plank_left = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class AboutPromoRightItem(models.Model):
    icon = models.ImageField(upload_to="img/icon", blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    sub_content = models.CharField(max_length=100, blank=True, null=True)
    plank_right = models.BooleanField(default=False)  

    def __str__(self):
        return self.title      
    

class AboutTeam(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Category, on_delete=models.CASCADE)
    worker_about = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="worker/img", blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} department is {self.department.name}"

class BlogCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
  
class Blog(models.Model):
    author = models.ForeignKey(AboutTeam, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    many_category = models.ManyToManyField(BlogCategory)
    updated_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/image")
    slug = models.SlugField(blank=True, null=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog-singel", kwargs={"slug": self.slug})        
