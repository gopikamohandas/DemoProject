from django.db import models

class Todo(models.Model):

    id = models.BigAutoField(
        primary_key=True
    )

    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name= 'Todo Title'
    )

    desription = models.TextField(
        max_length=300,
        verbose_name='Description'
    )

    createDate = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Todo Create Date'
    )

    updateDate = models.DateTimeField(
        auto_now=True,
    )

    status = models.BooleanField(
        default=False,
    )

    rating = models.IntegerField(
        default=1,
    )

    def __str__(self):
        return self.title
    
class Department(models.Model):

    dep_name = models.CharField(
        max_length= 50,
        null= False,
        blank= False,
        unique= True,
        verbose_name='Department Name',
    )

    dep_description = models.TextField(
        max_length= 300,
        verbose_name="Department Description",
    )

    def __str__(self):
        return self.dep_name
    
class Contact(models.Model):
    id = models.BigAutoField(
        primary_key = True
    )


    Name = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name='Name',
    )

    Phone_Number = models.IntegerField(
        max_length=10,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Phone Number',
    )
    def __str__(self):
        return self.Name
    
class Booking(models.Model):
    p_name=models.CharField(max_length=300)
    p_phone=models.IntegerField(max_length=10)
    p_email=models.EmailField()
    booking_date=models.DateField()
    bookin_on=models.DateField(auto_now=True)

    def __str__(self):
            return self.p_name
    

class Doctors(models.Model):
     doc_name=models.CharField(max_length=50)
     doc_sep=models.CharField(max_length=100)
     dep_name=models.ForeignKey(Department, on_delete=models.CASCADE)
     doc_img=models.ImageField(upload_to='doctors', default='default_image.jpg')

     def __str__(self):
        return 'Dr.' + self.doc_name + ' - (' + self.doc_sep + ')'
    
