from django.db import models
from account.models import User
from datetime import datetime
from core.models import TimestampModel
from rest_framework.parsers import FormParser

# def get_file_path(instance, filename):
#     ymd_path = datetime.now().strftime("%Y/%m/%d")
#     ext = filename.split(".")[-1]
#     filename = "{}.{}".format(uuid4().hex, ext)
#     return "/".join(["feeds/", ymd_path, filename])

#Post Model
class Post(TimestampModel):
    content = models.TextField(blank=True, verbose_name="방명록 내용")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    class Meta:
        db_table = "post"
        verbose_name= "방명록"
        ordering=["-created_at"]

class PostImage(TimestampModel):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/',blank=True, null=True)

    class Meta:
        db_table = "postImage"
        ordering=["created_at"]

#Comment Model
# class Comment(models.Model):

# #Like Model
# class Like(models.Model):


# class Report(models.Model):
