# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from ..models.exams import Exam

# Views for Students


def exams_list(request):
    exams = Exam.objects.all()
    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('', 'subject', 'teacher', 'group', 'id'):
        if order_by == '':
            exams = exams.order_by('date')
        else:
            exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()

    try:
        num_page = int(request.GET.get('num'))
    except TypeError:
        num_page = 8

    if request.is_ajax():
        return render(request, 'students/exams_list.html', {"exams": exams[num_page: num_page+1]})
    else:
        return render(request, 'students/exams_list.html', {"exams": exams[:num_page]})






def exams_add(request):
    return render(request, 'students/exam_form.html', {})


def exams_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def exams_delete(reuest, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


