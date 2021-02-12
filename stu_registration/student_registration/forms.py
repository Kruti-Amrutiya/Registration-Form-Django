from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = {'fullname', 'dob', 'roll_num', 'gender', 'mobile', 'email', 'subject'}
        labels = {'fullname': 'Full Name', 'dob': 'Dob', 'roll_num': 'Roll Num', 'mobile': 'Mobile Num', 'email': 'Email Id'}

        def __init__(self, *args, **kwargs):
            super(StudentForm, self).__init__(*args, **kwargs)
            self.fields['subject'].empty_label = 'Select'
            self.fields['roll_num'].required = False
