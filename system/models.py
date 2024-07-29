from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    

class Material(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class ProductMaterial(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    material = models.ForeignKey(Material,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.product.name} - {self.material.name}'

class Warehouse(models.Model):
    material= models.ForeignKey(Material,on_delete=models.CASCADE)
    remainder = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return f'{self.material.name} - {self.remainder}'