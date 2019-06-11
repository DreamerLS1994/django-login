from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.shortcuts import get_object_or_404


# Create your views here.


def index_view(request):

    return render(request, 'team/index.html')

