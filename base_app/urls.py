from django.urls import path
from .views import (IndexTemplateView, AboutTemplateView, ServiceTemplateView,
 CasesTemplateView,BlogTemplateView, ContactTemplateView, SingelBlogPost,
  CategoryBaseWork, search, TermsConditionView,
   PrivacyAndPolicyView, RefundPolicyView, ServicePriceDetail, leadGeneration, realEstate, linkdinResearch, listBuilding, marketResearch)

urlpatterns = [
    path('', IndexTemplateView, name="index"),
    path('about', AboutTemplateView.as_view(), name="about"),
    path('service', ServiceTemplateView.as_view(), name="service"),
    path('cases', CasesTemplateView.as_view(), name="cases"),
    path('blog', BlogTemplateView.as_view(), name="blog"),
    path('contact', ContactTemplateView, name="contact"),
    path('post/<slug>', SingelBlogPost.as_view(), name="blog-singel"),
    path('service-page/<id>', CategoryBaseWork, name="service_item"),
    path('search', search, name="search"),
    path('terms-and-condition', TermsConditionView.as_view(), name="terms_condition_view"),
    path('privacy-and-policy', PrivacyAndPolicyView.as_view(), name="privacy_and_policy"),
    path('refound-policy', RefundPolicyView.as_view(), name="refound_policy"),
    path('order/<id>', ServicePriceDetail, name="order"),

    path('lead-generation', leadGeneration, name="leadGeneration"),
    path('linkdin-research', linkdinResearch, name="linkdinResearch"),
    path('list-building', listBuilding, name="listBuilding"),
    path('market-research', marketResearch, name="marketResearch"),
    path('real-estate', realEstate, name="realEstate"),
]
#   