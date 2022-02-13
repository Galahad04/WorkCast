from .models import Radio
from django.forms import TextInput, Textarea, RadioSelect, ModelForm


class RadioForm(ModelForm):

	# options = forms.BooleanField()

	# def __init__(self):
	# 	if check_something():
	# 		self.fields['options'].initial = True


	class Meta:
		model = Radio
		fields = ["title", "task", "gender", "options"] 
		widgets = {
			"title" : TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'Enter name'
				}),

			"task" : Textarea(attrs={
				'class' : 'form-control',
				'placeholder' : 'Enter description'
				}),

			"gender" : RadioSelect}

