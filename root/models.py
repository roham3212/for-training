from django.db import models

class Services(models.Model):
    title = models.CharField(max_length= 15)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)
    statues = models.BooleanField(default=False)


    def __str__(self):
        return self.title
