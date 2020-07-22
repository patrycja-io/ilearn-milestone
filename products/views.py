from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Course, Category


def courses_all(request):
    """ A view to show all products, including sorting and search queries """
    courses = Course.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            courses = courses.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('courses'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            courses = courses.filter(queries)

    context = {
        'courses': courses,
        'search_term': query,
        'current_categories': categories,
    }
    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    """ A view to show individual course details """

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_detail.html', context)
    
