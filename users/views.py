from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from books.models import *
from django.views.generic import ListView
from django.contrib.auth.models import Group


# Create your views here.
def base(request):
    books = Book.objects.all()
    return render(request, 'base.html', {'books': books})

class BookListView(ListView):
    model = Book
    template_name = 'user/base.html'
    context_object_name = 'books'
    ordering = ['-pub_date']
    paginate_by = 2


def register(request):
    # user = None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has ben created!{username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})        


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Has Been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'users/profile.html', context)