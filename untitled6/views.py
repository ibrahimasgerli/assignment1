__author__ = 'ibrahimasgerli'
import datetime
now=datetime.datetime.now()
print now

from django.http import HttpResponse

from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context


def word_count(request):
    t=get_template('assignment1.html')
    t=t.render()
    a=t.strip().split()
    b={}
    for word in a:
        if word in b:
            b[word]+=1
        else:
            b[word]=1
    pot=""
    for it,it1 in b.items():
        pot+="<p>%s,%s</p>"%(it,it1)
    html="<html><body>"+"Name: assignment1"+"<p>%s</p>"%("Words:")+pot+"</body></html>"
    return HttpResponse(html)

word_count(7)





