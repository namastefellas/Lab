from django.db import models

category_choice = [('computers', 'Computers'), ('keyboards', 'Keyboards'), ('others', 'Others'), ('mouses', 'Mouses'), ('headphones', 'Headphones')]
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=2000, null=True, blank=True)
    category = models.CharField(max_length=100, null=False, blank=False, default='others', choices=category_choice)
    leftover = models.IntegerField(null=False, blank=False)
    product_cost = models.DecimalField(max_digits=7, decimal_places=2)
    order = models.ManyToManyField(
        'webapp.Order',
        related_name='products',
        verbose_name='Order',
        through='webapp.ProductOrder',
        through_fields=('product', 'order'),
        blank=True
    )
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):

        return f'{self.product_name} {self.description} {self.category} {self.leftover} {self.product_cost}'



class Basket(models.Model):
    product_b = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, verbose_name='Product', related_name='products', default=1)
    product_qty = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = 'basket'
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'


class Order(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100, verbose_name='User Name')
    phone = models.IntegerField(null=False, blank=False, verbose_name='Phone Number')
    adress = models.CharField(null=False, blank=False, max_length=200, verbose_name='Adress')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'



class ProductOrder(models.Model):
    product = models.ForeignKey(
        'webapp.Product', 
        related_name='o_product',
        on_delete=models.CASCADE,
        verbose_name='Product'
        )
    
    order = models.ForeignKey(
        'webapp.Order',
        related_name='product_o',
        on_delete=models.CASCADE,
        verbose_name='Order'
    )