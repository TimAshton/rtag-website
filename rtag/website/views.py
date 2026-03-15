from django.shortcuts import render


def home(req):
    return render(req, 'home/root.html')


def about(req):
    return render(req, 'about/root.html')


def rules(req):
    return render(req, 'rules/root.html')
