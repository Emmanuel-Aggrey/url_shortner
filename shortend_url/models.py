from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from hashids import Hashids
hashids = Hashids()


# Create your models here.

class Link(models.Model):
    original_url = models.URLField('url',unique=True)
    hash_id = models.CharField(max_length=10, blank=True,editable=False)
    shortened_url = models.URLField(blank=True,editable=False)

    def get_absolute_url(self):
        return reverse("detailpage", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        link = Link.objects.values_list('pk', flat=True).last()
        # print('link',link)
        dirty_str = str(hashids.encode(link))
        self.hash_id = dirty_str
        self.shortened_url = 'https://shortner-url1.herokuapp.com/'+dirty_str
        return super().save(*args, **kwargs)


#     # Encodes Url to a short url
    @staticmethod
    def shorten(link):
        l, _ = Link.objects.get_or_create(original_url=link.original_url)
       
        # using library to encrypt id
        return str(hashids.encode(l.pk))

# #     # Decodes short url to original url
    @staticmethod
    def expand(original_url):
        # Decrypting slug and getting '(12,)'
        dirty_str = str(hashids.decode(original_url))
        # stripping out '(,)'
        clean_id = dirty_str.strip('(,)')
        # now converting '12' into 12
        link_id = int(clean_id)
        l = Link.objects.get(pk=link_id)
        return l.original_url

    @property
    def short_url(self):
        return reverse("redirect_short_url",
                       kwargs={"short_url": Link.shorten(self)})

    def __str__(self):
        return self.original_url
