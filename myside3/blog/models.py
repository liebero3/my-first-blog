from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextField()
    cdate = models.DateTimeField(default=timezone.now)
    pdate = models.DateTimeField(blank=True, null=True)
    mainpict = models.FileField(upload_to='uploads/', default='uploads/Pxjq6.jpg')
    kurs = models.CharField(max_length=15, default='1617PHEFGK2')

    def publish(self):
        self.pdate = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pdate']
