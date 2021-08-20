from django.db import models
# ckeditor
from ckeditor.fields import RichTextField
from core.models import TimestampModel
from account.models import User

# m2m 테이블들
class Base(TimestampModel):
    name = models.CharField(max_length=50, verbose_name="술 베이스", unique=True)

    class Meta:
        db_table = "base"

class Ingredient(TimestampModel):
    name = models.CharField(max_length=50, verbose_name="재료", unique=True)

    class Meta:
        db_table = "ingredient"

class AlcoholVolume(TimestampModel):
    name = models.CharField(max_length=20, verbose_name="도수", unique=True)

    class Meta:
        db_table = "alcohol_volume"

class Flavor(TimestampModel):
    name = models.CharField(max_length=50, verbose_name="맛", unique=True)

    class Meta:
        db_table = "flavor"

class Recipe(TimestampModel):
    name = models.CharField(max_length=100, verbose_name="레시피 이름")
    photo = models.CharField(max_length=100, verbose_name="사진 파일명")
    how_to_mix = models.TextField(verbose_name="제조법")
    detail_contents = RichTextField(verbose_name="디테일 컨텐츠")
    youtube_link = models.URLField(max_length=2000, verbose_name="유튜브 url")
    
    base = models.ManyToManyField(Base, through = 'RecipeBase')
    ingredient = models.ManyToManyField(Ingredient, through = 'RecipeIngredient')
    alcohol_volume = models.ManyToManyField(AlcoholVolume, through = 'RecipeAlcoholVolume')
    flavor = models.ManyToManyField(Flavor, through = 'RecipeFlavor')
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "recipe"


# 중간 테이블들
class RecipeBase(TimestampModel):
    recipe  = models.ForeignKey(Recipe, on_delete = models.CASCADE, null=True)
    base = models.ForeignKey(Base, on_delete = models.CASCADE, null=True)
    
    class Meta:
        db_table = 'recipe_base'

class RecipeIngredient(TimestampModel):
    recipe  = models.ForeignKey(Recipe, on_delete = models.CASCADE, null=True)
    ingredient  = models.ForeignKey(Ingredient, on_delete = models.CASCADE, null=True)
    
    class Meta:
        db_table = 'recipe_ingredient'

class RecipeAlcoholVolume(TimestampModel):
    recipe  = models.ForeignKey(Recipe, on_delete = models.CASCADE, null=True)
    alcohol_volume  = models.ForeignKey(AlcoholVolume, on_delete = models.CASCADE, null=True)
    
    class Meta:
        db_table = 'recipe_alcohol_volume'

class RecipeFlavor(TimestampModel):
    recipe  = models.ForeignKey(Recipe, on_delete = models.CASCADE, null=True)
    flavor  = models.ForeignKey(Flavor, on_delete = models.CASCADE, null=True)
    
    class Meta:
        db_table = 'recipe_flavor'


class Bookmark(TimestampModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, db_column='recipe_id')

    class Meta:
        db_table = "bookmark"