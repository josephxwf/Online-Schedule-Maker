from __future__ import unicode_literals

from django.db import models

# Create your models here.
class notification(models.Model):
    textbox = models.TextField()
    pub_date = models.DateTimeField('published_date',auto_now_add=True)

    def __unicode__(self):
        return self.textbox + '\n' +"(PostDate: " + str(self.pub_date) + ")"
'''
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
'''
