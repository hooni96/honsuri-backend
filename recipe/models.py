from django.db import models
# ckeditor
from ckeditor.fields import RichTextField

# class Recipe(models.Model):
#     name = models.CharField(max_length=100, verbose_name="레시피 이름")
#     photo = models.CharField(max_length=100, verbose_name="사진 파일명")
#     how_to_mix = models.TextField(verbose_name="제조법")
#     base = models.PositiveSmallInteger(default=0, null=True)
#     ingredients = models.CharField(max_length=100, verbose_name="재료 이름")
#     youtube_link = models.URLField(max_length=2000, verbose_name="유튜브 url")
#     detail_contents = models.RichTextField(verbose_name="디테일 컨텐츠")
#     tag_set = models.ManyToManyField('Tag', blank = True)
    
#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = "recipe"

# class Tag(models.Model):
#     name = models.CharField(max_length=50, verbose_name="태그", unique=True)
#     def __str__(self):
#         return self.name

# class Bookmark(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
#     recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, db_column='recipe_id')

#     class Meta:
#         db_table = "bookmark"