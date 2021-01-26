import django_filters
from .models import Course, Division, Student


class CourseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Course
        fields = ['title']


class DivisionFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Division
        fields = ['title', 'room']


class StudentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Student
        fields = ['name', 'surname', 'grade']