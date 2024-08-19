from django.urls import path
from . import views
# from .views import generate_transcript_pdf

urlpatterns = [
    # Course URLs
    path('', views.home, name="home"),
    path('course/', views.course_list, name="course_list"),
    path('course/create/', views.create_course, name='create_course'),
    path('course/update/<int:pk>/', views.update_course, name='update_course'),
    path('course/delete/<int:pk>/', views.delete_course, name='delete_course'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),

    # Semester URLs
    path('semester/list/', views.semester_list, name='semester_list'),
    path('semester/create/', views.create_semester, name='create_semester'),
    path('semester/<int:pk>/', views.semester_detail, name='semester_detail'),
    path('semester/<int:pk>/update/', views.update_semester, name='update_semester'),
    path('semester/<int:pk>/delete/', views.delete_semester, name='delete_semester'),


    path('students/', views.student_list, name='student_list'),
    path('transcript/<int:student_id>/', views.generate_transcript, name='student_transcript'),
    path('students/new/', views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('students/search/', views.student_search, name='student_search'),
    
    # Similar patterns for Course, Semester, Faculty





    path('faculty/', views.faculty_list, name='faculty_list'),
    path('add/', views.add_faculty, name='add_faculty'),
    path('<int:pk>/updete/', views.update_faculty, name='update_faculty'),
    path('<int:pk>/delite/', views.delete_faculty, name='delete_faculty'),



    path('exam-results/', views.exam_result_list, name='exam_results_list'),
    path('exam-results/add/', views.add_exam_result, name='add_exam_result'),
    path('exam-results/<int:pk>/update/', views.update_exam_result, name='update_exam_result'),
    path('exam-results/<int:pk>/delete/', views.delete_exam_result, name='delete_exam_result'),




    path('batch/', views.batch_list, name='batch_list'),
    path('create/', views.batch_create, name='batch_create'),
    path('<int:pk>/updatebatch/', views.batch_update, name='batch_update'),
    path('<int:pk>/deletebatch/', views.batch_delete, name='batch_delete'),



    # path('transcript/<int:student_id>/', views.transcript_view, name='generate_transcript'),
]
