from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='media')
    description = models.TextField()
    brochure = models.FileField(upload_to='media/files')
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title    

class LargeText(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    project = models.ForeignKey("project.Project", related_name='largetext', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class LargeTextSubsection(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    largetext = models.ForeignKey("project.LargeText", related_name='largetext_subsection', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class SmallText(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    project = models.ForeignKey("project.Project", related_name='smalltext', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CarouselItem(models.Model):
    desc = models.TextField()
    project = models.ForeignKey("project.Project", related_name='carousel_items', on_delete=models.CASCADE)


    