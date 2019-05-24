from django.shortcuts import render, redirect, get_object_or_404
from project.models import Card, Taro
# Create your views here.
def home(request):
    return render(request,'home.html')

def card(request):
    switch=0
    cards = Card.objects
    for card in cards.all():
        switch += card.select
    return render(request, 'card.html',{'cards':cards,'switch':switch})

def click(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    card.select += 1
   
    card.order = request.GET['card_order']
    card.save()
    return redirect('/card')

def rank(request):
    taros=Taro.objects.all()
    a = -100
    for item in taros:
        if (a < item.num):
            a=item.num

    for item in taros:
        if (a==item.num):
            first=item        

    
    li=[]
    for item in taros:
        i=0
        li.insert(i,item.num)

    li = list(set(li))    
    li.sort()
    li.reverse()
    return render(request,'rank.html', {'taros' : taros,'li' : li , 'first' : first}) 

def submit(request):
    cards = Card.objects
    taros=Taro.objects
    idd=0
    for t in taros.all():
        idd=t.id
    for t in taros.all():
        if(t.id==idd):
           taro=t 

    
    taro.num = 0
    taro.content = ''
    for card in cards.all():
        if card.order == 0:

            taro.content += card.mean1
            taro.num += card.score1
        if card.order == 1:
            taro.content += card.mean2
            taro.num += card.score2
    taro.save()
    return render(request,'submit.html',{'taro' : taro})

def Add(request):
    taro = Taro()
    taro.name = request.GET['user_name']
    taro.num=0
    taro.content=''
    taro.save()
    cards = Card.objects
    for card in cards.all():
        card.select = 0
        card.order = 1000
        card.save()

    return redirect('/card')

def reset(request):
    cards = Card.objects
    for card in cards.all():
        card.select = 0
        card.order = 1000
        card.save()
    
    return redirect('/')