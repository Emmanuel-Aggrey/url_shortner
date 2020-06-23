from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect, render,get_object_or_404,HttpResponse
from django.views.generic import DetailView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView
from rest_framework import generics
from .serializers import LinkSerializers,ShortToLongUrlSerializer
from django.http import  JsonResponse
from django.urls import  reverse_lazy
from .models import Link

# Create your views here.

class ShortUrlApi(generics.RetrieveAPIView):

    serializer_class = LinkSerializers
    queryset = Link.objects.all()
    # lookup_field = 'id'

    def get(self, request, pk=None):
        if pk:
            # return pk,original_url,shortened_url
            return self.retrieve(request, pk)

class ShortToLongUrlSerializer(generics.RetrieveAPIView):

    serializer_class = ShortToLongUrlSerializer
    queryset = Link.objects.all()
    lookup_field = 'hash_id'

    def get(self, request, hash_id=None):
        if hash_id:
            # return original_url,shortened_url
            return self.retrieve(request, hash_id)
    

class LinkCreate(CreateView):
    model = Link
    fields = ["original_url"]
    def form_valid(self, form):

        return super(LinkCreate, self).form_valid(form)
    

    def get_context_data(self, **kwargs):
        context = super(LinkCreate, self).get_context_data(**kwargs)
        # Passing link_list to display 5 objects
        context['link_list'] = Link.objects.all().order_by('-id')[:3]
        context['short_to_full'] = Link.objects.all().order_by('-id')[0]

        # Passing site_url to display domain base
        context['site_url'] = settings.SITE_URL
        return context

def detailpage(request,pk):
    link = get_object_or_404(Link,pk=pk)
    # return json of newly created data
    return JsonResponse({'id':link.id,'shortended url':link.shortened_url})


# redirecting shortend url to full
class RedirectToLongURL(RedirectView):
    
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        short_url = kwargs["short_url"]
        return Link.encode(short_url)



def error404(request, exception):
    context = {
        'date': 'IT LOOKS LIKE YOU\'R MISSING',
    }
    return render(request, 'error_pages/404.html', context)


def error500(request):

    return render(request, 'error_pages/500.html')
