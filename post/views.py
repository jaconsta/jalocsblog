from django.shortcuts import render, get_object_or_404

from .models import Post, Categories

def showGeneralResume(request):
    def mixCategAndPosts(cat):
        combined = []
        for i in cat:
            combined.append ( {'categ': i, 'posts': Post.objects.RecentPost(i)[:6]})
        return combined

    cat = Categories.main_objects.all();
    posts = mixCategAndPosts(cat)

    return render(request, 'post/main.html', {'categories': cat, 'posts':posts})

def getCategoryResume(request, category, page = 1):
    
    categ = get_object_or_404(Categories, name = category)
    posts = Post.objects.RecentPost(categ)[((page-1)*6):(page*6)]
    return render(request, 'post/categories.html', {'categories':Categories.main_objects.all(), 'category':categ, 'posts':posts})

def getPostContent(request, category, post_id):
    categ = get_object_or_404(Categories, name = category) #Verify that the category exists
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/post.html', {'categories':Categories.main_objects.all(), 'category':categ,'post':post, })
