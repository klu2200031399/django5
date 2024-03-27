import csv
import random
import string
import datetime
import matplotlib.pyplot as plt
import requests
import numpy as np
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.checks import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import IntegerDateForm, PieChartForm
from .models import FeedBack
from django.db.models import Count


def hello(request):
    return HttpResponse("<center>Welcome to TTM HomePage</center>")


def NewHomePage(request):
    return render(request, 'NewHomePage.html')


def Travel(request):
    return render(request, 'Travel.html')


def print1(request):
    return render(request, 'console.html')


def print_to_console(request):
    user_input = ''  # Initialize user_input for the case of a GET request
    if request.method == "POST":
        user_input = request.POST.get('user_input', '')  # Use get() to avoid UnboundLocalError
        print(f"User Input: {user_input}")
        # return HttpResponse('Form submitted successfully')
    a1 = {'user_input': user_input}
    return render(request, 'print_to_console.html', a1)


def randomcall(request):
    return render(request, 'randomlogic.html')


import random
from string import ascii_letters
from django.shortcuts import render

def randomcall1(request):
    ran1 = ''
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
        a2 = int(user_input)
        ran1 = ''.join(random.sample(ascii_letters, k=a2))

    a1 = {'ran1': ran1}
    return render(request, 'randomlogic.html', a1)


def getdate1(request):
    return render(request, 'TimeAndDate.html')


def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'get_date.html', {'updated_date': updated_date})
    else:
        form = IntegerDateForm()
    return render(request, 'get_date.html', {'form': form})





def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1 = {'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})


def car(request):
    return render(request, 'car.html')





def weatherpagecall(request):
    return render(request, 'weatherappinput.html')


def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = 'c69c467e89e4597f616d562c5334864e'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})


def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'NewHomePage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')

    else:
        return render(request,'login.html')

# Corrected imports
# Corrected imports
from django.contrib import auth, messages
from django.contrib.auth.models import User
# Other imports remain the same

# Your view functions remain unchanged

def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.success(request, 'Account created successfully!!')
                return render(request, 'login.html')
        else:
            messages.error(request, 'Passwords do not match')
    # Render the signup.html template in both cases
    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return render(request, 'NewHomePage.html')

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from .models import FeedBack

'''def Feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        feedback = request.POST.get("feedback")

        # Save feedback to the database
        obj = FeedBack.objects.create(name=name, email=email, feedback=feedback)

        # Send email notification
        subject = 'New Feedback Received'
        message = f'Hi, a new feedback has been submitted.\n\nName: {name}\nEmail: {email}\nFeedback: {feedback}'
        from_email = 'yogeendra7761@gmail.com'  # Replace with your email address
        to_email = email  # Replace with recipient's email address
        send_mail(subject, message, from_email, [to_email])

        return HttpResponse("<h1> Feedback has been submitted </h1>")

    return render(request, 'feedback.html')'''


def Feedback(request):
    if request.method =="POST":
        name=request.POST["name"]
        email=request.POST['email']
        feedback=request.POST["feedback"]
        obj=FeedBack(name=name,email=email,feedback=feedback )
        tosend = feedback + 'this is copy'

        obj.save()
        send_mail(
            'thank You',
            tosend,
            'yogeendra7761@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1> Feedback has been submitted </h1>")

    return render(request, 'feedback.html')
