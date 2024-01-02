from django.db import models
from django.contrib import auth
from PIL import Image
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    GenreType = (
        ('HORROR', 'horror'),
        ('COMEDY', 'comedy'),
        ('ROMANCE', 'romance'),
        ('ACTION', 'action'),
        ('SCI-FI', 'sci-fi'),
        ('SCIENCE', 'science')
    )

    title = models.CharField(max_length=70)
    pub_date = models.DateField()
    isbn = models.CharField(max_length=20, unique=True)
    author = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    genre = models.CharField(verbose_name='genre of this book', choices=GenreType, max_length=20)
    contributors = models.CharField(max_length=70)
    image = models.ImageField(default='no_image.JPEG', upload_to='book_images', null=True, blank=True)
    pdf_file = models.FileField(upload_to='book_pdfs', null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.title, self.isbn)

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'id': self.id})



class Chapter(models.Model):
    book = models.ForeignKey(Book, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    pdf_file = models.FileField(upload_to='chapters_pdfs', null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} - Chapter {self.title}"


class Review(models.Model):
    rating_choices = (
        ('1', 'One Star'),
        ('2', 'Two Stars'),
        ('3', 'Three Stars'),
        ('4', 'Four Stars'),
        ('5', 'Five Stars'),
    )
    comment = models.CharField(max_length=255)
    ratings = models.CharField(choices=rating_choices, max_length=4, default="1")
    date_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.comment
