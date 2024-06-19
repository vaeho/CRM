from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from .forms import UserRegistrationForm, UserLoginForm, AddRecordForm
from .models import User, Record


def index(request):
    if request.user.is_authenticated:
        user_records = Record.objects.filter(created_by=request.user)
        paginator = Paginator(user_records, 20)  # Show 10 records per page

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if request.headers.get('HX-Request'):
            table_html = render_to_string('partials/record_table_body.html', {'records': page_obj.object_list})
            pagination_html = render_to_string('partials/pagination_controls.html', {'page_obj': page_obj})
            return HttpResponse(table_html + pagination_html)

        return render(request, 'core/index.html', {'records': page_obj.object_list, 'page_obj': page_obj})
    else:
        return render(request, 'core/index.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'account/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def record_add(request):
    if request.method == 'GET':
        form = AddRecordForm()
        if request.headers.get('HX-Request'):
            return render(request, 'partials/add_record.html', {'form': form})
    elif request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.created_by = request.user
            record.save()

            if request.headers.get('HX-Request'):
                user_records = Record.objects.filter(created_by=request.user)
                table_html = render_to_string('partials/record_table_body.html', {'records': user_records})
                return HttpResponse(table_html)
            else:
                return redirect('index')


def record_delete(request, id):
    pass

def record_edit(request, id):
    pass


