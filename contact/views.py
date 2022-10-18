from django.shortcuts import render, redirect
from .forms import ContactForm, ApplyForm


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/contact/')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def apply(request):
    form = ApplyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/apply/')
    context = {
        'form': form
    }
    return render(request, 'courses/apply.html', context)
