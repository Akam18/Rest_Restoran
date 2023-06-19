from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name="Тame of the dish")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Category")
    image = models.ImageField(upload_to="food/", verbose_name="Image")
    price = models.PositiveIntegerField(verbose_name="Price")
    description = models.TextField(max_length=200, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")


    def __str__(self) -> str:
        return f"{self.title} {self.category}"


    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"


class Events(models.Model):
    image = models.ImageField(upload_to="events/", verbose_name="Image")
    title = models.CharField(max_length=100, verbose_name="Title Event")
    price = models.PositiveIntegerField(verbose_name="Price")
    description = models.TextField(max_length=200, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")


    def __str__(self) -> str:
        return f"{self.title} - {self.price} - {self.created_at}"
    

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


class Reservation(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(max_length=150, verbose_name="Email")
    phone = models.CharField(max_length=13, verbose_name="Phone")
    date = models.DateField(verbose_name="Date")
    time = models.TimeField(verbose_name="Time")
    persons = models.PositiveSmallIntegerField(verbose_name="Persons")
    message = models.TextField(max_length=500, verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    def __str__(self) -> str:
        return f"{self.full_name} - {self.phone} - {self.date} - {self.time} - {self.persons} - {self.created_at}"
    

    class Meta:
        verbose_name = "reserv"
        verbose_name_plural = "reservation"


class Testimonials(models.Model):
    image = models.ImageField(upload_to="testimonials/", 
        verbose_name="Изображение", blank=True, null=True)
    first_name = models.CharField(verbose_name="Имя", max_length=120)
    last_name = models.CharField(verbose_name="Фамилия", max_length=120)
    description = models.TextField(verbose_name="Тематика", max_length=120)
    profession = models.CharField(verbose_name="Профессия", max_length=120)
    created_at = models.DateTimeField(auto_now_add=True,
        verbose_name="Дата создания")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} | Профессия: {self.profession} | {self.created_at}"

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/", verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
            return f"Фотография {self.image}"


class Role(models.Model):
    title = models.CharField(max_length=120, verbose_name="Role")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created") 

    def __str__(self) -> str:
        return f"{self.title} - {self.created_at}"    

    class Meta:
        verbose_name = ("Role")
        verbose_name_plural = ("Roles")

                                          


class Chefs(models.Model):
    image = models.ImageField(upload_to="shefs/", 
        verbose_name="Изображение", blank=True, null=True)
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, 
        verbose_name="Роль повара")
    twitter  = models.URLField(blank=True, null=True, unique=True, 
        verbose_name="twitter Url", max_length=300)
    facebook = models.URLField(blank=True, null=True, unique=True, 
        verbose_name="facebook Url", max_length=300)
    instagram = models.URLField(blank=True, null=True, unique=True,
        verbose_name="instagram Url", max_length=300)
    linkedin = models.URLField(blank=True, null=True, unique=True, 
        verbose_name="linkedin Url", max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, 
        verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.full_name} | {self.role} | {self.created_at}"
    
    class Meta:
        verbose_name = "Повар"
        verbose_name_plural = "Повара"

class Contact(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    email = models.CharField(verbose_name="email", max_length=50)
    subject = models.CharField(verbose_name="Subject", max_length=120)
    message = models.TextField(verbose_name="Message", max_length= 120)
    created_at = models.DateTimeField(verbose_name="Created at", max_length=120)

    def __str__(self) -> str:
        return f"{self.full_name} - {self.subject} - {self.message} - {self.created_at}" 
