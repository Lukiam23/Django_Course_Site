from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import Meetup, Participant
from .form import RegistrationForm, MeetupForm
# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    print("antes do try")
    try:
        if request.method == 'GET':
            print("Fez um GET")
            registration_form = MeetupForm()
            return render(request, 'meetups/index.html', {
                'form': registration_form,
                'show_meetups': True,
                'meetups': meetups
            })

        else:
            print("fez um POST")
            registration_form = MeetupForm(request.POST)
            print(registration_form)
            print("Antes da validação")
            if registration_form.is_valid():
                print("Era valida")
                registration_form.save()
                return render(request,'meetups/creation-success.html')
            print("Não entrou no except")

        return render(request, 'meetups/index.html', {
            'form': registration_form,
            'show_meetups': True,
            'meetups': meetups
        })

    except Exception as exc:
        return render(request, 'meetups/index.html', {
            'show_meetups': True,
            'meetups': meetups
            })

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email = user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request,'meetups/meetup-details.html',{
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form
            })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
            })

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request,'meetups/registration-success.html', {
        'organizer_email': meetup.organizer_email
        } )

