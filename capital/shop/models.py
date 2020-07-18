from django.db import models

# Create your models here.

class Shirt(models.Model):
    Name=models.CharField( max_length=50)
    Contact= models.CharField( max_length=10)
    Height= models.DecimalField(max_digits=5, decimal_places=2)
    Widht= models.DecimalField(max_digits=5, decimal_places=2)
    Shoulder= models.DecimalField(max_digits=5, decimal_places=2)
    Hand_height= models.DecimalField(max_digits=5, decimal_places=2)
    Hand_width= models.DecimalField(max_digits=5, decimal_places=2)
    S=(
        ('Inprogress','Inprogress'),
        ('Done','Done'),
        ('Delivered','Delivered')
    )
    Status=models.CharField(choices=S, max_length=50)


    def __str__(self):
        return self.Name
    

class Pant(models.Model):
    Name= models.CharField(max_length=50)
    Contact= models.CharField( max_length=10)
    Height= models.DecimalField( max_digits=5, decimal_places=2)
    Waist= models.DecimalField(max_digits=5, decimal_places=2)
    Seat=models.DecimalField(max_digits=5, decimal_places=2)
    Rise=models.DecimalField( max_digits=5, decimal_places=2)
    thigh=models.DecimalField(max_digits=5, decimal_places=2)
    Styles=(
        ('Flat','flat'),
        ('single flit','single flit'),
        ('double flits','double flits')
    )
    Style =models.CharField(choices=Styles, max_length=50)
    Fit=(
        ('Regular fit','Regular fit'),
        ('Skinny fit','Skinny fit'),
        ('Slim fit','Slim fit'),
        ('Loose fir','Loose fit')
    )
    Fitting= models.CharField(choices=Fit, max_length=50)
    Bottoms=(
        ('Normal','Normal'),
        ('Bell','Bell'),
        ('Pencil','Pencil')
    )
    Bottom= models.CharField(choices=Bottoms, max_length=50)
    Pockets=(
        ('Straight','Straight'),
        ('Cross','Cross'),
        ('Jeans','Jeans')
    )
    Pocket_Style=models.CharField(choices=Pockets, max_length=50)
    Remarks= models.CharField( max_length=50)
    S=(
        ('Inprogress','Inprogress'),
        ('Done','Done'),
        ('Delivered','Delivered')
    )
    Status=models.CharField(choices=S, max_length=50)



    def __str__(self):
        return self.Name

    



