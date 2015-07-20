from django import forms

from phonenumber_field.formfields import PhoneNumberField

from growthstreet.borrowers.models import Borrower, Company


class BorrowerForm(forms.ModelForm):
    phonenumber = PhoneNumberField(label='Phone number')

    class Meta:
        model = Borrower
        fields = ['borrow_amount', 'loan_days', 'loan_reason']

    def clean_borrow_amount(self):
        amount = self.cleaned_data['borrow_amount']
        if int(amount) < 10000:
            self.add_error('borrow_amount', 'Too low')

        if int(amount) > 100000:
            self.add_error('borrow_amount', 'Too high')
        return amount


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'registered_number', 'sector']
        widgets = {
            'registered_number': forms.TextInput(attrs={'type': 'number',
                                                        })
        }
