from django.db import models

# Create your models here.


class Name(models.Model):
    text = models.CharField(max_length=200)
    # auto_now_add=True - set this attribute to the current date and time
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Topping(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "toppings"

        def __str__(self):
            return f"{self.text[:50]}..."


"""class Comment(models.Model):
    post = models.ForeignKey(Name, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.text
"""
