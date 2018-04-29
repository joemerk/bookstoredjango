#adapted from https://github.com/guinslym/django-by-example-book
from django.db import models
from django.core.urlresolvers import reverse

class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length=30, db_index = True)

    def __str__(self):
        return '%s' % (self.manufacturer_name)

class ModelNo(models.Model):
    modelno = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, db_index = True, unique = True)

    class Meta:
        ordering = ('modelno',)
        verbose_name = 'modelno'
        verbose_name_plural = 'modelnos'

    def __str__(self):
		return self.modelno

    def get_absolute_url(self):
        return reverse('headphones:headphone_list_by_modelno', args=[self.slug])

class Headphone(models.Model):
    modelno = models.ForeignKey(ModelNo, related_name='headphones')
    name = models.CharField(max_length = 100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    manufacturers = models.ForeignKey(Manufacturer)
    image = models.ImageField(upload_to='headphones/headphones_img', blank=True)
    description = models.TextField(blank = True, null = True)
    release_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('-release_date',)
        index_together = (('id', 'slug'),)

    def __str__(self):
    	return self.name

    def get_absolute_url(self):
        return reverse('headphones:headphone_detail', args=[self.id, self.slug])