# Go to the site
# Submit a git repo url with commit hash
# If the sbom stuff completed with no problem, save a status True in the database
# If it did have a problem, save with a status of False

from django.shortcuts import render, redirect

def render_new_page(request):
    return render(request, 'new_page.html')