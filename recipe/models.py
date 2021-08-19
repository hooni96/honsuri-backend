from django.db import models
# ckeditor
from ckeditor.fields import RichTextField
from core.models import TimestampModel

class Recipe(TimestampModel):
    name = models.CharField(max_length=100, verbose_name="레시피 이름")
    photo = models.CharField(max_length=100, verbose_name="사진 파일명")
    how_to_mix = models.TextField(verbose_name="제조법")
    detail_contents = models.RichTextField(verbose_name="디테일 컨텐츠")
    youtube_link = models.URLField(max_length=2000, verbose_name="유튜브 url")
    
    base = models.ManyToManyField(Base, through = 'RecipeBase')
    ingredient = models.ManyToManyField(Ingredient, through = 'IngredientBase')
    alcohol_volume = models.ManyToManyField(AlcoholVolume, through = 'AlcoholVolumeBase')
    flavor = models.ManyToManyField(Flavor, through = 'FlavorBase')
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "recipe"

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

# 중간 테이블들
class RecipeBase(models.Model):
    recipe  = models.ForeignKey(Recipe, on_delete = models.CASCADE, null=True)
    base = models.ForeignKey(Base, on_delete = models.CASCADE, null=True)
    
    class Meta:
    db_table = 'recipe_base'

class IngredientBase(models.Model):
    ingredient  = models.ForeignKey(Ingredient, on_delete = models.CASCADE, null=True)
    base = models.ForeignKey(Base, on_delete = models.CASCADE, null=True)
    
    class Meta:
    db_table = 'ingredient_base'

class AlcoholVolumeBase(models.Model):
    alcohol_volume  = models.ForeignKey(AlcoholVolume, on_delete = models.CASCADE, null=True)
    base = models.ForeignKey(Base, on_delete = models.CASCADE, null=True)
    
    class Meta:
    db_table = 'alcohol_volume_base'

class FlavorBase(models.Model):
    flavor  = models.ForeignKey(Flavor, on_delete = models.CASCADE, null=True)
    base = models.ForeignKey(Base, on_delete = models.CASCADE, null=True)
    
    class Meta:
    db_table = 'flavor_base'

class Bookmark(TimestampModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, db_column='recipe_id')

    class Meta:
        db_table = "bookmark"