from django.db import models


# Create your models here.


class SiteSetting(models.Model):
    header_logo = models.ImageField(upload_to='header_logo')
    header_phone_umber = models.CharField(max_length=20)
    header_email = models.CharField(max_length=30)
    header_address = models.TextField()
    footer_license = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    favicon = models.ImageField(upload_to='thumbnail')

    class Meta:
        db_table = 'Site Settings'


class HomeDetails(models.Model):
    header1 = models.CharField(max_length=100, blank=True, null=True)
    body1 = models.TextField(blank=True, null=True)

    header2 = models.CharField(max_length=100, blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)

    header3 = models.CharField(max_length=100, blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Home Settings'

    def __str__(self):
        return self.header1


class AboutUsDetails(models.Model):
    header1 = models.CharField(max_length=100, blank=True, null=True)
    body1 = models.TextField(blank=True, null=True)

    header2 = models.CharField(max_length=100, blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)

    header3 = models.CharField(max_length=100, blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'About Us Settings'


class OurServicesDetails(models.Model):
    header1 = models.CharField(max_length=100, blank=True, null=True)
    body1 = models.TextField(blank=True, null=True)

    header2 = models.CharField(max_length=100, blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)

    header3 = models.CharField(max_length=100, blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Our Services Settings'


class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider')
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Slider Settings'
