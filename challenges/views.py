from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

# def january(request):
#   return HttpResponse("Eat no meat")

# def february(request):
#   return HttpResponse("Walk for 20 min daily")

def monthly_challenge(request, month):
  month_challenge = None
  if month == "january":
    month_challenge="Eat no meat"
  elif month == "february":
    month_challenge="Walk 20 min"
  elif month == "march":
    month_challenge="Practice Django"
  else:
    return HttpResponseNotFound("This month is not supported")
  return HttpResponse(month_challenge)