from django.shortcuts import render
from .models import Order
from cms.models import CmsSlider
from .forms import OrderForm
from price.models import PriceCard, PriceTable


def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'form': form,
                }

    return render(request, './index.html', dict_obj)


def thanks_page(request):
    name = request.GET['name']
    phone = request.GET['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, './thanks_page.html', {'name': name,})

# Create your views here.
