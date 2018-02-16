from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',include('mainPage.urls')),
    url(r'^aboutUs',include('aboutUs.urls')),
    url(r'^start',include('game.urls'))
]
