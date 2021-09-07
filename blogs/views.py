from blogs.forms import Createnewpost
from django.shortcuts import render,redirect
from .models import Blogs, static_data
# import pyrebase
from .forms import Createnewpost

# config = {
#     'apiKey': "AIzaSyC3FA81julOAziBf1hV3l3NKVgwfCHMzm0",
#     'authDomain': "blogger-app-8f6fc.firebaseapp.com",
#     'databaseURL': "https://blogger-app-8f6fc-default-rtdb.asia-southeast1.firebasedatabase.app",
#     'projectId': "blogger-app-8f6fc",
#     'storageBucket': "blogger-app-8f6fc.appspot.com",
#     'messagingSenderId': "90482352838",
#     'appId': "1:90482352838:web:31ded5451c1d6a1a072dc7",
#     'measurementId': "G-QC68WZHH9H"
# }
# firebase = pyrebase.initialize_app(config)
# authe = firebase.auth()
# database = firebase.database()

# Create your views here.
def homepage(request):
    blogs = Blogs.objects.all()
    # db = database.child('blogs').get().val()
    background = static_data.objects.all()
    for i in background:
        bg = i.background

    context={'blogs':blogs,'background':bg}
    return render(request,'index.html',context)

def posts(request):
    blogs = Blogs.objects.all()
    # db = database.child('blogs').get().val()

    background = static_data.objects.all()
    for i in background:
        bg = i.background

    context={'blogs':blogs,'background':bg}
    return render(request,'posts.html',context)

def show_post(request,id):
    post = Blogs.objects.get(id=id)

    bg = post.article_banner
    context={'post':post,'background':bg}

    return render(request,'post.html',context)

def create_post(request):
    form = Createnewpost()
    background = static_data.objects.all()
    for i in background:
        bg = i.background
    context={'form':form,'background':bg}
    if request.method=='POST':
        form = Createnewpost(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('')
        # else:
        #     messages.error(request, 'Try again with different details')
        #     context={'form':form}
        #     return render(request,'signup.html',context)
    return render(request,'create_post.html',context)
