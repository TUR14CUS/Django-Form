from django.shortcuts import render
from .forms import ContactForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                date=date,
                occupation=occupation
            )

            message_body = f"A new form has been submitted:\n\nFirst Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nPhone: {phone}\nDate: {date}\nOccupation: {occupation}"
            email_message = EmailMessage(
                subject="Form Submission Confirmation",
                body=message_body,
                from_email=[email]
            )
            email_message.send()
            messages.success(request, "Form submission successful")

    return render(request, "index.html")
