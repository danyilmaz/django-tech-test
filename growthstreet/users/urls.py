from django.conf.urls import url
from growthstreet.users.views import RegisterNewUserView

urlpatterns = [
    url(r'^$', RegisterNewUserView.as_view()),
]
