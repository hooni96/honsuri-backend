from django.db import models

#Post Model
class Post(models.Model):
    content = models.TextField(blank=True, verbose_name="방명록 내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="방명록 작성 날짜")
    photo = models.CharField(max_length=100, verbose_name="방명록 사진")
    # user_id = models.ForeignKey("User", related_name="post", on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    class Meta:
        db_table = "post"
        verbose_name= "방명록"

#Comment Model
class Comment(models.Model):
    content = models.TextField(blank=True, verbose_name="댓글 내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="댓글 작성 날짜")
    # FK
    # post_id = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE, db_column="id")
    # user_id = models.ForeignKey("User", related_name="comment", on_delete=models.CASCADE)
    def __str__(self):
        return self.content
    class Meta:
        db_table = "comment"
        verbose_name= "댓글"

# #Like Model
# class Like(models.Model):
#     # FK
#     # post_id = models.ForeignKey("Post", related_name="comment, on_delete=models.CASCADE)
#     # user_id = models.ForeignKey("User", related_name="comment", on_delete=models.CASCADE)
#     class Meta:
#         db_table = "like"

# class Report(models.Model):
#     # FK
#     # post_id = models.ForeignKey("Post", related_name="comment, on_delete=models.CASCADE)
#     # user_id = models.ForeignKey("User", related_name="comment", on_delete=models.CASCADE)
#     class Meta:
#         db_table = "report"