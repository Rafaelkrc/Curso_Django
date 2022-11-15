from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': '770651906?h=511e20b27b&amp'}
    return render(request, 'aperitivos/video.html', context={'video': video})
