from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime
import math


def home(request):
    return render(request, "base.html")