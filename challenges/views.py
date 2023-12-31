from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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
    "december": None

}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months" : months
    })

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
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "month_name" : month,
        })
    except:
        raise Http404()