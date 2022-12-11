from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

languages = {
    'python':'Hi, This is the python programming page.',
    'php':'Hi, This is the PHP programming page.',
    'c++':'Hi, This is the C++ programming page.',
    'javascript':'Hi, This is the JavaScript programming page.'
}

def language_page(request,topic):
    result = languages[topic]
    return HttpResponse(result)

def number_view(request,page_n):
    language_list_keys = list(languages.keys()) #language_list_keys = ['python','php','c++','javascript']
    result = language_list_keys[page_n]
    return HttpResponseRedirect(reverse('language_page', args=(result,)))