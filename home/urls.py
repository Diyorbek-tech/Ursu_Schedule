from django.urls import path

from .views import *

urlpatterns = [
    path('', homeview, name='home'),
    path('<int:parent>/', coursesview, name='kurs'),
    path('<int:deportment>/<int:year>/', curriculumview, name='curriculum'),
    path('<int:deportment>/<int:year>/<int:group>/', scheduleview, name='schedule'),


    # path('<int:id>/<int:cur>/', coursesview, name='groups'),
]
