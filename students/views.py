# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404

# Views for Students


def students_list(request):
    students = (
        {
            'id': 1,
            'first_name': u'Віталій',
            'last_name': u'Подоба',
            'ticket': 235,
            'image': 'img/img_1.jpg'
        },
        {
            'id': 2,
            'first_name': u'Андрій',
            'last_name': u'Корост',
            'ticket': 2123,
            'image': 'img/img_2.jpg'
        },
        {
            'id': 3,
            'first_name': u'Кулага',
            'last_name': u'Вадим',
            'ticket': 2133,
            'image': 'img/img_3.jpg'
        },
    )
    return render(request, 'students/students_list.html', {"students": students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(reuest, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


# Views for Groups


def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)