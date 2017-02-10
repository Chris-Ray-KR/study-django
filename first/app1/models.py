from django.db import models

# Create your models here.
class model_test(models.Model):
    objects = models.Manager()
    keyword = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.keyword