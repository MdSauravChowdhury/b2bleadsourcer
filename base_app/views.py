from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView

from service.models import (ServiceItem, ServicePrice, StrategicWork, Category, 
TermsAndConditions, PrivacyAndPolicy, RefundPolicy, ClientsFeedback, OurCorporateClient
)

from .models import (Contact, ContactWithItem, About, AboutPromoRightItem, AboutPromoLeftItem,
 AboutPromoTitle, AboutPromoBanner, AboutTeam, Blog)

from lead.models import LeadService

from base_app.forms import ContactForm

# Create your views here.

def search(request):
    queryset = Blog.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)

def get_category_count():
    queryset = Blog.objects.values('many_category__name').annotate(Count('many_category__name'))
    return queryset


def IndexTemplateView(request):
    # db query
    service = ServiceItem.objects.all().order_by('-id')
    serviceTop = ServiceItem.objects.all()[:3]
    service_price = ServicePrice.objects.all()
    strategic_work = StrategicWork.objects.all()
    category = Category.objects.all()
    AboutIndex = About.objects.all()
    AboutTeamIndex = AboutTeam.objects.all()
    AboutPromoIndex = AboutPromoTitle.objects.all()
    AboutLeftPromoIndex = AboutPromoLeftItem.objects.all()
    AboutPromoTitleIndex = AboutPromoTitle.objects.all()
    AboutMedelPromoIndex = AboutPromoBanner.objects.all()
    AboutRightPromoIndex = AboutPromoRightItem.objects.all()
    blog_Post = Blog.objects.all().order_by('-timestamp')[:3]
    # Form Validation

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        name = request.POST['name']
        phone = request.POST['phone']
        email_from = settings.EMAIL_HOST_USER


        contact_v2 = ContactWithItem(name=name, email=email, phone=phone, subject=subject, message=message)
        contact_v2.save()

        try:
            send_mail(subject, message, email, [email_from], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('/')    

    return render(request, 'index.html', context={
        'service': service,
        'service_price': service_price,
        'strategic_work': strategic_work,
        'category': category,
        
        'about': AboutIndex,
        'serviceTop': serviceTop,
        'AboutTeam': AboutTeamIndex,
        'blog_Post': blog_Post,
        'AboutPromo': AboutPromoIndex,
        'AboutLeftPromo': AboutLeftPromoIndex,
        'AboutPromoTitle': AboutPromoTitleIndex,
        'AboutMedelPromo': AboutMedelPromoIndex,
        'AboutRightPromo': AboutRightPromoIndex
    })

class AboutTemplateView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service_price"] = ServicePrice.objects.all()
        context["about"] = About.objects.all()

        context["AboutTeam"] = AboutTeam.objects.all()
        
        context["AboutPromo"] = AboutPromoTitle.objects.all()
        context["AboutLeftPromo"] = AboutPromoLeftItem.objects.all()
        context["AboutPromoTitle"] = AboutPromoTitle.objects.all()
        context["AboutMedelPromo"] = AboutPromoBanner.objects.all()
        context["AboutRightPromo"] = AboutPromoRightItem.objects.all()
        return context
    


class ServiceTemplateView(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = ServiceItem.objects.all()
        context["service_price"] = ServicePrice.objects.all()
        context["strategic_work"] = StrategicWork.objects.all()
        return context
    

class CasesTemplateView(TemplateView):
    template_name = "cases.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["strategic_work"] = StrategicWork.objects.all()
        return context
    

class BlogTemplateView(ListView):
    model = Blog
    context_object_name = "blog_post"
    template_name = "blog.html"


class SingelBlogPost(DetailView):
    model = Blog
    context_object_name = "blog_detail"
    template_name = "blog-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_three_post"] = Blog.objects.all().order_by('-timestamp')
        context["category_count"] = get_category_count()
        return context
    

def ContactTemplateView(request):

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        name = request.POST['name']
        phone = request.POST['phone']
        email_from = settings.EMAIL_HOST_USER


        contact = ContactWithItem(name=name, email=email, phone=phone, subject=subject, message=message)
        contact.save()

        try:
            send_mail(subject, message, email, [email_from], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('/')    
                
    return render(request, "contact.html")


def CategoryBaseWork(request, id):
    strategic_Work = get_object_or_404(StrategicWork, pk=id)

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        name = request.POST['name']
        phone = request.POST['phone']
        email_from = settings.EMAIL_HOST_USER


        contact_v2 = ContactWithItem(name=name, email=email, phone=phone, subject=subject, message=message)
        contact_v2.save()

        try:
            send_mail(subject, message, email, [email_from], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('/')    

    return render(request, 'work_details.html', context={
        'strategic_Work': strategic_Work
    })   

class TermsConditionView(TemplateView):
    template_name = "termsamp_conditions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trams_policy"] = TermsAndConditions.objects.all()
        return context
    


class PrivacyAndPolicyView(TemplateView):
    template_name = "privacy_policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["privacy_policy"] = PrivacyAndPolicy.objects.all()
        return context
    
def ServicePriceDetail(request, id):
    item = get_object_or_404(ServicePrice, pk=id)

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        name = request.POST['name']
        phone = request.POST['phone']
        email_from = settings.EMAIL_HOST_USER


        contact_v2 = ContactWithItem(name=name, email=email, phone=phone, subject=subject, message=message)
        contact_v2.save()

        try:
            send_mail(subject, message, email, [email_from], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('/')    

    return render(request, 'order.html', context={
        'order': item
    })

class RefundPolicyView(TemplateView):
    template_name = "refund_policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["refund_policy"] = RefundPolicy.objects.all()
        return context
    
# service pages
def leadGeneration(request):

    lead = LeadService.objects.all()
    feedback = ClientsFeedback.objects.all()
    corporate = OurCorporateClient.objects.all()


    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        name = request.POST['name']
        phone = request.POST['phone']
        email_from = settings.EMAIL_HOST_USER


        contact = ContactWithItem(name=name, email=email, phone=phone, subject=subject, message=message)
        contact.save()

        try:
            send_mail(subject, message, email, [email_from], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('/')    
                
    return render(request, "leadGeneration.html", context={
        'lead': lead,
        'feedback': feedback,
        'corporate': corporate
    })    


def linkdinResearch(request):

    lead = LeadService.objects.all()
    feedback = ClientsFeedback.objects.all()
    corporate = OurCorporateClient.objects.all()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        name = request.POST['name']
        phone = request.POST['phone']
        email_from = settings.EMAIL_HOST_USER


        contact = ContactWithItem(name=name, email=email, phone=phone, subject=subject, message=message)
        contact.save()

        try:
            send_mail(subject, message, email, [email_from], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('/')    
                
    return render(request, "linkdinResearch.html", context={
        'lead': lead,
        'feedback': feedback,
        'corporate': corporate
    })


def listBuilding(request):

    lead = LeadService.objects.all()
    feedback = ClientsFeedback.objects.all()
    corporate = OurCorporateClient.objects.all()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        name = request.POST['name']
        phone = request.POST['phone']
        email_from = settings.EMAIL_HOST_USER


        contact = ContactWithItem(name=name, email=email, phone=phone, subject=subject, message=message)
        contact.save()

        try:
            send_mail(subject, message, email, [email_from], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('/')    
                
    return render(request, "listBuilding.html", context={
        'lead': lead,
        'feedback': feedback,
        'corporate': corporate
    })    

def marketResearch(request):

    lead = LeadService.objects.all()
    feedback = ClientsFeedback.objects.all()
    corporate = OurCorporateClient.objects.all()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        name = request.POST['name']
        phone = request.POST['phone']
        email_from = settings.EMAIL_HOST_USER


        contact = ContactWithItem(name=name, email=email, phone=phone, subject=subject, message=message)
        contact.save()

        try:
            send_mail(subject, message, email, [email_from], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('/')    
                
    return render(request, "marketResearch.html", context={
        'lead': lead,
        'feedback': feedback,
        'corporate': corporate
    })    


def realEstate(request):

    lead = LeadService.objects.all()
    feedback = ClientsFeedback.objects.all()
    corporate = OurCorporateClient.objects.all()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        name = request.POST['name']
        phone = request.POST['phone']
        email_from = settings.EMAIL_HOST_USER


        contact = ContactWithItem(name=name, email=email, phone=phone, subject=subject, message=message)
        contact.save()

        try:
            send_mail(subject, message, email, [email_from], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('/')    
                
    return render(request, "realEstate.html", context={
        'lead': lead,
        'feedback': feedback,
        'corporate': corporate
    })    

