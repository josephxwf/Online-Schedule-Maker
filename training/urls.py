from django.conf.urls import include, url
from django.contrib import admin
import mtaapp.views
admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', 'training.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', mtaapp.views.index, name='index'),
    url(r'^account/', include('mtaapp.urls', namespace="mtaapp")),

    #url(r'^hello/calendar/$', hello.views.calendar,name = "test2"),

    #url(r'^db', app.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]


"""
django gives you the option to name your views in case you need to refer to them from your code, or your templates. This is useful and good practice because you avoid hardcoding urls on your code or inside your templates. Even if you change the actual url, you don't have to change anything else, since you will refer to them by name.
for example:

in urls.py:
urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),

    url(r'^(?i)calendar/$', views.calendar, name='trainingCalendar'),

)


in views.py:

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def myview(request):
    passwords_url = reverse('trainingCalendar')  # this returns the string `/calendar/`
    return HttpResponseRedirect(passwords_url)
More here.


in templates:

<p>Please go <a href="{% url 'hello:trainingCalendar' %}">here</a></p>
"""
