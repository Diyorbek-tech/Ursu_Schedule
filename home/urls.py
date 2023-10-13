from django.urls import path

from .views import *

urlpatterns = [
    path('', homeview, name='home'),
    path('schedule/', facultiesview, name='faculties'),
    path('schedule/<int:parent>/', coursesview, name='kurs'),
    path('schedule/<int:deportment>/<int:year>/', curriculumview, name='curriculum'),
    path('schedule/<int:deportment>/<int:year>/<int:group>/', scheduleview, name='schedule'),


    # path('<int:id>/<int:cur>/', coursesview, name='groups'),
]
