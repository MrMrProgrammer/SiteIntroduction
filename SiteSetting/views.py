from django.shortcuts import render, redirect
from ContactUs.forms import MessageForm
from .models import SiteSetting, HomeDetails, AboutUsDetails, OurServicesDetails, SliderImage


def home(request):
    site_setting: SiteSetting = SiteSetting.objects.filter(is_active=True).last()
    home_setting: HomeDetails = HomeDetails.objects.filter(is_active=True).last()
    slider_images: SliderImage = SliderImage.objects.filter(is_active=True).all()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MessageForm()

    context = {
        'form': form,
        'page': home,
        'site_setting': site_setting,
        'home_setting': home_setting,
        'slider_images': slider_images,
    }

    return render(request, 'SiteSetting/home.html', context)


def about_us(request):
    site_setting: SiteSetting = SiteSetting.objects.filter(is_active=True).last()
    about_us_setting: AboutUsDetails = AboutUsDetails.objects.filter(is_active=True).last()
    slider_images: SliderImage = SliderImage.objects.filter(is_active=True).all()

    context = {
        'page': about_us,
        'site_setting': site_setting,
        'about_us_setting': about_us_setting,
        'slider_images': slider_images,

    }

    return render(request, 'SiteSetting/about_us.html', context)


def our_services(request):
    site_setting: SiteSetting = SiteSetting.objects.filter(is_active=True).last()
    our_services_setting: OurServicesDetails = OurServicesDetails.objects.filter(is_active=True).last()
    slider_images: SliderImage = SliderImage.objects.filter(is_active=True).all()

    context = {
        'page': our_services,
        'site_setting': site_setting,
        'our_services_setting': our_services_setting,
        'slider_images': slider_images,

    }

    return render(request, 'SiteSetting/our_services.html', context)
