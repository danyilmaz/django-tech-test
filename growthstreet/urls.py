from django.conf.urls import include, url
from django.contrib import admin

from growthstreet.users.urls import urlpatterns as user_urls
from growthstreet.borrowers.urls import urlpatterns as borrower_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^borrower/', include(borrower_urls, namespace='borrowers')),
    url(r'^$', include(user_urls))
]
