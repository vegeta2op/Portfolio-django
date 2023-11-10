# views.py
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .forms import ContactForm

from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Modify the success message as needed
            return JsonResponse({'success': True, 'message': 'The message has been successfully sent.'})
        else:
            # Handle form errors
            return JsonResponse({'success': False, 'errors': form.errors})

    else:
        form = ContactForm()

    return render(request, "index.html", {'form': form})
