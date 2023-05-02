from rest_framework import serializers

from mainapp.models import(
    School, Clas, Student
)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id', 'first_name', 'last_name',
            'age', 'gender', 'clas',
)


class ClasSerializer(serializers.ModelSerializer):
    # school_name = serializers.ReadOnlyField(source='school.name') 
    studens = StudentSerializer(read_only=True, many=True)       
    class Meta:
        model = Clas
        fields = (
            'student_amount',
            'id', 'room_number', 'teacher_name',
            'student_amount', 'grade', 'school', 'studens', # shcool_name',
)


class SchoolSerializer(serializers.ModelSerializer):
    classes = ClasSerializer(read_only=True, many=True)
    class Meta:
        model = School
        fields = (
            'clas_amount',
            'id', 'name', 'number', 'address', 'classes',
)