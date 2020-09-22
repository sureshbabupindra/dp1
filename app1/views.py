from django.shortcuts import render
#1 from django.http import HttpResponse

def home(request):
	#1 return HttpResponse('<h1>Blog-Home<h1>')
	return render(request, 'blog/home.html') #rot to blog folder in templates and then home.html


def about(request):
	#1 return HttpResponse('<h1>Blog-About<h1>')
	return render(request, 'blog/about.html')
