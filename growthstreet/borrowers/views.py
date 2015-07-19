from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from growthstreet.borrowers.forms import BorrowerForm, CompanyForm
from growthstreet.users.services import UserService
from growthstreet.borrowers.services import BorrowerService, CompanyService


class NewBorrowerView(FormView):
    template_name = 'borrowers/borrower.html'
    form_class = BorrowerForm

    def dispatch(self, request, *args, **kwargs):
        self.user = self.kwargs['user_pk']
        return super(NewBorrowerView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = UserService().get_user(self.user)
        phonenumber = form.cleaned_data['phonenumber']
        borrow_amount = form.cleaned_data['borrow_amount']
        loan_days = form.cleaned_data['loan_days']
        loan_reason = form.cleaned_data['loan_reason']
        BorrowerService().create_new_borrower(phonenumber, borrow_amount,
                                              loan_days, loan_reason, user)
        return HttpResponseRedirect(reverse('borrowers:company', args=[self.user]))


class CompanyInfoView(FormView):
    template_name = 'borrowers/company.html'
    form_class = CompanyForm

    def dispatch(self, request, *args, **kwargs):
        self.user = self.kwargs['user_pk']
        return super(CompanyInfoView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        name = form.cleaned_data['name']
        address = form.cleaned_data['address']
        registered_number = form.cleaned_data['registered_number']
        sector = form.cleaned_data['sector']
        CompanyService().create_new_company(name, address, registered_number,
                                            sector, self.user)
        return HttpResponseRedirect(reverse('borrowers:success'))
