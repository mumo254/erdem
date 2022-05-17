from django.db import models
from cloudinary.models import CloudinaryField

class Blogs(models.Model):
    image = CloudinaryField('image')
    heading = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.heading

class Reply(models.Model):
    comment = models.CharField(max_length=250, blank=False)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=256, null=True)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)


    def __str__(self):
        return self.comment
    