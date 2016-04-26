from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from lists.models import Item, List
from lists.forms import ItemForm

# Create your views here.
def home_page(request):
	return render(request, 'home.html', {'form': ItemForm()})
	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST.get('text',''))
	# 	return redirect('/')

	# items = Item.objects.all()
	# return render(request, 'home.html', {'items': items})

def new_list(request):
	form = ItemForm(data=request.POST)
	if form.is_valid():
		list_ = List.objects.create()
		Item.objects.create(text=request.POST['text'], list=list_)
		return redirect(list_)
	else:
		return render(request, 'home.html', {"form": form})

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	form  = ItemForm()
	if request.method == 'POST':
		form = ItemForm(data=request.POST)
		if form.is_valid():
			form.save(for_list=list_)
			return redirect(list_)
	return render(request, 'list.html', {'list': list_, "form": form})