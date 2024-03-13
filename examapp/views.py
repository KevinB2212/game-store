from django.shortcuts import render, get_object_or_404
import random
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')




class UserLoginView(LoginView):
    template_name='login.html'


def logout_user(request):
    logout(request)
    return redirect("/")


from django.contrib import messages
from .models import Game

def add_to_cart(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    if 'cart' not in request.session:
        request.session['cart'] = []

    cart = request.session['cart']

    for item in cart:
        if item['game_id'] == game.id:
            messages.info(request, f"{game.name} is already in your cart.")
            return redirect('game_list')

    cart.append({
        'game_id': game.id,
        'name': game.name,
        'price': float(game.price),
        'quantity': 1,
    })

    game.stock -= 1
    game.save()

    messages.success(request, f"{game.name} added to your cart.")
    return redirect('game_list')

def view_cart(request):
    cart = request.session.get('cart', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart)

    return render(request, 'view_cart.html', {'cart': cart, 'total_price': total_price})

def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game_detail.html', {'game': game})

def console_games(request, platform):
    games = Game.objects.filter(platform__iexact=platform)
    return render(request, 'console_games.html', {'games': games, 'platform': platform})


from .models import Game
from .forms import GameCreationForm


def create_game(request):
    if request.method == 'POST':
        form = GameCreationForm(request.POST)
        if form.is_valid():
            game = form.save()
            messages.success(request, f"{game.name} has been created.")
            return redirect('game_list')
    else:
        form = GameCreationForm()

    return render(request, 'create_game.html', {'form': form})
