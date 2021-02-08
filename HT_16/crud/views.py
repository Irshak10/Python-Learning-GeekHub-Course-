from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from crud.models import Crud, Tag
from crud.forms import CrudCreateForm


def main_menu(request):
    context = {'Products': Crud.objects.filter(activation=True)}
    return render(request, 'crud/allproducts.html', context)


def single_product(request, single_id):
    try:
        a = Crud.objects.get(id=single_id)
    except:
        raise Http404('Product is not finded')
    action = request.POST.get('action')

    if request.POST and action == 'delete':
        Crud.objects.filter(id=single_id).delete()
        return redirect(reverse('main_menu'))

    if request.POST and action == 'deactivate':
        Crud.objects.filter(id=single_id).update(activation=False)
        return redirect(reverse('single_product', args=(single_id,)))

    if request.POST and action == 'activate':
        Crud.objects.filter(id=single_id).update(activation=True)
        return redirect(reverse('single_product', args=(single_id,)))

    if request.POST and action == 'add to cart':
        cart_in_product = request.session.get('cart_in_product', {})
        one_product = Crud.objects.values().get(id=single_id)
        wanted_quantity = int(request.POST['qotap'])
        if one_product['quantity'] < wanted_quantity:
            messages.add_message(request, messages.INFO, f'Not enough quantity')
        else:
            one_product['added_qotap'] = wanted_quantity
            cart_in_product[str(single_id)] = one_product
            request.session['cart_in_product'] = cart_in_product
            messages.add_message(request, messages.INFO, f'The product is added to the cart')

    latest_10_comments = a.comment_set.order_by('-id')[:10]
    return render(request, 'crud/single_product.html', {'single_product': a, 'latest_10_comments': latest_10_comments})


def leave_comment(request, single_id):
    try:
        a = Crud.objects.get(id=single_id)
    except:
        raise Http404('Product is not finded')

    a.comment_set.create(comment_text=request.POST['text_comment'])
    return HttpResponseRedirect(reverse('single_product', args=(a.id,)))


def creating_product(request):
    form = CrudCreateForm(request.POST or None)
    if form.is_valid():
        created_product = form.save(commit=True)
        return redirect(reverse('single_product', args=(created_product.id,)))

    context = {'form': form}
    return render(request, 'crud/creating_product.html', context)


def cart(request):
    action = request.POST.get('action')
    cart_in_cart = request.session.get('cart_in_product', {})
    if request.POST and action == 'delete':
        del cart_in_cart[request.POST['single_id']]
        request.session['cart_in_product'] = cart_in_cart

    if request.POST and action == '+':
        cart_plus = cart_in_cart[str(request.POST['single_id'])]
        if cart_plus['quantity'] < cart_plus['added_qotap'] + 1:
            messages.add_message(request, messages.INFO, f'Not enough quantity')
        else:
            cart_plus['added_qotap'] += 1
            request.session['cart_in_product'] = cart_in_cart
            messages.add_message(request, messages.INFO, f'Quantity is updated: +1 ')

    if request.POST and action == '-':
        cart_minus = cart_in_cart[str(request.POST['single_id'])]
        if cart_minus['added_qotap'] < 1:
            messages.add_message(request, messages.INFO, f'Quantity is NULL')
            del cart_in_cart[request.POST['single_id']]
            request.session['cart_in_product'] = cart_in_cart
        else:
            cart_minus['added_qotap'] -= 1
            request.session['cart_in_product'] = cart_in_cart
            messages.add_message(request, messages.INFO, f'Quantity is updated: -1')

    if request.POST and action == 'update':
        update_cart = cart_in_cart[str(request.POST['single_id'])]
        wanted_quantity = int(request.POST['qotap'])
        update_cart['added_qotap'] = wanted_quantity
        request.session['cart_in_product'] = cart_in_cart

    return render(request, 'crud/cart.html')


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'crud/tags_list.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'crud/tag_detail.html', context={'tag': tag})