# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    # paginate students
    #paginator = Paginator(students, 3)
    #page = request.GET.get('page')
    #try:
    #    students = paginator.page(page)
    #except PageNotAnInteger:
    #    # If page is not an integer, deliver first page.
    #    students = paginator.page(1)
    #except EmptyPage:
    #    # If page is out of range (e.g. 9999), deliver
    #    # last page of results.
    #    students = paginator.page(paginator.num_pages)
    try:
        num_page = int(request.GET.get('num'))
    except TypeError:
        num_page = 8

    if request.is_ajax():
        return render(request, 'students/students_list.html', {"students": students[num_page: num_page+1]})
    else:
        return render(request, 'students/students_list.html', {"students": students[:num_page]})






def students_add(request):
    return render(request, 'students/student_form.html', {})


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(reuest, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


