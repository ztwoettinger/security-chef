from django.shortcuts import render
from django.http import HttpResponse
from time import sleep

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def sample_function_add_two_numbers(x, y):
    result = x + y
    return result

def sample_function_add_two_numbers_then_triple_it(x, y):
    sum = sample_function_add_two_numbers(x, y)
    result = sum * 3
    return result