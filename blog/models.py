from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image_1 = models.ImageField(upload_to='post_pics/', default='avasco.jpeg', blank=True, null=True)
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

    def save(self, *args, **kwargs):
        if self.image_1 and self.image_1.size > 100000:
            self.image_1 = self.compressImage(self.image_1)
        if self.image_2 and self.image_2.size > 100000:
            self.image_2 = self.compressImage(self.image_2)
        if self.image_3 and self.image_3.size > 100000:
            self.image_3 = self.compressImage(self.image_3)
        super(Post, self).save(*args, **kwargs)
        
    
    def compressImage(self,uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        outputIoStream = BytesIO()
        imageTemproary = imageTemproary.resize( (300,250) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=100)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage        


class Timeline(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=2020)
    image = models.ImageField(upload_to = 'timeline_pics/', default='avasco.jpeg')
    content = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image.size > 100000:
            im = Image.open(self.image)
            output = BytesIO()
            im = im.resize( (400,300) )
            im.save(output, format='JPEG', quality=100)
            output.seek(0)
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(Timeline, self).save(*args, **kwargs)
   

class Member(models.Model):

    BLOOD_GROUP = ((1, "A+",), (2, "A-"), (3, "B+"), (4, "B-"),
               (5, "AB+"), (6, "AB-"), (7, "0+"), (8, "O-"), (9,"OTHERS"))

    SECTION = ((1,"INDIA"), (2,"GCC"))

    SEX = ((1,"Male"), (2,"Female"), (3,"Others") )

    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='member_pics/', default='accountdefault.jpg')
    avasco_id =  models.CharField("Avasco ID (if exists)", max_length=10,null=True, blank=True) 
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

    
    def save(self, *args, **kwargs):
        if self.image and self.image.size > 100000:
            self.image = self.compressImage(self.image)
        super(Member, self).save(*args, **kwargs)
        
    
    def compressImage(self,uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        outputIoStream = BytesIO()
        imageTemproary = imageTemproary.resize( (270,270) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=100)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage    

        

class Homepic(models.Model):
    image = models.ImageField(upload_to='home_pics/')
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image and self.image.size > 100000:
            im = Image.open(self.image)
            output = BytesIO()
            im = im.resize( (400,300) )
            im.save(output, format='JPEG', quality=100)
            output.seek(0)
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(Homepic, self).save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        if self.india_poster and self.india_poster.size > 100000:
            self.india_poster = self.compressImage(self.india_poster)
        if self.gcc_poster and self.gcc_poster.size > 100000:
            self.gcc_poster = self.compressImage(self.gcc_poster)
        super(Committee, self).save(*args, **kwargs)
        
    
    def compressImage(self,uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        outputIoStream = BytesIO()
        imageTemproary = imageTemproary.resize( (300,600) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=100)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage        
 
   