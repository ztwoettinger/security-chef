# Go to the site
# Submit a git repo url with commit hash
# If the sbom stuff completed with no problem, save a status True in the database
# If it did have a problem, save with a status of False

from .forms import InputForm
from django.shortcuts import render, redirect

def user_input(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/app")
    else:
        form = InputForm()
    return render(request, 'submit_repo.html', {"form": form})