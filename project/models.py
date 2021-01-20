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


class FloorPlan(models.Model):
    image = models.ImageField(upload_to='media')


class FloorPlanSection(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=255)
    boundaries = models.CharField(max_length=50)
    floorplan = models.OneToOneField("project.FloorPlan", on_delete=models.CASCADE)

class CarouselItem(models.Model):
    desc = models.TextField()
    project = models.ForeignKey("project.Project", related_name='carousel_items', on_delete=models.CASCADE)


class CarouselPhoto(models.Model):
    photo = models.ImageField(upload_to='media')
    carouselItem = models.ForeignKey("project.CarouselItem", on_delete=models.CASCADE)

class CarouselVideo(models.Model):
    video = models.FileField(upload_to='media/files')
    carouselItem = models.ForeignKey("project.CarouselItem", on_delete=models.CASCADE)
