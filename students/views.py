from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

@login_required
def dashboard(request):
    query = request.GET.get('q')

    if query:
        students_list = Student.objects.filter(
            Q(name__icontains=query) |  # Adjust field name if needed
            Q(student_class__icontains=query)
        ).order_by('-created_at')
    else:
        students_list = Student.objects.all().order_by('-created_at')

    paginator = Paginator(students_list, 10)  # 10 students per page
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    return render(request, 'dashboard.html', {
        'students': students,
        'query': query,
    })


@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully")
            return redirect('dashboard')
    else:
        form = StudentForm()
    
    context = {'form': form, 'form_title': 'Add Student'}
    return render(request, 'add_edit.html', context)

@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'form_title': 'Edit Student'
    }
    return render(request, 'add_edit.html', context)

@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, "Student deleted successfully")
    return redirect('dashboard')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'students/login.html')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')
