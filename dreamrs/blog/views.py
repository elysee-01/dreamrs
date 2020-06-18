from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Article, Tag, Commentaire, InstagramFeed, CathegorieArticle
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q



def blog(request, filtre=None, filtre_id=None):
    
    articles = Article.objects.filter(status=True).order_by('-date_update')
    
    if filtre == 'tag':
        articles_all = articles.filter(tag=filtre_id)
    elif filtre == 'cath':
        articles_all = articles.filter(cathegorie_id=filtre_id)
    else:
        articles_all = articles

    _paginator = Paginator(articles_all, 4)
    page = request.GET.get('page')

    tags = Tag.objects.filter(status=True)
    commentaires = Commentaire.objects.filter(status=True)
    instagrams = InstagramFeed.objects.filter(status=True)
    cathegories = CathegorieArticle.objects.filter(status=True)

    try:
        articles_page = _paginator.page(page)
    except PageNotAnInteger:
        articles_page = _paginator.page(1)
    except EmptyPage:
        articles_page = _paginator.page(_paginator.num_pages)


    data = {
        'articles': articles_page,
        'articles_recent': articles[:4],
        'tags': tags,
        'commentaires': commentaires,
        'instagrams': instagrams,
        'cathegories': cathegories,
    }
    
    return render(request, 'pages/blog/blog.html', data)



def single(request, article_id):
    
    article = get_object_or_404(Article, status=True, pk=article_id)
    articles_recent = Article.objects.filter(status=True).order_by('-date_update')[:4]
    tags = Tag.objects.filter(status=True)
    commentaires = Commentaire.objects.filter(status=True)
    instagrams = InstagramFeed.objects.filter(status=True)
    cathegories = CathegorieArticle.objects.filter(status=True)
    
    if request.method == 'POST' and request.POST['comment']:
        if request.user.is_authenticated:
            new_comment = Commentaire.objects.create(
                commentaire=request.POST['comment'], 
                auteur=request.user,
                article=article
            )
            new_comment.save()
        else:
            return redirect('login')
    
    data = {
        'l_article': article,
        'articles_recent': articles_recent,
        'tags': tags,
        'commentaires': commentaires,
        'instagrams': instagrams,
        'cathegories': cathegories,
    }
    
    return render(request, 'pages/blog/single-blog.html', data)



def search(request):
    try:
        request.POST['search']
        assert len(request.POST['search']) >= 2
    except Exception:
        return redirect(request.META.get('HTTP_REFERER', '/'))

    q = request.POST['search']
    articles = Article.objects.filter(status=True)
    articles = articles.filter(Q(titre__icontains=q) | Q(description__icontains=q) | Q(contenu__icontains=q))

    data = {
        'q': q,
        'articles': articles,
        'nombre_resultat': len(articles),
    }
    
    return render(request, 'pages/blog/blog_search.html', data)