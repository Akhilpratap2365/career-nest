from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from datetime import date
from django.db.models import Q
# Create your views here.
def index(request):
    if request.method=="POST":
      Name=request.POST.get("name")
      Mobile=request.POST.get("mob")
      Email=request.POST.get("email")
      Message=request.POST.get("msg")
      tblcontact(name=Name,email=Email,mobile=Mobile,message=Message).save()
      return HttpResponse("<script>alert('Data Saved Successfully');location.href='/index/'</script>")

    return render (request,"index.html")
def about(request):
    return render (request,"about.html")
def team(request):
    data=tblteam.objects.all()
    d={"tem":data}
    return render (request,"team.html",d)
def gallery(request):
    data=tblgallery.objects.all()
    d={"gal":data}
    
    return render (request,"gallery.html",d)
def category(request):
    return render (request,"category.html")
def services(request):
    return render (request,"services.html")
def job(request):
    return render (request,"joblisting.html")

def details(request):
    a=request.GET.get('jid')
    if a:
        job=tbljob.objects.filter(id=a)
    else:
        return HttpResponse("<script>alert('Please select a job');location.href='/alljobs/'</script>")
    dic={"job":job}
    return render (request,"jobdetails.html",dic)

def contact(request):
    return render(request,"contact.html")

def jobs(request):
    skill=request.POST.get("skill")
    location=request.POST.get("location")
    exp=request.POST.get("exp")
    
    cat=tblcategory.objects.all()
    cid=request.GET.get('cid')
    if cid : 
    
        job=tbljob.objects.select_related('company').filter(category=cid).order_by('-id')[0:10]
    elif exp:
        job=tbljob.objects.select_related('company').filter(Q(exp__icontains=exp) & Q(skills__icontains=skill) & Q(city__name__icontains=location))
    else: 
        job=tbljob.objects.select_related('company').filter(active=True).order_by('-id')[0:10]
    data={"cat":cat,"job":job}
    return render(request,"jobs.html",data)


def company(request):
    cat=tblcategory.objects.all()
    mnc=tblcompany.objects.filter(type='MNC').order_by('-id')
    paid=tblcompany.objects.filter(ispaid=True).order_by('-id')
    all=tblcompany.objects.all().order_by('-id')
    dic={"cat":cat,"mnc":mnc,"paid":paid,"all":all}
    return render(request,"company.html",dic)


def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        mob=request.POST.get('mob')
        quali=request.POST.get('qualification')
        exp=request.POST.get('exp')
        company=request.POST.get('company')
        salary=request.POST.get('salary')
        esalary=request.POST.get('esalary')
        resume=request.FILES.get('resume')
        profile=request.FILES.get('profile')
        tblseeker(name=name,email=email,mobile=mob,password=password,qualification=quali,exp=exp,company=company,resume=resume,salary=salary,esalary=esalary,picture=profile,regdate=date.today()).save()
        return HttpResponse("<script>alert('Welcome to naukri portal.Now you explore jobs');location.href='/ulogin/'</script>")
        
    return render(request,"register.html")
def ulogin(request):
    if request.method=="POST":
       email=request.POST.get("email")
       password=request.POST.get("passwd")
       x=tblseeker.objects.all().filter(email=email,password=password)
       if x.count()==1:
          request.session["name"]=str(x[0].name)
          request.session["picture"]=str(x[0].picture)
          request.session["email"]=email
          return HttpResponse("<script>location.href='/jobs/'</script>")
       else:
          return HttpResponse("<script>alert('Your Email Id or Password is Incorrect..');location.href='/ulogin/'</script>")
    return render(request,"userlogin.html")
def elogin(request):
    return render(request,"employeerlogin.html")
def profile(request):
    email=request.session.get("email")
    user=tblseeker.objects.filter(email=email)
    dic={"user":user}
    return render(request,"profile.html",dic)
def logout(request):
    user=request.session.get("email")
    if user:
       del request.session["email"]
       del request.session["name"]
       del request.session["picture"]
       return redirect("/ulogin/")
    return render(request,"logout.html")

def alljobs(request):
    cid=request.GET.get('cid')
    comid=request.GET.get('comid')
    if cid:
        job=tbljob.objects.select_related('company').filter(category=cid).order_by('-id')
    elif comid:
        job=tbljob.objects.select_related('company').filter(company=comid).order_by('-id')
    else:
        job=tbljob.objects.select_related('company').all().order_by('-id')

    dic={"job":job}
    return render(request,'alljobs.html',dic)

def apply(request):
    jid=request.GET.get('jid')
    email=request.session.get("email")
    if email is None :
        return HttpResponse("<script>alert('Login First and then apply...');location.href='/ulogin/'</script>")
    elif jid is None:
            return HttpResponse("<script>alert('Please select a job to apply...');location.href='/alljobs/'</script>")
    else :
        
        job=tbljob.objects.get(id=jid)
        user=tblseeker.objects.get(email=email)
        tblapply(job=job,seeker=user,date=date.today()).save()
        return HttpResponse("<script>alert('Applied Succesfully.Wait for company response.Explore more...');location.href='/jobs/'</script>")
def application(request):
    email=request.session.get("email")
    job=tblapply.objects.select_related('job').filter(seeker=email).order_by('-id')
    dic={'job':job}
    return render(request,'application.html',dic)





