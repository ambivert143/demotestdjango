from django.db import models

# Create your models here.
class Product(models.Model):
	code = models.CharField(max_length=30, unique=True, verbose_name="Mã sản phẩm")
	name = models.CharField(max_length=300, verbose_name="Tên sản phẩm")
	price = models.FloatField(verbose_name="Đơn giá")

	def __str__(self):
		return self.name