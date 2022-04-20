from django.contrib import admin
from .models import ServiceItem, ServicePrice, ClientsFeedback, OurCorporateClient, StrategicWork, Category, TermsAndConditions, PrivacyAndPolicy, RefundPolicy
# Register your models here.

admin.site.register(ServiceItem)
admin.site.register(ServicePrice)
admin.site.register(StrategicWork)
admin.site.register(Category)
admin.site.register(TermsAndConditions)
admin.site.register(PrivacyAndPolicy)
admin.site.register(RefundPolicy)
admin.site.register(ClientsFeedback)
admin.site.register(OurCorporateClient)
# OurCorporateClient