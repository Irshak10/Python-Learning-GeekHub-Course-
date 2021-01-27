from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from crud.models import Crud
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

    if request.POST and action == 'main menu':
        return redirect(reverse('main_menu'))

    if request.POST and action == 'delete':
        Crud.objects.filter(id=single_id).delete()
        return redirect(reverse('main_menu'))

    if request.POST and action == 'deactivate':
        Crud.objects.filter(id=single_id).update(activation=False)
        return redirect(reverse('single_product', args=(single_id, )))

    if request.POST and action == 'activate':
        Crud.objects.filter(id=single_id).update(activation=True)
        return redirect(reverse('single_product', args=(single_id, )))

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
        return redirect(reverse('single_product', args=(created_product.id, )))

    context = {'form': form}
    return render(request, 'crud/creating_product.html', context)

