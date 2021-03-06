# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    question_text=models.CharField(max_length=250)
    date_published=models.DateTimeField('Date Published')


class Choices(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=250)
    votes=models.IntegerField(default=0)

# Create your models here.
