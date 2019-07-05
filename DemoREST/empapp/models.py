from django.db import models


class Emp(models.Model):
    f_name = models.CharField(max_length=10)
    l_name = models.CharField(max_length=10)
    contact = models.IntegerField()
    email = models.EmailField(max_length=30)

    def _str__(self):
        return self.f_name
