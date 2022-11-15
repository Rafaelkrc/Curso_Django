from django.shortcuts import render

videos = [
    {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': '770651906?h=511e20b27b&amp'},
    {'slug': 'comemoracao', 'titulo': 'Comemoração', 'vimeo_id': '771135617?h=f0b1ac0ee3&amp'}
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
