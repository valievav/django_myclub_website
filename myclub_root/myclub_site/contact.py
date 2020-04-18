from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(required=False, label="Your Email")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


def contact(request):
    """
    Creates 'contact us form' and sends email
    """
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():             # uses else flow if invalid - re-renders form with error messages
            cd = form.cleaned_data      # normalizing data (e.g., standard date format)
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(cd['subject'],    # send email (printed to console to test
                      cd['message'],
                      cd.get('email', 'noreply@example.com'),
                      ['admin@gmail.com'],
                      connection=con)
            return HttpResponseRedirect('/contact?submitted=True')  # redirects to 'Thank you' page if submitted
    else:
        form = ContactForm()            # empty form
        if 'submitted' in request.GET:  # display 'Thank you page' if was submitted
            submitted = True

    return render(request, 'contact/contact.html', {'form': form,
                                                    'submitted': submitted})
