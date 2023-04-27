from  rest_framework import serializers

from mainapp.models import(
    School,Clas,Student,
)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=(
           'id','student_name','grade_1',
        )



class ClasSerializer(serializers.ModelSerializer):
    students=StudentSerializer(read_only=True,many=True)
    # school_name=serializers.ReadOnlyField(source='school.name')
    class Meta:
        model = Clas
        fields=(
           'id', 'room_number','teacher_name','grade','school','students' , 'student_amount',
            
)

class SchoolSerializer(serializers.ModelSerializer):
    classes=ClasSerializer(read_only=True,many=True)
    class Meta:
        model =School
        fields=(
            'id','name','number','address','classes' , 'clas_amount',
        )







    
