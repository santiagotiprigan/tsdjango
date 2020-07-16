from django.shortcuts import render

# Create your views here.

def activitate_list(request):
    return render(request, 'timesheetdj/activitate_list.html', {})