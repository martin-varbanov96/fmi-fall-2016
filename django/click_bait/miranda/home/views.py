from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader
from django.views.generic import ListView

class IndexView(ListView):
	def get(self, request):
		template_name = 'home/blog.html'
		return render(request, template_name) 		