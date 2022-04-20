from django.contrib import admin
from .models import (Contact, ContactWithItem, About, AboutPromoTitle,
                     AboutPromoLeftItem, AboutPromoRightItem, AboutPromoBanner,
                      AboutTeam, BlogCategory, Blog)
# Register your models here.

admin.site.register(Contact)
admin.site.register(ContactWithItem)
admin.site.register(About)
admin.site.register(AboutPromoTitle)
admin.site.register(AboutPromoLeftItem)
admin.site.register(AboutPromoRightItem)
admin.site.register(AboutPromoBanner)
admin.site.register(AboutTeam)
admin.site.register(BlogCategory)
admin.site.register(Blog)
