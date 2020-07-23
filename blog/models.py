from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image_1 = models.ImageField(upload_to='post_pics/', default='avasco_logo.jpeg', blank=True, null=True)
    image_2 = models.ImageField(upload_to='post_pics/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='post_pics/', blank=True, null=True)
    file_1 = models.FileField(upload_to='post_files/', blank=True, null=True)
    file_2 = models.FileField(upload_to='post_files/', blank=True, null=True)
    file_3 = models.FileField(upload_to='post_files/', blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Timeline(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=2020)
    image = models.ImageField(upload_to = 'timeline_pics/', default='avasco_logo.jpeg')
    content = models.TextField()

    def __str__(self):
        return self.title
   

class Member(models.Model):

    BLOOD_GROUP = ((1, "A+",), (2, "A-"), (3, "B+"), (4, "B-"),
               (5, "AB+"), (6, "AB-"), (7, "0+"), (8, "O-"), (9,"OTHERS"))

    SECTION = ((1,"INDIA"), (2,"GCC"))

    SEX = ((1,"Male"), (2,"Female"), (3,"Others") )

    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='member_pics/', default='account_default.jpg')
    blood_group = models.IntegerField( 
        choices = BLOOD_GROUP,
        default = 9,null= True
        ) 
    sex = models.IntegerField(
        choices= SEX,
        default=1, null= True
    )    
    email = models.EmailField(max_length=30, null= True, blank=True)
    phone_1_india = models. IntegerField("Indian Phone (if exists)",null=True, blank=True) 
    phone_2_gcc = models.IntegerField("GCC Phone (if exists)",null=True, blank=True) 
    section = models.IntegerField(
        choices= SECTION,
        default= 1, null= True
    )
    current_location = models.URLField( max_length=200, default= "https://maps.app.goo.gl/aSoSHUyyFsuMZMsB6",null=True, blank=True) 
    country = models.CharField(max_length=20, default="India",null=True, blank=True) 
    city = models.CharField(max_length=20, default="Thrissur",null=True, blank=True) 
    place = models.CharField(max_length=30, default="Aviyoor, Edakkara P.O",null=True, blank=True) 
    occupation_or_course = models.CharField("Occupation/Course", max_length=100, default="Student",null=True, blank=True) 
    company_or_institution_name = models.CharField("Company/Institution Name", max_length=100,null=True, blank=True) 
    company_or_institution_place = models.CharField("Company/Institution Place", max_length=100,null=True, blank=True) 

    def __str__(self):
        return self.name

class Homepic(models.Model):
    image = models.ImageField(upload_to='home_pics/')
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Committee(models.Model):
    
    india_poster = models.ImageField(upload_to='committee_pics', null=True, blank=True)
    gcc_poster = models.ImageField(upload_to='committee_pics', null=True, blank=True)
    
    president = models.ForeignKey(Member,related_name="president", null=True,blank=True, on_delete= models.SET_NULL)
    secretary = models.ForeignKey(Member,related_name="secretary", null=True,blank=True, on_delete= models.SET_NULL)
    vice_president_1 = models.ForeignKey(Member,related_name="vice_president_1", null=True,blank=True, on_delete= models.SET_NULL)
    vice_president_2 = models.ForeignKey(Member,related_name="vice_president_2", null=True,blank=True, on_delete= models.SET_NULL)
    joint_secretary_1 = models.ForeignKey(Member,related_name="joint_secretary_1", null=True,blank=True, on_delete= models.SET_NULL)
    joint_secretary_2 = models.ForeignKey(Member,related_name="joint_secretary_2", null=True,blank=True, on_delete= models.SET_NULL)
    treasurer = models.ForeignKey(Member,related_name="treasurer", null=True,blank=True, on_delete= models.SET_NULL)
    executive_member_1 = models.ForeignKey(Member,related_name="executive_member_1", null=True,blank=True, on_delete= models.SET_NULL)
    executive_member_2 = models.ForeignKey(Member,related_name="executive_member_2", null=True,blank=True, on_delete= models.SET_NULL)
    executive_member_3= models.ForeignKey(Member,related_name="executive_member_3", null=True,blank=True, on_delete= models.SET_NULL)
    executive_member_4 = models.ForeignKey(Member,related_name="executive_member_4", null=True,blank=True, on_delete= models.SET_NULL)
    

    gcc_president = models.ForeignKey(Member,related_name="gcc_president", null=True,blank=True, on_delete= models.SET_NULL)
    gcc_secretary = models.ForeignKey(Member,related_name="gcc_secretary", null=True,blank=True, on_delete= models.SET_NULL)
    gcc_vice_president_1 = models.ForeignKey(Member,related_name="gcc_vice_president_1", null=True,blank=True, on_delete= models.SET_NULL)
    gcc_vice_president_2 = models.ForeignKey(Member,related_name="gcc_vice_president_2", null=True,blank=True, on_delete= models.SET_NULL)
    gcc_joint_secretary_1 = models.ForeignKey(Member,related_name="gcc_joint_secretary_1", null=True,blank=True, on_delete= models.SET_NULL)
    gcc_joint_secretary_2 = models.ForeignKey(Member,related_name="gcc_joint_secretary_2", null=True,blank=True, on_delete= models.SET_NULL)
    gcc_treasurer = models.ForeignKey(Member,related_name="gcc_treasurer", null=True,blank=True, on_delete= models.SET_NULL)
    gcc_executive_member_1 = models.ForeignKey(Member,related_name="gcc_executive_member_1", null=True,blank=True, on_delete= models.SET_NULL)
    gcc_executive_member_2 = models.ForeignKey(Member,related_name="gcc_executive_member_2", null=True,blank=True, on_delete= models.SET_NULL)
    gcc_executive_member_3= models.ForeignKey(Member,related_name="gcc_executive_member_3", null=True,blank=True, on_delete= models.SET_NULL)
    gcc_executive_member_4 = models.ForeignKey(Member,related_name="gcc_executive_member_4", null=True,blank=True, on_delete= models.SET_NULL)
    
    def __str__(self):
        return "Committee"
   