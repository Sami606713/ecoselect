from djongo import models
from django.contrib.auth.models import User
from bson import ObjectId 
# Create your models here.
# Product Model
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    description=models.CharField(max_length=200,default="")
    category=models.CharField(max_length=20,choices=(
        ("Electronic","Electronic"),
        ("Fashion","Fashion"),
        ("Education","Education"),
        ("Vehicle","Vehicles")
    ))
    price=models.DecimalField(max_digits=10,decimal_places=2,default="")
    date=models.DateTimeField(auto_now=True)
    # image=models.ImageField(upload_to="media/images",default="")
    def __str__(self):
        return f"{self.name} {self.category}"
    
class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", default="")

    def __str__(self):
        return f"Image for {self.product.name}"


# End product 

# Contact model
class Contact(models.Model):
    _id=models.ObjectIdField(primary_key=True)
    name=models.CharField(max_length=100,default="")
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    msg=models.CharField(max_length=300,default="")

    def __str__(self):
        return f"{self.name} {self.email}"
# End contact

class Address(models.Model):
    _id =models.ObjectIdField(primary_key=True,default=ObjectId, editable=False)
    # _id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default="")
    address = models.CharField(max_length=250,null=False,default="")
    code = models.CharField(max_length=250,null=False)
    mobile = models.CharField(max_length=20, help_text="+12345678",null=False,default="")
    email = models.CharField(max_length=50, unique=True,default="")
    province = models.CharField(max_length=50, choices=(
       ("Azad Kashmir", "Azad Kashmir"),
       ("Balochistan", "Balochistan"),
       ("Islamabad", "Islamabad"),
       ("KPK", "KPK"),
       ("Punjab", "Punjab"),
       ("Sindh", "Sindh")
    ))
    city = models.CharField(max_length=50, choices=(
       ("haripur", "haripur"),
       ("Abbottabad", "Abbottabad"),
       ("Mansehera", "Mansehra"),
       ("Hattar", "Hattar"),
       ("Ghazi", "Ghazi")
    ))
    area = models.CharField(max_length=50, choices=(
       ("Pharhala", "Pharhala"),
       ("K.T.S", "K.T.S"),
       ("Amir khan plaza", "Amir Khan Plaza")
    ))

    def __str__(self):
        return f"{self.name} {self.city}"


class Order(models.Model):
    address=models.OneToOneField(Address, on_delete=models.CASCADE,primary_key=True)
    item_json=models.CharField(max_length=5000)

    def __str__(self):
        return f"{self.address.name}"

