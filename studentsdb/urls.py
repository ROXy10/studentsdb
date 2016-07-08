"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from students.views import students, groups, journal, exams, contact_admin
from .settings import DEBUG


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Students urls
    url(r'^$', students.students_list, name='home'),
    url(r'^students/add/$', students.StudentCreateView.as_view(), name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', students.StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students.students_delete, name='students_delete'),

    # Groups urls
    url(r'^groups/$', groups.groups_list, name='groups'),
    url(r'^groups/add/$', groups.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups.groups_delete, name='groups_delete'),

    # Journal URL
    url(r'^journal/$', journal.journal_list, name='journal'),

    # Exams urls
    url(r'^exams/$', exams.exams_list, name='exams'),
    url(r'^exams/add/$', exams.exams_add, name='exams_add'),
    url(r'^exams/(?P<sid>\d+)/edit/$', exams.exams_edit, name='exams_edit'),
    url(r'^exams/(?P<sid>\d+)/delete/$', exams.exams_delete, name='exams_delete'),

    # Contact Admin Form
    #url(r'^contact-admin/$', contact_admin.contact_admin, name='contact_admin'),

    # Contact Admin Form class
    url(r'^contact-admin/$', contact_admin.ContactView.as_view(), name='contact_admin'),
]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
