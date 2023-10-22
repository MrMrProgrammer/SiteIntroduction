from django.contrib import admin

# Register your models here.


from django.contrib import admin
from . import models


# class showDay(admin.ModelAdmin):
#     list_display = ["__str__"]
#     list_filter = ["fields"]
#     list_editable = ["fields"]
#     list_filter = ["fields"]


admin.site.register(models.SiteSetting)
admin.site.register(models.HomeDetails)
admin.site.register(models.AboutUsDetails)
admin.site.register(models.OurServicesDetails)
admin.site.register(models.SliderImage)
