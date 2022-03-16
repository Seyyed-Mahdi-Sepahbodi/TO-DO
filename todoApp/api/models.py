from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    completed = models.BooleanField(default=False, verbose_name='تکمیل شده')

    def __str__(self):
        return self.title
        