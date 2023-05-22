from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import BookInstance



# class IF(forms.ModelForm):
#     class Meta:
#         model = BookInstance
#         fields = ('due_back', )


class RenewBookForm(forms.ModelForm):

    def clean_due_back(self):
        data = self.cleaned_data['due_back']

        # Check if a date is not in the past.
        if (data < datetime.date.today()):
            raise ValidationError (_('Invalid date - renewal is in past already'))
        
        # Check if a date is in the allowed range (+4 weeks from today).
        if(data > (datetime.date.today() + datetime.timedelta(weeks=4))):
            print('-------data------', data)
            print("___-------_____------_______-------_____------_____------_____")
            print((datetime.date.today() + datetime.timedelta(weeks=4)))
            raise ValidationError(_(f'Invalid date - renewal can\'t be more than 4 weeks from today({datetime.date.today()}) '))
        
        return data
    
    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back':_('Renewal Date')}
        help_texts = {
            'due_back':_('Enter a date between now and 4 weeks (default 3).')
        }

        widgets = {
            'due_back': forms.DateInput(attrs={
                'type':'date',
                
            })
        }