from django.db import models

# Create your models here.


class Tracking(models.Model):
    add_date = models.DateTimeField(auto_now_add=True)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    note = models.CharField(max_length=100)

    def _str_(self):
        return self.first_name+" "+self.last_name

