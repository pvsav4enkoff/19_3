from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegistr
from task1.models import Buyer, Game

# users = ['user', 'username', 'truelogin']
# Create your views here.
def task4_view_platform(request):
    header = "Главная страница"
    context = {'header': header}
    return render(request, 'platform.html',context)


def task4_view_games(request):
    header = "Игры"
    title = Game.objects.all().values_list('title', flat=True)
    description = Game.objects.all().values_list('description', flat=True)
    cost = Game.objects.all().values_list('cost', flat=True)
    games = zip(title, description, cost)
    context = {'games': games, 'header': header}
    return render(request, 'games.html', context)


def task4_view_cart(request):
    header = "Корзина"
    content = "Ваша корзина пуста"
    context = {'header': header, 'content': content}

    return render(request, 'cart.html', context)



def sign_up_by_html(request):
    error = None
    good = None
    if request.method == "POST":
        username = request.POST.get('username')
        users = Buyer.objects.all().values_list('name', flat=True)
        if username in users:
            error = 'Такой логин уже существует.'
        balance = request.POST.get('balance')
        age = request.POST.get('age')
        if error is None:
            Buyer.objects.create(name=username, balance=balance, age=age)
            good = f'Приветствуем, {username}!'
        info = {'good': good, 'error': error}
        return render(request, 'registration_page.html', info)
    else:
        return render(request, 'registration_page.html')

def sign_up_by_django(request):
    error = None
    good = None
    if request.method == "POST":
        form = UserRegistr(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            users = Buyer.objects.all().values_list('name', flat=True)
            if username in users:
                error = 'Такой логин уже существует.'
            balance = form.cleaned_data['balance']
            age = form.cleaned_data['age']
            if error == None:
                Buyer.objects.create(name=username, balance=balance, age=age)
                good = f'Приветствуем, {username}!'
        else:
            error = 'Форма не валидна.'
        info = {'good': good, 'error': error}
        return render(request, 'registration_page.html', info)
    else:
        form = UserRegistr()
        return render(request, 'registration_page.html')
