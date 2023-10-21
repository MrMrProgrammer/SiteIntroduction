from django.shortcuts import render, redirect
from django.views import View

from .forms import MessageForm


# Create your views here.


def get_message(request):

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MessageForm()

    return render(request, 'SiteSetting/home.html', {'form': form})
