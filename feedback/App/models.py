from django.db import models

# Create your models here.

class Project_topic(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=200)

    def __str__(self) :
        return self.topic
  

class Project_issue(models.Model):
    id = models.AutoField(primary_key=True)
    issue_type = models.CharField(max_length=200)
    
    def __str__(self) :
        return self.issue_type


class Feedback_history(models.Model):
    id = models.AutoField(primary_key=True)
    project_topic = models.ForeignKey(Project_topic, on_delete=models.CASCADE) 
    project_issue = models.ForeignKey(Project_issue, on_delete=models.CASCADE)   
    reporting_manager = models.CharField(max_length=200)
    discussed_with_rm = models.BooleanField()
    message = models.CharField(max_length=460)
    attached_file = models.FileField(upload_to="uploads/")
    created_date = models.DateField(auto_now_add=True,null=True)