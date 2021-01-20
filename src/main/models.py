from django.db import models
from django.urls import reverse

class task(models.Model):
    task_text = models.TextField()
    user = models.EmailField(max_length=245, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_text}"
    
    def get_absolute_url(self):
        return reverse('main:notes', kwargs={'email' :self.email})
