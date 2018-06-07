from django.shortcuts import render


def index(request):
    """/ トップページ"""
    context = {
        'name': 'Yasuki',
    }
    return render(request, 'myapp/index.html', context)  # index.htmlにcontextを埋め込まれている


def about(request):
    """/about アバウトページ"""
    return render(request, 'myapp/about.html')


def info(request):
    """/info インフォページ"""
    return render(request, 'myapp/info.html')
