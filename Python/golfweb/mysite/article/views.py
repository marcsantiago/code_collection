from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
# Create your views here.

#1 way
def hello(request):
	name = 'Marc'
	html = "<html><body>Hi %s, this seems to worked!</body></html>" % name
	return HttpResponse(html)

#2 way
def hello_template(request):
	name = 'Marc'
	t = get_template('hello.html')
	html = t.render(Context({'name': name}))
	return HttpResponse(html)

#3 way
def hello_template_simple(request):
	name = "Marc"
	return render_to_response('hello.html', {'name': name})

#4 way
class HelloTemplate(TemplateView):
	template_name = 'hello_class_view.html'

	def get_context_data(self, **kwargs):
		context = super(HelloTemplate, self).get_context_data(**kwargs)
		context['name'] = 'Marc'
		return context