from pathlib import Path

from django.conf import settings
from django.shortcuts import render
from tech_stack.models import TechStack


def home(request):
    tech_stacks = TechStack.objects.all().order_by('-percent')

    # Cache-busting version for the hero photo. The file name never changes when
    # the image is replaced, so mobile browsers keep serving the old cached copy.
    # Using the file mtime makes the URL change whenever the image is swapped.
    hero_image = Path(settings.MEDIA_ROOT) / 'younes.webp'
    try:
        hero_version = int(hero_image.stat().st_mtime)
    except OSError:
        hero_version = 1

    return render(request, 'home.html', {
        'tech_stacks': tech_stacks,
        'hero_version': hero_version,
    })