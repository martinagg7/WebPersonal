from django.db import models
# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #para ordenarlos seg se crean
        ordering=["-created"]
    def __str__(self):
        return self.title