from django.shortcuts import render
from django.http import HttpResponse
from gamerateapp.models import Game
from gamerateapp.models import Category
from gamerateapp.models import Review
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from gamerateapp.forms import ReviewForm
from django.urls import reverse
from gamerateapp.forms import UserForm, UserProfileForm
# Create your views here.

def index(request):

    top_gameplay = Game.objects.order_by('-gameplay_rating')[:1]
    top_graphics = Game.objects.order_by('-graphics_rating')[:1]
    top_story = Game.objects.order_by('-story_rating')[:1]
    top_difficulty = Game.objects.order_by('-difficulty_rating')[:1]
    
    context_dict = {}
    context_dict['top_gameplay'] = top_gameplay
    context_dict['top_graphics'] = top_graphics
    context_dict['top_story'] = top_story
    context_dict['top_difficulty'] = top_difficulty
    
    response = render(request, 'gamerateapp/index.html', context=context_dict)
    
    return response
    
def categories(request):

    context_dict = {}
    
    for categeroy in Category.objects.all():
        context_dict[category.str()] = Game.objects.filter(category = category)[:1].picture 
    

    response = render(request, 'gamerateapp/categories.html', context=context_dict)
    
    return response
    
def category(request, category_name_slug):

    context_dict = {}
    
    try:
        category = Category.objects.get(slug=category_name_slug)
        games = Game.objects.filter(category = category)
        
        context_dict['games'] = games
        context_dict['category'] = category
        
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['games'] = None
    
    
    response = render(request, 'gamerateapp/category.html', context=context_dict)
    
    return response
    
def game(request, game_name_slug):

    context_dict = {}

    try:
        game = Game.objects.get(slug=game_name_slug)
        reviews = Review.objects.order_by(game = game)
        
        context_dict['game'] = game
        context_dict['reviews'] = reviews
        
    except Game.DoesNotExist:
        context_dict['game'] = None
        
    
    
    response = render(request, 'gamerateapp/game.html', context=context_dict)
    return response

@login_required
def review(request, game_name_slug):
    try:
        game = Game.objects.get(slug=game_name_slug)
    except Game.DoesNotExist:
        game = None
    
    if game is None:
        return redirect('/gamerateapp/')
    
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            if game:
                review = form.save(commit=False)
                review.game = game
                review.save()
                
                return redirect(reverse('gamerateapp:game', kwargs={'game_name_slug': game_name_slug}))
        else:
            print(form.errors)
    
    context_dict = {'form': form, 'game': game}
    return render(request, 'gamerateapp/review.html', context=context_dict)
    
@login_required        
def profile(request, username):
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        user = None
    
    if user is None:
       return redirect('/gamerateapp/')
       
    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'website': user_profile.website, 'picture': user_profile.picture})
    
    try:
        publisher = Publisher.objects.get(profile = user_profile)
        games = Game.objects.filter(publisher = publisher)
    except Publisher.DoesNotExist:
        games = None
    
    context_dict = {'user_profile': user_profile, 'selected_user': user, 'form': form, 'games': games}
    
    return render(request, 'gamerateapp/profile.html', context_dict)
    
def publishers(request, username):

    publishers = Publisher.objects.all()
    
    context_dict['publishers'] = publishers

    
    return render(request, 'gamerateapp/publishers.html', context_dict)