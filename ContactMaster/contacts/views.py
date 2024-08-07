# contacts/views.py

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Contact
from django.shortcuts import render
from.forms import ContactForm
from.models import Contact

def home(request):
    return render(request, 'contacts/home.html')

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/list_contacts.html', {'contacts': contacts})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact deleted successfully.')
        return redirect(reverse('list_contacts'))
    return render(request, 'contacts/confirm_delete.html', {'contact': contact})

def search_contacts(request):
    query = request.GET.get('query')
    contacts = Contact.objects.filter(name__icontains=query) if query else Contact.objects.all()
    return render(request, 'contacts/list_contacts.html', {'contacts': contacts})


