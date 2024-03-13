from django.urls import path, include
from . import views
from .forms import * # add o imports at the top of the file
from .views import game_list, game_detail, console_games, add_to_cart, view_cart
from .views import game_list

urlpatterns = [
    path('',views.index, name="index"),# mywebsite.com 
    path('register/', views.UserSignupView.as_view(), name="register"),
    path('login/',views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name='login'),
    path('logout/', views.logout_user, name="logout"),
    path('create_game/', views.create_game, name='create_game'),
    path('game_list/', views.game_list, name='game_list'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('console/<str:platform>/', views.console_games, name='console_games'),
    path('add_to_cart/<int:game_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
]