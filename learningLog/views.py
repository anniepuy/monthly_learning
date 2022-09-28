from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

learning_logs = {
    "january" : "Learned Bootstrap with NuCamp Coding Bootcamp",
    "february" : "Learned React with NuCamp Coding Bootcamp",
    "march" : "Continued to learn React with NuCamp Coding Bootcamp",
    "april" : "Learned React Native with NuCamp Coding Bootcamp",
    "may" : "Continued to learn React Native with NuCamp Coding Bootcamp",
    "june" : "Studied and passed Comptia Security +",
    "july" : "Learned Python with NuCamp Coding Bootcamp",
    "august" : "Learned Sql and Python with NuCamp Coding Bootcamp",
    "september" : "Learned DevOps and CI/CD with NuCamp Coding Bootcamp",
    "october" : "Projected to complete the Linux Foundation's DevOps Bootcamp",
    "november" : "Projected to complete the Linux Foundations Cloud Engineering Bootcamp",
    "december" : "Projected to head back to React and Node.js to strengthen full stack skills."
}


# Create your views here.

def monthly_learning_by_number(request, month):
    months = list(learning_logs.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    forward_month = months[month - 1]
    forward_path = reverse("monthly-learning", args=[forward_month])
    return HttpResponseRedirect(forward_path)

def monthly_learning(request, month):
    try:
        learning_text = learning_logs[month]
        return HttpResponse(learning_text)
    except:
        return HttpResponseNotFound("Is there another month?  Amazing, I must have slept through it. Sorry, not found.")
    

