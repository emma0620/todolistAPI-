from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)  # 待辦事項的標題
    description = models.TextField(blank=True, null=True)  # 詳細描述
    completed = models.BooleanField(default=False)  # 是否完成
    created_at = models.DateTimeField(auto_now_add=True)  # 建立時間
    updated_at = models.DateTimeField(auto_now=True)  # 更新時間

    def __str__(self):
        return self.title
