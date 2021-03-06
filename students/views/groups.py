# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import UpdateView, CreateView, DeleteView

from ..models.groups import Group

# Group delete class
class GroupDeleteView(DeleteView):
     model = Group
     template_name = 'students/group_confirm_delete.html'

     def get_success_url(self):
         messages.success(self.request, u'Студента успішно видалено!')
         return reverse('home')


def groups_list(request):
    groups = Group.objects.all()
    # try to order group list
    order_by = request.GET.get('order_by', '')
    if order_by in ('', 'leader', 'id'):
        if order_by == '':
            groups = groups.order_by('leader')
        else:
            groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    try:
        num_page = int(request.GET.get('num'))
    except TypeError:
        num_page = 8

    if request.is_ajax():
        return render(request, 'students/groups_list.html', {"groups": groups[num_page: num_page + 1]})
    else:
        return render(request, 'students/groups_list.html', {"groups": groups[:num_page]})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)