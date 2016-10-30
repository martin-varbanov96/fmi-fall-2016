from django.contrib import admin
from django.conf.urls import url, include
from home.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^admin/', admin.site.urls),
]