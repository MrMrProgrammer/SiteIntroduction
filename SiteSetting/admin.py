from django.contrib import admin
from . import models


class ShowSiteSetting(admin.ModelAdmin):
    list_display = ['header_phone_umber', 'header_email', 'header_address', 'footer_license', 'is_active']
    list_filter = ["is_active"]


class ShowHomeDetails(admin.ModelAdmin):
    list_display = ['is_active', 'header1', 'body1', 'header2', 'body2', 'header3', 'body3', ]
    list_filter = ["is_active"]


class ShowAboutUsDetails(admin.ModelAdmin):
    list_display = ['is_active', 'header1', 'body1', 'header2', 'body2', 'header3', 'body3', ]
    list_filter = ["is_active"]


class ShowOurServicesDetails(admin.ModelAdmin):
    list_display = ['is_active', 'header1', 'body1', 'header2', 'body2', 'header3', 'body3', ]
    list_filter = ["is_active"]


class ShowSliderImage(admin.ModelAdmin):
    list_display = ['__str__', 'is_active', 'image']
    list_filter = ["is_active"]


admin.site.register(models.SiteSetting, ShowSiteSetting)
admin.site.register(models.HomeDetails, ShowHomeDetails)
admin.site.register(models.AboutUsDetails, ShowAboutUsDetails)
admin.site.register(models.OurServicesDetails, ShowOurServicesDetails)
admin.site.register(models.SliderImage, ShowSliderImage)
