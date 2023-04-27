from django.db import models



class School(models.Model):
    name = models.CharField(max_length=127)
    number = models.PositiveIntegerField(default=1)
    address = models.CharField(max_length=127)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'

    def __str__(self):
        return f'Школа {self.name} номер {self.number}'
    
    @property
    def clas_amount(self):
        return self.classes.count()


class Clas(models.Model):
    room_number = models.PositiveIntegerField(default=1)
    teacher_name = models.CharField(max_length=127)
    student_amount = models.PositiveIntegerField(default=1)
    grade = models.CharField(max_length=127)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE,null=True,
          related_name='claases'
          )

    


    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


    def __str__(self):
        return f'{self.grade} класс в школе '
    

class Student(models.Model):
    student_name = models.CharField(max_length=127)
    grade_1 = models.CharField(max_length=129)
    clas = models.ForeignKey(
        Clas, on_delete=models.CASCADE,null=True ,
        related_name='students'
        )


    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студента'




    def __str__(self):
        return f'{self.student_name},{self.grade_1}'