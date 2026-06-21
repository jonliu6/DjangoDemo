from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenge_dictionary = {
    "january":"run a marathon",
    "february":"play cricket",
    "march":"eat vegan food",
    "april":"read a book",
    "may":"draw a picture",
    "june":"listen to music",
    "july":"study a new language",
    "august":"workout",
    "september":"watch a movie",
    "october":"learn to dance",
    "november":"volunteer at a shelter",
    "december":"reflect on the year"
}

# Create your views here.
def index(request):
    list_items = ""
    months = list(challenge_dictionary.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly_challenges", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def number_challenge(request, month):
    months = list(challenge_dictionary.keys())
    if month > len(months):
        return HttpResponseNotFound("This month is not supported")
    redirect_month = months[month-1]
    redirection_path = reverse("monthly_challenges", args=[redirect_month])
    return HttpResponseRedirect(redirection_path)

def challenge(request, month):
    # return HttpResponse(f"{month} challenge!")
    try:
        challenge_text = challenge_dictionary[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<span style='color: red;'>This month is not supported</span>")