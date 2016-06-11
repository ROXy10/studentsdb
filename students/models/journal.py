# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Journal(models.Model):
    """Journal Model"""

    class Meta(object):
        verbose_name = u"Відвідування"
        verbose_name_plural = u"Відвідування"

    student_name = models.OneToOneField('Student', verbose_name=u"Студент", blank=False, null=True)
    visiting = models.IntegerField(verbose_name=u"Відвідування", blank=True, null=True)

    def __unicode__(self):
        return u"%s %s" %(self.student_name.last_name, self.student_name.first_name)