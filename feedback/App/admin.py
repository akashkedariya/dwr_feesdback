from django.contrib import admin
from .models import Project_topic, Project_issue, Feedback_history

# Register your models here.

@admin.register(Project_topic)
class project_topicAdmin(admin.ModelAdmin):
    list_display = [ 'id','topic']

@admin.register(Project_issue)
class project_issueAdmin(admin.ModelAdmin):
    list_display = [ 'id','issue_type']


@admin.register(Feedback_history)
class feedback_historyAdmin(admin.ModelAdmin):
    list_display = [ 'id','project_topic','project_issue','reporting_manager','discussed_with_rm','message','attached_file','created_date' ]
