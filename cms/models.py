from django.db import models

# Create your models here.
class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/')
    cms_title = models.CharField(max_length=200, verbose_name='Title')
    cms_text = models.TextField(max_length=200, verbose_name='Text')

    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = ('Slides')