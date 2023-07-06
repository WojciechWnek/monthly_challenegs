from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

# def january(request):
#   return HttpResponse("Eat no meat")

# def february(request):
#   return HttpResponse("Walk for 20 min daily")
monthly_challenges = {
  "january": "Eat no meat",
  "february": "Walk 20 min",
  "march": "Practice Django",
  "april": "Eat no meat",
  "may": "Walk 20 min",
  "june": "Practice Django",
  "july": "Eat no meat",
  "august": "Walk 20 min",
  "september": "Practice Django",
  "october": "Eat no meat",
  "november": "Walk 20 min",
  "december": "Practice Django",
}

def index(request):
  list_items =""
  months = list(monthly_challenges.keys())

  for month in months:
    capitalized_month = month.capitalize()
    month_path= reverse("month-challenge", args=[month])
    list_items +=f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
  response_data = f"<ul>{list_items}</ul>"

  return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())

  if (month > len(months)):
    return HttpResponseNotFound("Invalid month")
  redirect_month = months[month - 1]
  redirect_path = reverse("month-challenge", args=[redirect_month])
  return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    response_data = render_to_string("challenges/challenge.html")
    return HttpResponse(response_data)
  except:
    return HttpResponseNotFound("<h1>This month is not supported</h1>")
