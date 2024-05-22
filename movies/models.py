from django.db import models

# Create your models here.

from django.urls import reverse


class Actress(models.Model):
    name = models.CharField(max_length=25)
    enName = models.CharField(max_length=50)
    birth = models.IntegerField(null=True)
    height = models.CharField(max_length=5, null=True)
    debut = models.CharField(max_length=10, null=True)
    info = models.TextField(null=True, default="NO DATA")

    def __str__(self):
        """ String for representing the object (in Admin site etc.)."""

        return f"{self.name} ({self.enName})"
    
    # Metadata
    class Meta:
        ordering = ['enName']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of ModelName."""
        
        return reverse('actress', args=[str(self.id)])
    

class Movies(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=200)
    actress = models.ManyToManyField(Actress, blank=True, related_name="movies")
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    info = models.TextField(null=True, default="NO DATA")

    def __str__(self):
        return f"{self.title} {self.description} {self.actress}"
    
    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of ModelName."""
        
        return reverse('movies', args=[str(self.id)])


# added for the test

class Category(models.Model):
    category = models.CharField(max_length=15)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ["category"]


# added for the test

class ItemCode(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=200)
    actress = models.ForeignKey(Actress, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]