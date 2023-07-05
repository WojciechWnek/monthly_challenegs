from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
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

def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())

  if (month > len(months)):
    return HttpResponseNotFound("Invalid month")
  redirect_month = months[month - 1]
  redirect_path = reverse("month-challenge", args=[redirect_month])
  return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
  try:
    month_challenge = monthly_challenges[month]
    return HttpResponse(month_challenge)
  except:
    return HttpResponseNotFound("This month is not supported")
