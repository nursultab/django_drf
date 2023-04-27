from rest_framework.routers import DefaultRouter as DR 

from mainapp.views import(
    SchoolView, ClasView, StudentView,
)

router = DR()

router.register('school',SchoolView)
router.register('clas',ClasView)
router.register('student',StudentView)

urlpatterns = []

urlpatterns += router.urls


