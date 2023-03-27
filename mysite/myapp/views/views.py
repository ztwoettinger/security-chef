from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def submit_repo_for_scan(request):
    test_message = "I'm doing it yay!"
    return render(request, 'security_chef.html', {'message': test_message})