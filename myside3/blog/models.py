from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    abstract = models.TextField(max_length=300, default='...')
    text = RichTextField()
    cdate = models.DateTimeField(default=timezone.now)
    pdate = models.DateTimeField(blank=True, null=True)
    mainpict = models.FileField(upload_to='uploads/', default='uploads/Pxjq6.jpg')
    kurs = models.ForeignKey('auth.Group')

    def publish(self):
        self.pdate = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pdate']

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
