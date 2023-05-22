from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class RenewBookForm(forms.Form):
    renewal_date = forms.DateField()#(help_text="Enter a date between now and 4 weeks (default 3).")
    

    # renewal_date = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder':'YYYY-MM-DD',
    #     'type':'date',
        
        
        
    # }))

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if (data < datetime.datetime.today()):
            raise ValidationError (_('Invalid date - renewal is in past already'))
        
        # Check if a date is in the allowed range (+4 weeks from today).
        if(data > datetime.datetime.today() + datetime.timedelta(weeks=28)):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        
        return data
