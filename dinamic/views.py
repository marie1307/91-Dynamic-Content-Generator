from django.shortcuts import render
from django.http import HttpResponse


def main(request, name):
    return render(request,'dinamic/content.html', {'name': name})

