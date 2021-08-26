from django.db import models
from account.models import User
from datetime import datetime
from core.models import TimestampModel

#Post Model
class Post(TimestampModel):
    content = models.TextField(blank=True, verbose_name="방명록 내용")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likepost = models.ManyToManyField(User, through = 'LikePost', related_name = 'like_post', blank=True) 

    def __str__(self):
        return self.content
    class Meta:
        db_table = "post"
        verbose_name= "방명록"
        ordering=["-created_at"]

class PostImage(TimestampModel):
    post = models.ForeignKey(Post, related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts', blank=True, null=True)

    class Meta:
        db_table = "postImage"
        ordering=["created_at"]

# Comment Model
class Comment(TimestampModel):
    content = models.TextField(blank=True, verbose_name="댓글 내용")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.content
    class Meta:
        db_table = "comment"
        verbose_name= "댓글"
        ordering=["-created_at"]

# Like Model
class LikePost(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post', blank=True, db_column='post_id')
    is_like = models.BooleanField(default=False)

    class Meta:
        db_table = "likeposts"



# class Report(models.Model):