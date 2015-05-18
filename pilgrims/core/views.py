from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse

from core.models import Conference

def home(request):

    conference = Conference.objects.filter(is_current=True).order_by('date_start').first()

    context = {'conference' : conference}

    return render(request, 'home.html', context)
