from django.conf.urls import url
from django.views.generic import TemplateView
from growthstreet.borrowers.views import NewBorrowerView, CompanyInfoView

urlpatterns = [
    url(r'^(?P<user_pk>\d+)/$', NewBorrowerView.as_view(), name='borrower'),
    url(r'^company_info/(?P<user_pk>\d+)/', CompanyInfoView.as_view(), name='company'),
    url(r'^thanks$', TemplateView.as_view(template_name='borrowers/success.html'), name='success')
]
