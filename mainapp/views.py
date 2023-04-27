from rest_framework.viewsets import ModelViewSet

from mainapp.models import (
    School,Clas,Student,
)

from mainapp.serializers import(
    SchoolSerializer,
)

class SchoolView(ModelViewSet):
    queryset=School.objects.all()
    serializer_class=SchoolSerializer


from mainapp.serializers import(
    ClasSerializer,
)

class ClasView(ModelViewSet):
    queryset=Clas.objects.all()
    serializer_class=ClasSerializer




from mainapp.serializers import(
    StudentSerializer,
)

class StudentView(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer



