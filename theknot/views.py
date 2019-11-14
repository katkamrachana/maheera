import json
from django.shortcuts import render
from django.core.mail import send_mail
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from theknot.forms import GuestForm
from maheera.settings import RECIPIENT_EMAIL, DEFAULT_FROM_EMAIL, DEFAULT_TO_EMAIL

def index(request, block_rsvp=False):
    
    # check if Guest object exists with the same IP 
    context_variables = {}
    if not block_rsvp:
        form = GuestForm({'attending_wedding': 1, 'attending_reception': 1})
        context_variables = {'form': form}
    return render(request, 'index.html', context_variables) 

def get_ip(request):
    ip = None
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def write_ip(ip_val):
    pass

def save_rsvp(request):
    try:
        print(request)
        if request.method == "POST":
            form = GuestForm(request.POST)
            if form.is_valid():
                subject = "RSVP from :" + form.cleaned_data['first_name'] +\
                " " + form.cleaned_data['last_name'] 
                message = form.cleaned_data['message']
                sender = form.cleaned_data['email']
                guest = form.save(commit=False)
                is_attending = True if form.cleaned_data['attending_reception']== "1" or \
                                form.cleaned_data['attending_wedding']== "1"  else False
                # ip_address = get_ip(request)
                guest.ip_address = None
                guest.submission_timestamp = timezone.now()
                form.save()
                # write_ip(ip_address)

                # send_mail(subject, message, DEFAULT_FROM_EMAIL, [sender, DEFAULT_TO_EMAIL])
                return HttpResponse(json.dumps({'success': True, 'is_attending': is_attending}), content_type='application/json') 
            else:
                return HttpResponse(json.dumps(form.errors.as_json()), status=500,  content_type='application/json') 
    except Exception as e:
        print(e)
        return reverse('index') 
