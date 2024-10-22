from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Books(models.Model):
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='books/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Ilmiy(models.Model):
    category = models.ForeignKey(Category, related_name='ilmiy', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, related_name='ilmiy', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    def __str__(self):
        return self.title

class IlmiyIsh(models.Model):
    category = models.ForeignKey(Category, related_name='jurnallar', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    profile


    def __str__(self):
        return self.nom
