from django.db import models

# Create your models here.


class Category(models.Model):
    code = models.CharField(max_length=30, unique=True, verbose_name="Mã")
    name = models.CharField(max_length=200, verbose_name="Tên")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, verbose_name="Nhóm sản phẩm", on_delete=models.PROTECT)
    code = models.CharField(max_length=30, unique=True, verbose_name="Mã")
    name = models.CharField(max_length=200, verbose_name="Tên")
    price = models.IntegerField(verbose_name="Đơn giá")
    image = models.ImageField(upload_to="static/images", verbose_name="Ảnh")

    def __str__(self):
        return self.name
