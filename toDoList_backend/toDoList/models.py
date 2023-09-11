from django.db import models

# Create your models here.
class Item(models.Model):
    title=models.CharField(max_length=20,null=True)
    content=models.TextField(null=True)
    cover_url=models.URLField(null=True)
    file=models.FileField(verbose_name="上传文件",null=True,upload_to="file")
    # class Meta:
    #    # model = Item
    #     fields = ['title','content']