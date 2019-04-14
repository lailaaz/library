from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from rest_framework.compat import MinValueValidator, MaxValueValidator


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
    category_id = models.ForeignKey(Category, blank=False)
    author_id =  models.ForeignKey(Author, blank=False)
    name = models.CharField(max_length=30, blank=False)
    price = models.FloatField(blank=False)
    author_percentage = models.IntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    description = models.TextField()

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=30, blank=False)
    employee = models.ForeignKey(User, blank=False)
    phone = models.CharField(max_length=11, blank=False)
    address = models.TextField()

    class Meta:
        db_table = 'branch'

    def __str__(self):
        return self.name

class BranchBookStock(models.Model):
    book_id = models.ForeignKey(Book, blank=False)
    branch_id = models.ForeignKey(Branch, blank=False)
    number_of_books = models.IntegerField(blank=False, default=1)
    nubmer_of_bought_books = models.IntegerField(blank=False, default=0)


    class Meta:
        db_table = 'branch_book_stock'


class Bill(models.Model):
    branch_id = models.ForeignKey(Branch, blank=False)
    total_price = models.FloatField(blank=False)
    created_at = models.DateTimeField(blank=False)

    class Meta:
        db_table = 'bill'


class Invoice(models.Model):
    book_id = models.ForeignKey(Book, blank=False)
    branch_id = models.ForeignKey(Branch, blank=False)
    bill_id = models.ForeignKey(Bill, blank=False)
    number_of_books = models.IntegerField(blank=False, default=1)
    price = models.FloatField(blank=False)
    created_at = models.DateTimeField(blank=False)

    class Meta:
        db_table = 'invoice'

