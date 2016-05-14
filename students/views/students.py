# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404

from ..models import Student

# Views for Students


def students_list(request):
    students = Student.objects.all()
    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('', 'first_name', 'ticket', 'id'):
        if order_by == '':
            students = students.order_by('last_name')
        else:
            students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    return render(request, 'students/students_list.html', {"students": students})


def students_add(request):
    return render(request, 'students/student_form.html', {})


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(reuest, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


