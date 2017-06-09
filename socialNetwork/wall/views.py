# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.template import loader
from django.http import HttpResponse
from .models import user, post

class current_user:
	def __init__(self):
		self.user=user(user_name="dummy.")

	def set_user(self, obj):
		self.user=obj

	def current_user(self):
		return self.user 

cu=current_user()

def index(request):
    posts=tuple(post.objects.all())
    t=loader.get_template('wall/index.html')
    context={
        'posts':posts,
    }
    return HttpResponse(t.render(context, request))

def user_wall(request, user_name):
	users=tuple(user.objects.all())
	for u in users:
		if u.user_name==user_name:
			break
	return render(request, 'wall/user_wall.html', {'username':user_name, 'posts': tuple(u.post_set.all()) } )


def login(request):
	return render(request, 'wall/login.html', {})


def logInHandler(request):
	un=request.POST['name']
	pw=request.POST['password']

	users=tuple(user.objects.all())
	found=False	
	for user in users:
		if user.user_name==un:
			if user.pass_word==pw:
				found=True
				break

	print user 
	print '\n\n'
	cu.set_user(user)

	return render(request, 'wall/index.html', { 'posts': tuple(post.objects.all()) })
	
	

def signup(request):
	return render(request, 'wall/signup.html', {} )

def signUpHandler(request):
	un=request.POST['name']
	pw=request.POST['password']
	
	u=user(user_name=un, pass_word=pw)
	u.save()

	login(request)

def movie(request):
	movie_title=request.POST['movie']
	import bs4
	import urllib2
	from bs4 import BeautifulSoup
	movielist=[]
	page=urllib2.urlopen('http://www.imdb.com/india/top-rated-indian-movies?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2730173942&pf_rd_r=15KNX5D64SZDZ13Y5NYN&pf_rd_s=right-4&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_india_tr_rhs_1').read()
	soup=BeautifulSoup(page,"lxml")
	rows=soup.tbody.find_all('tr')
	for r in rows:
		cell=r.find_all('td')
		span_tag=cell[1].span.text.strip()
		a_tag=cell[1].a.text.strip()
		a_tag2=cell[2].text.strip()
		print a_tag
		print span_tag 
		print a_tag2
		movielist=movielist+[a_tag,span_tag,a_tag2]
	context={'movielist':movielist,'movie_title':movie_title}
	return render(request, 'wall/movie.html',context)	
		
