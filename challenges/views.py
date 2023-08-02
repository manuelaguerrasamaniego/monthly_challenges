from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

monthly_challenges = {
    "january":"Do things you used to love as a child!",
    "february":"Get out of your comfort zone!",
    "march":"Journal every day!",
    "april":"Exercise a little!",
    "may":"Go on a road trip!",
    "june":"Sign up for a class!",
    "july":"Pick up an instrument!",
    "august":"Visit someone you like!",
    "september":"Cook something new!",
    "october":"Visit a local attraction!",
    "november":"Teach yourself some sentences in a foreign language!",
    "december":"Make a diy project!"

}

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    challenge_text = monthly_challenge[month]
    try:
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
