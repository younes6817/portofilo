from django.shortcuts import render
from tech_stack.models import TechStack

def home(request):
    tech_stacks = TechStack.objects.all().order_by('-percent')

    return render(request, 'home.html', {
        'tech_stacks': tech_stacks,
    })