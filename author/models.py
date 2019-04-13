from django.db import models

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=30, blank=False)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=30, blank=False)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Book(models.Model):
    
    name = models.CharField(max_length=30, blank=False)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name
