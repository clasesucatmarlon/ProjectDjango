from django.db import models

# Create your models here.
class ManageUserModels(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField(max_length=200)
    company = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class meta:
    ordering = ["-created"] # order by last created

    def __str__(self):
        return self.first_name
