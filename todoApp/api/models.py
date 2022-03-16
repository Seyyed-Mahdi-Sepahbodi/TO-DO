from django.db import models

# Create your models here.

class Task(models.Model):

    HIGH = 'HIG'
    MEDIUM = 'MED'
    LOW = 'LOW'
    TASK_PRIORITY_CHOICES = [
        (HIGH, 'بالا'),
        (MEDIUM, 'متوسط'),
        (LOW, 'پایین'),
    ]

    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    category = models.ForeignKey('api.Category', on_delete=models.PROTECT, verbose_name='دسته بندی')
    priority = models.CharField(max_length=3, choices=TASK_PRIORITY_CHOICES, default=MEDIUM, verbose_name='الویت')
    completed = models.BooleanField(default=False, verbose_name='تکمیل شده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'کار'
        verbose_name_plural = 'کار‌ها'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    parent = models.ForeignKey('self', name='child', on_delete=models.CASCADE, null=True, blank=True, verbose_name='دسته بندی پدر')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural = 'دسته بندیها'

    def __str__(self):
        return self.title
