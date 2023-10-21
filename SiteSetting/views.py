from django.shortcuts import render, redirect
from ContactUs.forms import MessageForm


# Create your views here.


def home(request):
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
    }

    return render(request, 'SiteSetting/home.html', context)


def about_us(request):
    context = {
        'page': about_us,
    }

    return render(request, 'SiteSetting/about_us.html', context)


def our_services(request):
    context = {
        'page': our_services,
    }

    return render(request, 'SiteSetting/our_services.html', context)
