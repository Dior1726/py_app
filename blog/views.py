from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from django.http import HttpResponse
import json


class HomeView(View):
    def get(self, request):
        last_items = News.objects.order_by('-date')[:6]
        ref_subcategories = SubCategory.objects.filter(category_id=1)
        dip_subcategories = SubCategory.objects.filter(category_id=2)
        kur_subcategories = SubCategory.objects.filter(category_id=3)
        context = {
            'last_items': last_items,
            'ref_subcategories': ref_subcategories,
            'dip_subcategories': dip_subcategories,
            'kur_subcategories': kur_subcategories
        }

        return render(request, 'blog/home.html', context)


class SearchView(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        search_items = News.objects.filter(name__icontains=search_query)
        return render(request, 'blog/search.html', {'search_items': search_items})


class SubcategoryNews(View):
    def get(self, request, pk, id):
        category = Category.objects.filter(id=pk)
        sub_category = SubCategory.objects.filter(id=id)
        news = News.objects.filter(category_id=pk, subCategory_id=id)
        context = {
            'news': news,
            'category': category,
            'sub_category': sub_category
        }
        return render(request, 'blog/subcategory.html', context)


def get_sub_category(request):
    pk = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(category_id=int(pk)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

def error_404_view(request, exception):
    return render(request, 'blog/404.html')
