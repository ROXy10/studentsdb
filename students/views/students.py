# -*- coding: utf-8 -*-
from datetime import datetime
from PIL import Image

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import UpdateView, CreateView, DeleteView
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions, Div

from ..models.students import Student
from ..models.groups import Group


# Students delete class
class StudentDeleteView(DeleteView):
     model = Student
     template_name = 'students/students_confirm_delete.html'

     def get_success_url(self):
         messages.success(self.request, u'Студента успішно видалено!')
         return reverse('home')


# Students update cripsy form
class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name',
                  'last_name',
                  'middle_name',
                  'birthday',
                  'photo',
                  'ticket',
                  'student_group',
                  'notes',
                  ]

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # set form tag attributes
        if kwargs['instance'] is not None:
            self.helper.form_action = reverse('students_edit', kwargs={'pk': kwargs['instance'].id})
        else:
            self.helper.form_action = reverse('students_add')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-4 control-label'
        self.helper.field_class = 'col-sm-6'
        self.helper.layout.append(FormActions(
            Div('', css_class='col-sm-4'),
            Submit('add_button', u'Зберегти'),
            Submit('cancel_button', u'Скасувати'),
        ))


# Update students class
class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        messages.success(self.request, u'Студента успішно збережено!')
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.success(self.request, u'Редагування студента відмінено!')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


# Create students class
class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm
    success_url = 'home'

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button') is not None:
            messages.success(self.request, u'Додавання студента скасовано!')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(StudentCreateView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, u'Студента успішно додано!')
        return reverse('home')


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

    try:
        num_page = int(request.GET.get('num'))
    except TypeError:
        num_page = 8

    if request.is_ajax():
        return render(request, 'students/students_list.html', {"students": students[num_page: num_page+1]})
    else:
        return render(request, 'students/students_list.html', {"students": students[:num_page]})


def students_add(request):
    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # errors collection
            errors = {}
            # validate student data will go here
            data = {
                'middle_name': request.POST.get('middle_name'),
                'notes': request.POST.get('notes'),
            }
            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u"Введіть коректний формат дати (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер білета є обов'язковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                try:
                    Image.open(photo).verify()
                except:
                    errors['photo'] = u"Оберіть файл зображення"
                else:
                    if not photo.size < 2097152:
                        errors['photo'] = u"Оберіть файл розміром до 2МБ"
                    else:
                        data['photo'] = photo

            # save student
            if not errors:
                student = Student(**data)
                student.save()
                # redirect to students list
                messages.success(request, u'Студента %s %s успішно додано!' %(data['last_name'], data['first_name']))
                return HttpResponseRedirect(reverse('home'))
            else:
                # render form with errors and previous user input
                messages.success(request, u'Будь-ласка, виправте наступні помилки')
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                               'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            messages.success(request, u'Додавання студента скасовано!')
            return HttpResponseRedirect(reverse('home'))
    else:
        # initial from render
        return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})


#def students_edit(request, sid):
    # return render(request, 'students/students_edit.html', {})


def students_delete(reuest, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


