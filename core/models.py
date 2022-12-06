from django.db import models

class School(models.Model):
    name=models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=10)
    def __str__(self) :
        return self.title

class Department(models.Model):
    name = models.CharField(max_length=150)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    def __str__(self) :
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=50)
    date_of_joining = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=50)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self) :
        return self.name