from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect, render,get_list_or_404
from django.views.generic import DetailView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView

from .models import Link

# Create your views here.


class LinkCreate(CreateView):
    model = Link
    fields = ["url"]

    def form_valid(self, form):
        prev = Link.objects.filter(url=form.instance.url)
        if prev:
            return redirect("link_show", pk=prev[0].pk)
        return super(LinkCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LinkCreate, self).get_context_data(**kwargs)
        # Passing link_list to display original and short_url in link_form.html
        context['link_list'] = Link.objects.all().order_by('-id')[:10]
        # Passing site_url to display domain base
        context['site_url'] = settings.SITE_URL
        return context


class LinkShow(DetailView):
    model = Link
    # A base view for displaying a single object."""

    def get_context_data(self, **kwargs):
        context = super(LinkShow, self).get_context_data(**kwargs)
        context['site_url'] = settings.SITE_URL
        return context

class RedirectToLongURL(RedirectView):
    
    permanent = False
    

    def get_redirect_url(self, *args, **kwargs):
        short_url = kwargs["short_url"]
        return Link.expand(short_url)




def error404(request, exception):
    context = {
        'date': 'IT LOOKS LIKE YOU\'R MISSING',
    }
    return render(request, 'error_pages/404.html', context)


def error500(request):

    return render(request, 'error_pages/500.html')