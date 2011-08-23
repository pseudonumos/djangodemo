# Create your views here.
from search.models import Result, Voyage
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

def new(request):
    return render_to_response('search/new.html')

def results(request):
    #departure_city = request.GET['departure_city']
    results_list = Result.objects.all()
    print results_list
    for result in results_list:
        print result.voyages
    return render_to_response('search/results.html', {'results_list': results_list})


