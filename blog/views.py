from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Free
from .models import Paid


# Create your views here.
def index(request):
    created_at_free = Free.objects.order_by('-created_at')[:10]
    created_at_paid = Paid.objects.order_by('-created_at')[:10]
    template = loader.get_template('index.html')
    context = {
        'nav_free': 'Free Intros',
        'nav_paid': 'Paid intros',
        'href_free': 'free',
        'href_paid': 'paid',
        'title': '6Frame',
        'cont_free': created_at_free,
        'cont_paid' : created_at_paid,
    }

    return HttpResponse(template.render(context, request))

def free_all(request):
    created_at_free = Free.objects.order_by('-created_at')
    template = loader.get_template('free_all.html')
    context = {
        'title': 'Free Intros',
        'cont_free': created_at_free,
    }

    return HttpResponse(template.render(context, request))

def paid_all(request):
    created_at_paid = Paid.objects.order_by('-created_at')
    template = loader.get_template('paid_all.html')
    context = {
        'title': 'Paid Intros',
         'cont_paid' : created_at_paid,
    }

    return HttpResponse(template.render(context, request))

def show_free(request, id):
    object_free = Free.objects.get(id=id)
    template = loader.get_template('show_free.html')
    context = {
        'title': 'Free Intros',
        'show_free' : object_free,
    }

    return HttpResponse(template.render(context, request))

def show_paid(request, id):
    get_url_paid = Paid.objects.get(id=id)
    template = loader.get_template('show_paid.html')
    context = {
        'title': 'Paid Intros',
        'cont_show_paid': get_url_paid,
    }

    return HttpResponse(template.render(context, request))
