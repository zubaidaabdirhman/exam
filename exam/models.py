from django.db import models
from decimal import Decimal

# Create your models here.
from django.db import models

class Semester(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    faculty_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    credit_hours = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    faculties = models.ManyToManyField(Faculty)

    def __str__(self):
        return self.title

class Batch(models.Model):
    name = models.CharField(max_length=100)  # e.g., "2024 - CS101"
    year = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)  # Adjust if 'Semester' is in a different app

    def __str__(self):
        return f"{self.name} ({self.year})"





class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    contact_details = models.TextField()
    courses = models.ManyToManyField(Course, through='ExamResult')

    def __str__(self):
        return self.name


    def calculate_sgpa(self, semester):
        results = ExamResult.objects.filter(student=self, semester=semester)
        total_credits = Decimal(0)
        total_points = Decimal(0)
        for result in results:
            credits = Decimal(result.course.credit_hours)
            total_credits += credits

            # Convert score to a GPA scale, ensuring all values are Decimal
            if result.score == 100:
                points = Decimal(4.0) * credits
            else:
                points = (Decimal(result.score) / Decimal(100)) * Decimal(4) * credits

            total_points += points
        
        return total_points / total_credits if total_credits > 0 else Decimal(0)



    def calculate_ogpa(self):
        semesters = Semester.objects.all()
        total_credits = Decimal(0)
        total_points = Decimal(0)

        for semester in semesters:
            results = ExamResult.objects.filter(student=self, semester=semester)
            
            for result in results:
                credits = Decimal(result.course.credit_hours)
                total_credits += credits
                
                # Convert SGPA calculation to use Decimal
                if result.score == 100:
                    points = Decimal(4.0) * credits
                else:
                    points = (Decimal(result.score) / Decimal(100)) * Decimal(4) * credits
                
                total_points += points

        return total_points / total_credits if total_credits > 0 else Decimal(0)



class ExamResult(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.name} - {self.course.title} - {self.score}"
    