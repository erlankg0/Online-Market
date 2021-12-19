from django.db import models


class Category(models.Model):
    category_name = models.CharField(verbose_name='Category', max_length=100)
    slug = models.CharField(max_length=256, verbose_name='url', unique=True)
    description = models.TextField(max_length=255, verbose_name='Description', blank=True)
    category_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

