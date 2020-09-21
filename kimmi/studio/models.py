from django.db import models

# Create your models here.
class Studio(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Title')
    url = models.URLField(verbose_name = 'URL', max_length=200, null=True, blank=True)
    image = models.ImageField(verbose_name = 'Images', upload_to='studio')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Date Uploaded')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Last Update')

    class Meta:
        verbose_name = 'Studio'
        verbose_name_plural = 'Studios'
        ordering = ['-created']
    
    def __str__(self):
        return self.title