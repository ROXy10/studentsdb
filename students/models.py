# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    """Student Model"""

    class Meta(object):
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенти"

    first_name = models.CharField(max_length=256, blank=False, verbose_name=u"Ім'я")
    last_name = models.CharField(max_length=256, blank=False, verbose_name=u"Прізвище")
    middle_name = models.CharField(max_length=256, blank=False, verbose_name=u"По-батькові")
    birthday = models.DateField(blank=False, verbose_name=u"Дата народження", null=True)
    photo = models.ImageField(blank=True, verbose_name=u"Дото", null=True)
    ticket = models.CharField(max_length=256, blank=True, verbose_name=u"Білет")
    notes = models.TextField(blank=True, verbose_name=u"Додаткові нотатки")


    def __unicode__(self):
        return u"%s %s" %(self.last_name, self.first_name)