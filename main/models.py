from django.db import models


class Home(models.Model):
    """Asosiy sahifadagi malumot uchun yozilgan"""
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title


class Table(models.Model):
    """Asosiy sahifa va blog sahifada ko;rinadi vaqtlar ish kunlari ayrim malumotlar kiritish uchun"""
    name = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.FileField(upload_to='about/')
    
    def __str__(self):
        return self.name

    
class Comment(models.Model):
    """Mijozlar qoldirgan komentaryalarni ko'rish uchun blog sahifada ko;rinadi"""
    title = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.FileField(upload_to='about/')

    def __str__(self):
        return self.body


class MedicalThem(models.Model):
    """Doktorlar malumotlari uchun blog sahifada ko'rinadi"""
    title = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.icon        


class Services(models.Model):
    """Qanday hizmat ko'rsatilishi uchun malumotlar ushbu Hizmatlar sahifasi uchun"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/')
    
    def __str__(self):
        return self.title 
    
    
class ServiceInformation(models.Model):
    """Hizmat ko'rsatishdagi kerakli malumotlar uchun Hizmatlar sahifasida ko'rinadi"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/')
    
    def __str__(self):
        return self.description
    
    
class Contact(models.Model):
    """Mijozlar biz bilan bog'lanishi uchun Habar qoldirish sahifasida ko'rinadi"""
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    body = models.TextField()             