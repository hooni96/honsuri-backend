from django.contrib import admin
from recipe.models import (Recipe, Base, Ingredient, Flavor, AlcoholVolume, 
                        RecipeAlcoholVolume, RecipeBase, RecipeFlavor, RecipeIngredient)

admin.site.register(Recipe)
admin.site.register(Base)
admin.site.register(Ingredient)
admin.site.register(Flavor)
admin.site.register(AlcoholVolume)
admin.site.register(RecipeAlcoholVolume)
admin.site.register(RecipeBase)
admin.site.register(RecipeFlavor)
admin.site.register(RecipeIngredient)

