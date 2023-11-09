from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    icon = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title
