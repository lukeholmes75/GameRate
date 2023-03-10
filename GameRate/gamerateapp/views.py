from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    top_gameplay = Game.objects.order_by('-gameplayrating')[:1]
    top_graphics = Game.objects.order_by('-graphicsrating')[:1]
    top_story = Game.objects.order_by('-storyrating')[:1]
    top_difficulty = Game.objects.order_by('-difficultyrating')[:1]
    
    gameplay_publisher = top_gameplay.publisher
    graphics_publisher = top_graphics.publisher
    story_publisher = top_story.publisher
    difficulty_publisher = top_difficulty.publisher
    
    context_dict = {}
    context_dict['top_gameplay'] = top_gameplay
    context_dict['top_graphics'] = top_graphics
    context_dict['top_story'] = top_story
    context_dict['top_difficulty'] = top_difficulty
    
    context_dict['gameplay_publisher'] = gameplay_publisher
    context_dict['graphics_publisher'] = graphics_publisher
    context_dict['story_publisher'] = story_publisher
    context_dict['difficulty_publisher'] = difficulty_publisher
    
    response = render(request, 'gamerateapp/index.html', context=context_dict)
    
    return response
    
def categories(request):
    
    



    

    response = render(request, 'gamerateapp/categories.html', context=context_dict)
    
    return response
    
def category(request, category_name_slug):

    

    response = render(request, 'gamerateapp/category.html', context=context_dict)
    
    return response
    
def game(request, game_name_slug):
    
    
    response = render(request, 'gamerateapp/game.html', context=context_dict)
    return response