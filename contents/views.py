from django.views.generic import TemplateView, RedirectView

from models import Slider, Category, Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['sliders'] = Slider.objects.filter(is_active=True)[:3]
        context['categories'] = Category.objects.filter(is_active=True)

        product_list = Products.objects.all()
        paginator = Paginator(product_list, 10) # Show 25 contacts per page

        page = self.request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            products = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            products = paginator.page(paginator.num_pages)
        context['products'] = products
        context['rec_products'] = Products.objects.all()[:3]
        return context

class ContactView(TemplateView):
    template_name = "contact.html"