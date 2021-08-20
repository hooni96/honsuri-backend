from django.db import models

#Post Model
class Post(models.Model):
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey("User", related_name="post", on_delete=models.CASCADE)
    
    # likes_post = models.ManyToManyField(
    #     User, 
    #     through= 'LikeProduct', 
    #     related_name='like_product', 
    #     blank=True
    # )
    # report_post = models.ManyToManyField(
    #     User, 
    #     through= 'ReportProduct', 
    #     related_name='report_product', 
    #     blank=True
    # )

    def __str__(self):
        return self.content
    class Meta:
        db_table = "post"
        verbose_name= "방명록"

#Comment Model
class Comment(models.Model):
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
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