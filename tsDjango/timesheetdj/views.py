from django.shortcuts import render

# Create your views here.

def activitate_list(request):
    return render(request, 'activitate/activitate_list.html', {})