from django.db import models

# Create your models here.
class Card(models.Model):
    title=models.CharField(max_length=20)
    mean1=models.CharField(max_length=200)
    mean2=models.CharField(max_length=200)
    select=models.PositiveIntegerField()
    picture = models.ImageField(blank=True, upload_to="pictures/%Y/%m/%d")
    score1=models.IntegerField()
    score2=models.IntegerField()
    order=models.IntegerField()

    def __str__(self):
        return self.title

class Taro(models.Model):
    name=models.CharField(max_length=20)
    num=models.IntegerField()
    content=models.TextField()
    

    def __str__(self):
        return self.name