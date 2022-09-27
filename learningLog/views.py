from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_learning(request, month):
    if month == "janauary":
        learning_text = "Learned Bootstrap with NuCamp Coding Bootcamp"
    elif month == "february":
        learning_text = "Learned React with NuCamp Coding Bootcamp"
    elif month == "march":
        learning_text = "Continued to learn React with NuCamp Coding Bootcamp"
    elif month == "april":
        learning_text = "Learned React Native with NuCamp Coding Bootcamp"
    elif month == "may":
        learning_text = "Continued to learn React Native with NuCamp Coding Bootcamp"
    elif month == "june":
        learning_text = "Studied and passed Comptia Security +"
    elif month == "july":
        learning_text = "Learned Python with NuCamp Coding Bootcamp"
    elif month == "august":
        learning_text = "Learned Sql and Python with NuCamp Coding Bootcamp"
    elif month == "september":
        learning_text = "Learned DevOps and CI/CD with NuCamp Coding Bootcamp"
    elif month == "october":
        learning_text = "Projected to complete the Linux Foundation's DevOps Bootcamp"
    elif month == "november":
        learning_text = "Projected to complete the Linux Foundations Cloud Engineering Bootcamp"
    elif month == "december":
        learning_text = "Projected to head back to React and Node.js to strengthen full stack skills."
    else:
        return HttpResponseNotFound("Is there another month?  Amazing, I must have slept through it. Sorry, not found.")
    return HttpResponse(learning_text)