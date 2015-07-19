from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from growthstreet.users.forms import UserForm
from growthstreet.users.services import UserService


class RegisterNewUserView(FormView):
    form_class = UserForm
    template_name = 'users/registration.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = UserService().create_new_user(username, email, password)
        return HttpResponseRedirect(reverse('borrowers:borrower', args=[user.pk]))
