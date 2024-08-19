from django import forms
from .models import Course, Semester, Student, Faculty, Batch,ExamResult

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'title', 'credit_hours', 'semester', 'faculties']
        
class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['name', 'start_date', 'end_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter semester name',
                'class': 'form-input rounded-md'
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'Start Date',  # More intuitive placeholder
                'class': 'form-input rounded-md',
                'onfocus': "(this.type='date')",  # Ensures the date picker pops up
                'onblur': "if(this.value==''){this.type='text'}"  # Reverts to text when empty to show placeholder
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'End Date',  # More intuitive placeholder
                'class': 'form-input rounded-md',
                'onfocus': "(this.type='date')",
                'onblur': "if(this.value==''){this.type='text'}"
            }),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'batch', 'contact_details']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'text-sm py-1 px-2 rounded'}),
            'student_id': forms.TextInput(attrs={'class': 'text-sm py-1 px-2 rounded'}),
            'batch': forms.Select(attrs={'class': 'text-sm py-1 px-2 rounded'}),
            'contact_details': forms.Textarea(attrs={'class': 'text-sm py-1 px-2 rounded'}),
        }

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'department', 'faculty_id']




class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['name', 'year', 'course', 'semester']


class ExamResultForm(forms.ModelForm):
    class Meta:
        model = ExamResult
        fields = ['student', 'course', 'semester', 'score']