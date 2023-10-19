from django.shortcuts import render
from .forms import IceCreamForm, MyForm
from django.core.paginator import Paginator
from .models import IceCream


def create_ice_cream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            form.save()
            # редирект на страницу с инфой о мороженом 
    else:
        form = IceCreamForm()
    return render(request, 'tasks/ice_cream_form.html', {'form': form})

def task_list(request):
    task_list = IceCream.objects.all()  # получить все объекты модели
    paginator = Paginator(task_list, 10)  # разделитель
    page = request.GET.get('page')  # получить номер текущей страницы 
    tasks = paginator.get_page(page)  # pолучитm объекты текущей страницы

    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = f'Task {task_id}'  # получение задачи из бд
    return render(request, 'tasks/task_detail.html', {'task': task})


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()  
            return render(request, 'tasks/success.html', {'form': form})
    else:
        form = MyForm()

    return render(request, 'tasks/form.html', {'form': form})