from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from images.forms import ImageCreateForm

# Create your views here.
@login_required
def image_create(request):
    if request.method == 'POST':
        pass
    else:
        form = ImageCreateForm(data=request.GET)
    return render('images/image/create.html', {'section':'images', 'form':form})