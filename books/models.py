#adapted from https://github.com/guinslym/django-by-example-book
from django.db import models
from django.core.urlresolvers import reverse

class Author(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length=30, db_index = True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Genre(models.Model):
    genre = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, db_index = True, unique = True)

    class Meta:
        ordering = ('genre',)
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
		return self.genre

    def get_absolute_url(self):
        return reverse('books:book_list_by_genre', args=[self.slug])

class Book(models.Model):
    genre = models.ForeignKey(Genre, related_name='books')
    title = models.CharField(max_length = 100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    authors = models.ForeignKey(Author)
    image = models.ImageField(upload_to='books/', blank=True)
    description = models.TextField(blank = True, null = True)
    publication_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('-publication_date',)
        index_together = (('id', 'slug'),)

    def __str__(self):
    	return self.title

    def get_absolute_url(self):
        return reverse('books:book_detail', args=[self.id, self.slug])