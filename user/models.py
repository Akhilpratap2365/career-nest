from django.db import models

# Create your models here.
class tblcontact(models.Model):
  name=models.CharField(max_length=70,null=True)
  email=models.EmailField(max_length=100,null=True)
  mobile=models.CharField(max_length=20,null=True)
  message=models.TextField(null=True)

class tblgallery(models.Model):
    title=models.CharField(max_length=50)
    picture=models.ImageField(upload_to="static/gallery/",null=True)
class tblteam(models.Model):
     name=models.CharField(max_length=70, null=True)
     picture=models.ImageField(upload_to="static/team/",null=True)
     post=models.CharField(max_length=30,null=True)
     experience=models.CharField(max_length=70,null=True)



class tblcity(models.Model):
  name=models.CharField(max_length=100, null=True)
  picture=models.ImageField(upload_to="static/city/", null=True)
  def __str__(self):
    return self.name

class tblcategory(models.Model):
  name=models.CharField(max_length=100, null=True)
  picture=models.ImageField(upload_to="static/category/", null=True)
  def __str__(self):
    return self.name

class tblcompany(models.Model):
  name=models.CharField(max_length=200, null=True)
  email=models.EmailField(max_length=200, null=True)
  mobile=models.IntegerField(null=True)
  department=models.CharField(max_length=200, null=True)
  city=models.ForeignKey(tblcity,on_delete=models.CASCADE)
  owner=models.CharField(max_length=200, null=True)
  logo=models.ImageField(upload_to="static/logo/", null=True)
  type=models.CharField(max_length=200, null=True)
  detail=models.TextField(null=True)
  url=models.CharField(max_length=100, null=True)
  startdate=models.DateField(null=True)
  active=models.BooleanField(null=True)
  isimp=models.BooleanField(null=True)
  ispaid=models.BooleanField(null=True)
  def __str__(self):
    return self.name

class tblseeker(models.Model):
  name=models.CharField(max_length=200, null=True)
  email=models.EmailField(primary_key=True,max_length=100,default="")
  mobile=models.IntegerField(null=True)
  password=models.CharField(max_length=50, null=True)
  qualification=models.CharField(max_length=200, null=True)
  exp=models.CharField(max_length=200, null=True)
  company=models.CharField(max_length=200, null=True)
  resume=models.ImageField(upload_to="static/resume/", null=True)
  salary=models.IntegerField(null=True)
  esalary=models.IntegerField(null=True)
  picture=models.ImageField(upload_to="static/profile/", null=True,blank=True)
  regdate=models.DateField(null=True)
  def __str__(self):
    return self.name

class tbljob(models.Model):
  company=models.ForeignKey(tblcompany,on_delete=models.CASCADE)
  title=models.CharField(max_length=200, null=True)
  description=models.TextField( null=True)
  jobtype=models.CharField(max_length=100,null=True)
  city=models.ForeignKey(tblcity,on_delete=models.CASCADE)
  category=models.ForeignKey(tblcategory,on_delete=models.CASCADE)
  minsalary=models.IntegerField(null=True)
  maxsalary=models.IntegerField(null=True)
  prefgender=models.CharField(max_length=100,null=True)
  exp=models.CharField(max_length=200, null=True)
  skills=models.CharField(max_length=300, null=True)
  vacany=models.IntegerField(null=True)
  lastdate=models.DateField(null=True)
  startdate=models.DateField(null=True)
  active=models.BooleanField(null=True)
  def __str__(self):
    return self.title

class tblapply(models.Model):
  job=models.ForeignKey(tbljob,on_delete=models.CASCADE)
  seeker=models.ForeignKey(tblseeker,on_delete=models.CASCADE)  
  date=models.DateField(null=True)
  cvselected=models.DateTimeField(null=True,blank=True)
  interview=models.DateTimeField(null=True,blank=True)
  hired=models.DateTimeField(null=True,blank=True)
  rejected=models.DateTimeField(null=True,blank=True)
  




 


     
      
  
