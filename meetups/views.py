from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


from .models import Meetup, Participant
from .form import RegistrationForm, MeetupForm
# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    try:
        if request.method == 'GET':
            print("GET")
            registration_form = MeetupForm()
            return render(request, 'meetups/index.html', {
                'form': registration_form,
                'show_meetups': True,
                'meetups': meetups
            })

        else:

            registration_form = MeetupForm(request.POST)

            if registration_form.is_valid():
                registration_form.save()
                return render(request,'meetups/creation-success.html')
            else:
                print(registration_form.cleaned_data)
                title = registration_form.cleaned_data['title']
                slug = registration_form.cleaned_data['slug']
                organizer_email = registration_form.cleaned_data['organizer_email']
                date = registration_form.cleaned_data['date']
                description = registration_form.cleaned_data['description']
                image = registration_form.cleaned_data['image']
                location = registration_form.cleaned_data['location']
                participants = registration_form.cleaned_data['title']
                
                # print(title)
                # print(slug)
                # print(organizer_email)
                # print(date)
                # print(description)
                # #print(image)
                # print(location)
                # print(participants)
                
                messages.error(request, "Error")

        return render(request, 'meetups/index.html', {
            'form': registration_form,
            'show_meetups': True,
            'meetups': meetups
        })

    except Exception as exc:
        print(exc)
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

