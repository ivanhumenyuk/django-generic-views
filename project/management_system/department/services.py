from .forms import *
from .models import Department
from django.shortcuts import reverse, get_object_or_404


def get_success_url(self, url):
    return reverse(url)