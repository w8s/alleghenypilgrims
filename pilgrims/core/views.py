from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse

from core.models import Conference
from core.forms import PilgrimUserForm

def home(request):

    conference = Conference.objects.filter(is_current=True).order_by('date_start').first()

    context = {'conference' : conference}

    return render(request, 'home.html', context)


@login_required
def user_settings(request):
    user = request.user
    if request.method == 'GET':
        form = PilgrimUserForm(data=request.POST, instance=user)
        context = {'form':form}
    else:
        # A POST request: Handle Form Upload
        form = PilgrimUserForm(data=request.POST, instance=request.user) # Bind data from request.POST into a PostForm
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            print "Valid User: %s" % request.user
            request.user = form.save(commit=False)
            request.user.save()
            return redirect('user_settings')
        else:
            return redirect('user_settings')

    return render(request, 'user/profile.html', context)
