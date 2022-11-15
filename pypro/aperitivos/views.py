from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': '770651906?h=511e20b27b&amp'},
        'comemoracao': {'titulo': 'Comemoração', 'vimeo_id': '771135617?h=f0b1ac0ee3&amp'}
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
