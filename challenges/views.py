from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
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


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")
    else:
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
 

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
