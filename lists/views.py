from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
	return render(request, 'home.html')
	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST.get('item_text',''))
	# 	return redirect('/')

	# items = Item.objects.all()
	# return render(request, 'home.html', {'items': items})

def new_list(request):
	Item.objects.create(text=request.POST.get('item_text',''))
	return redirect('/lists/the-only-list-in-the-world/')