from django.db import models

class Users(models.Model):
    verbose_name = "user"
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=245)
    password = models.CharField(max_length=40)
    terms_condition = models.BooleanField("I agree to terms and conditions", default=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

