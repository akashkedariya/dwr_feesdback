from .models import Feedback_history
from django import forms 
# from django.forms import ModelForm
  
# creating a form 
class feedback_historyForm(forms.ModelForm): 
    class Meta:
        model = Feedback_history
        fields = [ 'project_topic','project_issue','reporting_manager','discussed_with_rm','message','attached_file' ]