from django.shortcuts import render

# Create your views here.
def test(request):
    course={"courses":["English", "Python", "Java", "CSS"]}
    return render(request, 'core/index.html', course)
