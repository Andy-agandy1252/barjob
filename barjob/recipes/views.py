from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.files.storage import default_storage
import os
from .forms import RecipeForm
from .models import Recipe

def menu(request):
    return render(request, 'recipes/menu.html')
from django.shortcuts import render, redirect
from .forms import RecipeForm

def add_recipe(request):
    """
    View to handle adding a new recipe. Includes support for the category field and 10 images.
    """
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)  # Handle both form data and file uploads
        if form.is_valid():
            form.save()  # Save the recipe, including the images
            return redirect('recipe_list')  # Redirect to the recipe list after saving
    else:
        form = RecipeForm()  # If GET request, provide an empty form for the user to fill out

    return render(request, 'recipes/add_recipe.html', {'form': form})  # Render the form template




def recipe_list(request):
    # Get the sort and order parameters from the query string
    sort_by = request.GET.get('sort', 'name')  # Default to sorting by name
    order = request.GET.get('order', 'asc')  # Default to ascending order
    query = request.GET.get('query', '')  # Get the search query (if any)

    # Apply search filter if a query is provided
    recipes = Recipe.objects.all()
    if query:
        recipes = recipes.filter(
            Q(name__icontains=query) |
            Q(code__icontains=query) |
            Q(category__icontains=query)  # Add category filter here
        )

    # Apply sorting based on the sort_by and order parameters
    if sort_by == 'name':
        recipes = recipes.order_by('name' if order == 'asc' else '-name')
    elif sort_by == 'code':
        recipes = recipes.order_by('code' if order == 'asc' else '-code')
    elif sort_by == 'category':
        recipes = recipes.order_by('category' if order == 'asc' else '-category')

    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'order': order,
        'query': query,
        'sort_by': sort_by
    })


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def recipe_update(request, pk):
    """
    View to update a specific recipe's details.
    Handles image deletions and recipe updates.
    """
    recipe = get_object_or_404(Recipe, pk=pk)
    old_code = recipe.code  # Store the old code

    if request.method == 'POST':
        # Handle image deletions dynamically
        image_fields = ['image1', 'image2', 'image3', 'image4', 'image5','image6', 'image7', 'image8', 'image9', 'image10']
        for field in image_fields:
            if f'delete_{field}' in request.POST:
                image = getattr(recipe, field)  # Get the image field dynamically
                if image:
                    image_path = image.path
                    if os.path.exists(image_path):
                        default_storage.delete(image_path)
                    setattr(recipe, field, None)  # Set the image field to None

        # Handle recipe updates
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()  # Save changes to the recipe
            return redirect('recipe_detail_update', pk=recipe.pk)
        else:
            # If form is invalid, set the code back to its old value to ensure it's not lost
            form.instance.code = old_code

    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/recipe_detail_update.html', {'recipe': recipe, 'form': form})


def delete_recipe(request, recipe_id):
    # Get the recipe by its ID or return a 404 error if not found
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # Delete the recipe
    recipe.delete()

    # Redirect back to the current page (the recipe list)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('recipe_list')))