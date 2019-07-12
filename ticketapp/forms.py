from django import forms
from .models import Ticket

#Form used to create new ticket and store values in database
class TicketForm(forms.ModelForm):

    class Meta:
        model=Ticket
        fields=['ticket',]

#Form used to update existing ticket and store values in database
class AmendForm(forms.Form):
    amendValue=forms.CharField(label='Amend Ticket')