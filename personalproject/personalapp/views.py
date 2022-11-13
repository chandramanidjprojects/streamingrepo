from django.shortcuts import render,redirect
from . forms import UserForm
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from . models import Post,PostLike,Comment
from django.utils import timezone
def wellcomepage(request):
    if request.user.is_authenticated:
        posts=Post.objects.order_by('-date_time') 
        return  render(request ,'personalapp/posts.html',{'posts':posts})
    user_form=UserForm    
    if request.method=='POST':
        form=user_form(request.POST)
        if form.is_valid():
            f=form.save()
            f.set_password(f.password)
            f.save()
            return redirect('/accounts/login')
    return render(request,'personalapp/wellcome.html',{'user_form':user_form})

def update_profile(request):
    if request.method=='POST':
        request.user.profile=request.FILES.get('pickimage')
        request.user.save()
        return redirect('/')
    return render(request,'personalapp/updateprofile.html')

def likes(request):
  if request.method=='GET':  
    post=Post.objects.get(id=request.GET.get('post_id'))
    if int(post.post_by.id) != int(request.user.id):
       likes=post.post_like.filter(like_by=request.user.id)

       if likes.exists():
          post.post_like.filter(like_by=request.user.id).delete()
          count=post.post_like.all().count()        
       else:
          post.post_like.create(like_by=request.user.id)
          count=post.post_like.all().count()        
       return JsonResponse({'count':count})
    count=post.post_like.all().count()   
    return JsonResponse({'count':count})       
def post_comments(request,id=None):

    if id is None:
       if request.method=='POST':
         
         return JsonResponse({'text':request.POST.get('text'),'profile':request.user.profile.url,'username':request.user.username})

    post=Post.objects.get(id=id)
    comments=Comment.objects.filter(comment_to=post)
    return render(request,'personalapp/post_comments.html',{'comments':comments,'post_id':id})

def create_post(request):
    if request.method=='POST':
        Post.objects.create(post_by=request.user,file=request.FILES.get('pickpost'),date_time=timezone.now())
        print(request.FILES.get('pickpost'))
        return redirect('/')
    return render(request,'personalapp/create_post.html')

