from django.db import models

class Task(models.Model):
    task = models.CharField('Name', max_length=50)
    title = models.TextField('Descriprion')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tasks'
        verbose_name_plural = 'task'

