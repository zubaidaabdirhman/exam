from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Course,Student,Semester,Faculty,Batch,ExamResult
from django.db.models import Q
# from weasyprint import 
from django.core.paginator import Paginator
from .forms import CourseForm,SemesterForm,StudentForm,FacultyForm,BatchForm,ExamResultForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

# Create your views here.
def course_list(request):
    all_courses = Course.objects.order_by('code')
    query = request.GET.get('q', '')
    if query:
        all_courses = Course.objects.filter(name__icontains=query)
    else:
        all_courses = Course.objects.all()

    paginator = Paginator(all_courses, 10)  # Show 10 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'courses/course_list.html', {'page_obj': page_obj})





# views.py


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully!')
            return redirect('course_list')
        else:
            messages.error(request, 'Error adding course.')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})


# views.py
def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})





def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)  # Retrieve the course using `pk`
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'update_course.html', {'form': form})


# views.py
def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'delete_courses.html', {'course': course})









def semester_list(request):
    semesters = Semester.objects.all()  # Use the correct model reference
    return render(request, 'semester/semester_list.html', {'semesters': semesters})

def create_semester(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('semester_list')
    else:
        form = SemesterForm()
    return render(request, 'semester/create_semester.html', {'form': form})

# def create_semester(request):
#     if request.method == 'POST':
#         form = SemesterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Course added successfully!')
#             return redirect('course_list')
#         else:
#             messages.error(request, 'Error adding course.')
#     else:
#         form = SemesterForm()
#     return render(request, 'semester/create_semester.html', {'form': form})








def semester_detail(request, pk):
    semester = get_object_or_404(Semester, pk=pk)  # Use the correct model reference
    return render(request, 'semester/semester_detail.html', {'semester': semester})

def update_semester(request, pk):
    semester = get_object_or_404(Semester, pk=pk)  # Use the correct model reference
    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=semester)
        if form.is_valid():
            form.save()
            return redirect('semester_detail', pk=semester.pk)
    else:
        form = SemesterForm(instance=semester)
    return render(request, 'semester/create_semester.html', {'form': form})

def delete_semester(request, pk):
    semester = Semester.objects.get(pk=pk) # Use the correct model reference
    if request.method == 'POST':
        semester.delete()
        return redirect('semester_list')
    return render(request, 'delete_semester.html', {'semester': semester})










def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/create_student.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'delete_student.html', {'student': student})

def student_search(request):
    query = request.GET.get('q')
    students = Student.objects.filter(name__icontains=query)
    return render(request, 'students/student_list.html', {'students': students})














# List Faculties

def faculty_list(request):
    query = request.GET.get('q')
    department_filter = request.GET.get('department')

    faculties = Faculty.objects.all()

    if query:
        faculties = faculties.filter(
            Q(name__icontains=query) | 
            Q(faculty_id__icontains=query)
        )

    if department_filter:
        faculties = faculties.filter(department__icontains=department_filter)

    return render(request, 'faculty/faculty_list.html', {
        'faculties': faculties,
        'query': query,
        'department_filter': department_filter,
    })
# Add Faculty
def add_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyForm()
    return render(request, 'faculty/create_faculty.html', {'form': form})

# Update Faculty
def update_faculty(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyForm(instance=faculty)
    return render(request, 'update_faculty.html', {'form': form})

# Delete Faculty
def delete_faculty(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        faculty.delete()
        return redirect('faculty_list')
    return render(request, 'delete_faculty.html', {'faculty': faculty})












def batch_list(request):
    batches = Batch.objects.all()
    return render(request, 'batch/batch_list.html', {'batches': batches})

def batch_create(request):
    if request.method == 'POST':
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('batch_list')
    else:
        form = BatchForm()
    return render(request, 'batch/create_batch.html', {'form': form})

def batch_update(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    if request.method == 'POST':
        form = BatchForm(request.POST, instance=batch)
        if form.is_valid():
            form.save()
            return redirect('batch_list')
    else:
        form = BatchForm(instance=batch)
    return render(request, 'batch/create_batch.html', {'form': form})

def batch_delete(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    if request.method == 'POST':
        batch.delete()
        return redirect('batch_list')
    return render(request, 'batch/delete_batch.html', {'batch': batch})





def exam_result_list(request):
    results = ExamResult.objects.all()
    return render(request, 'exam_result/exam_result_list.html', {'results': results})



def add_exam_result(request):
    if request.method == 'POST':
        form = ExamResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_results_list')
    else:
        form = ExamResultForm()
    return render(request, 'exam_result/add_exam_result.html', {'form': form})




def update_exam_result(request, pk):
    result = get_object_or_404(ExamResult, pk=pk)
    if request.method == 'POST':
        form = ExamResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect('exam_result_list')
    else:
        form = ExamResultForm(instance=result)
    return render(request, 'exam_result/update_exam_result.html', {'form': form, 'result': result})






def delete_exam_result(request, pk):
    result = get_object_or_404(ExamResult, pk=pk)
    if request.method == 'POST':
        result.delete()
        return redirect('exam_result_list')
    return render(request, 'exam_result/delete_exam_result.html', {'result': result})








def generate_transcript(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    
    # Calculate SGPA and OGPA
    semesters = Semester.objects.all()
    transcript_data = {
        'student': student,
        'semesters': semesters,
        'sgpas': {semester: student.calculate_sgpa(semester) for semester in semesters},
        'ogpa': student.calculate_ogpa()
    }
    
    return render(request, 'transcript.html', transcript_data)




# def generate_transcript_pdf(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)
#     semesters = Semester.objects.all()
#     transcript_data = {
#         'student': student,
#         'semesters': semesters,
#         'sgpas': {semester: student.calculate_sgpa(semester) for semester in semesters},
#         'ogpa': student.calculate_ogpa()
#     }
    
#     # Render the transcript HTML
#     html = render_to_string('transcript_pdf.html', transcript_data)
    
#     # Generate the PDF
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="Transcript_{student.student_id}.pdf"'
    
#     HTML(string=html).write_pdf(response)
    
#     return response





