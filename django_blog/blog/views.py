from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm 
from django.contrib.auth import login
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView, ListView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
         form = RegisterForm(request.POST)
         if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')	
         else:
             messages.error(request, 'Error updating profile') 
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def UserProfile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
        profile.save()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile) 
        
    return render(request, 'profile.html', {'form': form})

class DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('movie_reviews')

    def test_func(self):
        review = self.get_object()
        return review.user == self.request.user
    
class UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'

    def test_func(self):
        review = self.get_object()
        return review.user == self.request.user
    
class DetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'review'

class CreateView(CreateView):
    model =Post
    form_class = PostForm
    template_name = 'create_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'reviews'

class UpdateComment(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'update_comments.html'

    def test_func(self):
        review = self.get_object()
        return review.user == self.request.user


class DetailComment(DetailView):
    model = Comment
    template_name = 'detail_comments.html'
    
    def get_context_data (self, **kwaargs): #this overides get_context_data
        context = super().get_context_data(**kwaargs)
        context['comment_form'] = CommentForm()
        context['comments']= self.object.comments.all()
        return context 

class CreateComment(CreateView):
    model =Comment
    form_class = CommentForm
    template_name = 'create_comments.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ListComment(ListView):
    model = Comment
    template_name = 'list_comments.html'
    context_object_name = 'reviews'
