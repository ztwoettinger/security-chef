from ..models import Job
from django.forms import ModelForm

class InputForm(ModelForm):
    class Meta:
        model = Job
        fields = ['repo_url']