from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Member, Timeline, Committee, Homepic
from django.contrib.auth.mixins import LoginRequiredMixin
def home(request):
    homepics = Homepic.objects.all()
    count = Homepic.objects.count()

    context = {
        'homepics': homepics, 'count': range(count)
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def gallery(request):
    posts = Post.objects.all()
    timelines = Timeline.objects.all()
    homepics = Homepic.objects.all()

    context = {
        'posts': posts,
        'timelines': timelines,
        'homepics': homepics,
        'title': 'Gallery'
    }
    return render(request, 'blog/gallery.html', context)


def timeline(request):
    return render(request, 'blog/timeline.html', {'title': 'Timeline'})


class TimelineListView(ListView):
    model = Timeline
    template_name = 'blog/timeline.html'
    context_object_name = 'timelines'
    ordering = ['-year']


class MemberListView(ListView):
    template_name = 'blog/members.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Member.objects.all()
        queryset1 = Committee.objects.all().first()
        return [queryset, queryset1]

    def get_context_data(self, *args, **kwargs):
        members = Member.objects.all().order_by('name')
        committee = Committee.objects.all().first()

        context = {
            'members': members,
            'committee': committee
        }

        return context


class MemberDetailView(DetailView):
    model = Member


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url='/admin/login/?next=/admin/'
    model = Post
    fields = '__all__'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url='/admin/login/?next=/admin/'
    model = Post
    fields = '__all__'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url='/admin/login/?next=/admin/'
    model = Post
    success_url = '/'
    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False
