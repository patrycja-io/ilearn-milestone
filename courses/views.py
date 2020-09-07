from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Course, Category
from .forms import CourseForm


def all_courses(request):
    """ A view to show all products, including sorting and search queries """
    courses = Course.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                courses = courses.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            courses = courses.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            courses = courses.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('courses'))

            queries = Q(name__icontains=query)
            courses = courses.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'courses': courses,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,

    }
    return render(request, 'courses/courses.html', context)


def course_description(request, course_id):
    """ A view to show individual course details """

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_description.html', context)

@login_required
def add_course(request):
    """ Add a course to the platform """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only creator can do it!.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Added new course!')
            return redirect(reverse('course_description', args=[course.id]))
        else:
            messages.error(request, 'Failed to add course. Please ensure the form is valid.')
    else:
        form = CourseForm()
        
    template = 'courses/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_course(request, course_id):
    """ Edit a course in the platform """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only course creator can do that.')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated course!')
            return redirect(reverse('course_description', args=[course.id]))
        else:
            messages.error(request, 'Failed to update the course. Please ensure the form is valid.')
    else:
        form = CourseForm(instance=course)
        messages.info(request, f'You are editing {course.name}')

    template = 'courses/edit_course.html'
    context = {
        'form': form,
        'course': course,
    }

    return render(request, template, context)

@login_required
def delete_course(request, course_id):
    """ Delete a course from the platform """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only course creator can do that.')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    messages.danger(request, 'Course deleted!')
    return redirect(reverse('courses'))
    
