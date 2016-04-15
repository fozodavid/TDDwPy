from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
	return render(request, 'home.html')
	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST.get('item_text',''))
	# 	return redirect('/')

	# items = Item.objects.all()
	# return render(request, 'home.html', {'items': items})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text = request.POST.get('item_text',''), list = list_)
	return redirect('/lists/%d/' % (list_.id,))

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	# items = Item.objects.filter(list = list_)
	return render(request, 'list.html', {'list': list_})

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST.get('item_text',''), list = list_)
	return redirect('/lists/%d/' % (list_.id,))

