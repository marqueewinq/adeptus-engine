from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import views as auth_views, logout
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
import logging
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, ModelFormMixin
from django.contrib.auth import urls

from .models import *

logger = logging.getLogger('app')

@login_required(login_url = '/login/')
def index(request):
    logger.info('hit index')
    return redirect(reverse('feed'))

def login(request):
    template = 'app/login.html'
    return auth_views.login(request, template_name = template, extra_context = {"next": reverse('app:profile')})

@login_required(login_url = '/login/')
def profile(request):
    context = {
        "player": get_object_or_404(Account, id = request.user.account.id), 
        "player_characters": Character.objects.filter(account__id = request.user.account.id)
        }
    template = 'app/profile.html'
    return render(request, template, context)

@login_required(login_url = '/login/')
def feed(request, char_id):
    char = get_object_or_404(Character, id = char_id)
    context = {
        "character": char, 
        "factions": char.faction.all()
        }
    template = 'app/feed.html'
    return render(request, template, context)


@login_required(login_url = '/login/')
def shipslookup(request):
    context = {
        "ships": Ship.objects.all()
        }
    template = 'app/ship.html'
    return render(request, template, context)



