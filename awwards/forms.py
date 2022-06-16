from django import forms
from .models import Projects,Rating,RATES


class ProjectSubmissionForm(forms.ModelForm):
    '''
    Class that handles project submission
    '''
    class Meta:
        model = Projects
        fields = '__all__'

class UpdateProjectForm(forms.ModelForm):
    '''
    Class that handles project update
    '''
    class Meta:
        model = Projects
        fields = '__all__'
        exclude = ['user','pub_date']

class RateProjectForm(forms.ModelForm):
    '''
    Class that handles ratings
    '''
    usability = forms.ChoiceField(choices=RATES,required=True,widget=forms.Select())
    content = forms.ChoiceField(choices=RATES,required=True,widget=forms.Select())
    design= forms.ChoiceField(choices=RATES,required=True,widget=forms.Select())
    
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']