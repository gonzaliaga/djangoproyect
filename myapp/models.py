from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="myapp/img")
    def __str__(self):
        return self.title
    
class Task (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.title + ' - ' + 'Proyecto -> ' + self.project.title