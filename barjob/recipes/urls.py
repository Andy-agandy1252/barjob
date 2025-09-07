from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/add/', views.add_recipe, name='add_recipe'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    path('recipes/<int:pk>/update/', views.recipe_update, name='recipe_detail_update'),
]
