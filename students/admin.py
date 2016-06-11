from django.contrib import admin
from .models.groups import Group
from .models.students import Student
from .models.journal import Journal
from .models.exams import Exam

# Register your model here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Journal)
admin.site.register(Exam)
