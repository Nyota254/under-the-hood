from django.shortcuts import render

def index_view(request):
    '''
    Will render the home page
    '''
    context = {
        "title":"Home"
    }
    return render(request,'main/index.html',context)
