from django.shortcuts import render
from django.utils import timezone
from .models import Course

def group_list(request):
    groups = Course.objects.filter()
    return render(request, 'matcher/group_list.html', {})
