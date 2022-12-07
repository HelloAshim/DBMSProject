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

class Programme(models.Model):
    name=models.CharField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self) :
        return self.name
class Course(models.Model):
    name=models.CharField(max_length=50)
    credit=models.PositiveIntegerField()
    programme=models.ForeignKey(Programme,on_delete=models.CASCADE)

    def __str__(self) :
        return self.name
class Question(models.Model):
    description=models.CharField(max_length=50)
    defficulty_level=models.CharField(max_length=50)
    blooms_id=models.CharField(max_length=50)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)


class Section(models.Model):
    sec_num=models.CharField(max_length=50)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    semester=models.CharField(max_length=50)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    def __str__(self) :
        return self.sec_num

class CourseOutline(models.Model):
    description=models.CharField(max_length=50)
    policy=models.CharField(max_length=50)
    lesson_plan=models.CharField(max_length=50)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    section=models.ForeignKey(Section,on_delete=models.CASCADE)

class PLO(models.Model):
    plo_num=models.PositiveIntegerField()
    description=models.CharField(max_length=50)
    programme=models.ForeignKey(Programme,on_delete=models.CASCADE)
    def __str__(self) :
        return self.plo_num


class CO(models.Model):
    co_num=models.PositiveIntegerField()
    description=models.CharField(max_length=50)
    plo=models.ForeignKey(PLO,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self) :
        return self.co_num


class Evaluation(models.Model):
    achieved_marks=models.PositiveBigIntegerField()
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    enrollment=models.PositiveBigIntegerField()
    def __str__(self) :
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    email=models.CharField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    programme= models.ForeignKey(Programme,on_delete=models.CASCADE)
    def __str__(self) :
        return self.name

class Enrollment(models.Model):
    sementer=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    student_num=models.IntegerField()
    section=models.ForeignKey(Section,on_delete=models.CASCADE)
    def __str__(self) :
        return self.name
