from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact

def index(request):

    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context=context
    )


def contact(request, contact_id):

    #single_contact = Contact.objects.get(pk=contact_id)
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True)
    
    contact_name = f'{single_contact.first_name} {single_contact.last_name} -'

    context = {
        'contact': single_contact,
        'site_title': contact_name
    }

    return render(
        request,
        'contact/contact.html',
        context=context
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == "":
        return redirect('contact:index')
    
    print(search_value)

    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]
    

    context = {
        'contacts': contacts,
        'site_title': 'Search - '
    }

    return render(
        request,
        'contact/index.html',
        context=context
    )