from django.shortcuts import render

def group_list(request):
    return render(request, 'matcher/group_list.html', {})