from rest_framework import serializers
from django.db import models

# Contacts table model 
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ()
        
        
        
# Jobs table model         
class Job(models.Model):
    job_title = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    company_location = models.CharField(max_length=50, default='Miami')
    company_overview = models.CharField(max_length=200, default='enter company overview')
    job_description = models.CharField(max_length=500, default='job description')
    responsibilities = models.CharField(max_length=200, default='job responsibilities')
    qualifications = models.CharField(max_length=200, default='qualifications')
    skills = models.CharField(max_length=200, default='job skills')
    salary = models.CharField(max_length=200, default='salary info')
    benefits = models.CharField(max_length=200, default='Paid vacation')
    
    

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = ()  
        
        
# Candidates table model         
class Candidate(models.Model):
    
    full_name= models.CharField(max_length=200, default='')
    email= models.CharField(max_length=100, default='')
    telephone= models.IntegerField(default='')
    street_address1= models.CharField(max_length=100, default='')
    street_address_2= models.CharField(max_length=100, default='')
    city= models.CharField(max_length=70, default='')
    state= models.CharField(max_length=70, default='')
    zip_code= models.IntegerField(default='')
    password= models.CharField(max_length=10, default='')
    job_title_1= models.CharField(max_length=100, default='')
    company_name_1= models.CharField(max_length=100, default='')
    company_city_1= models.CharField(max_length=70, default='')
    job_start_month_1= models.CharField(max_length=20, default='')
    job_start_year_1= models.IntegerField(default='')
    job_end_month_1= models.CharField(max_length=20, default='')
    job_end_year_1= models.IntegerField( default='')
    job_description_1= models.CharField(max_length=200, default='')
    qualification_1= models.CharField(max_length=70, default='')
    degree_1= models.CharField(max_length=70, default='')
    school_name_1= models.CharField(max_length=70, default='')
    field_of_study_1= models.CharField(max_length=70, default='')
    school_city_1= models.CharField(max_length=70, default='')
    school_start_month_1= models.CharField(max_length=70, default='')
    school_start_year_1= models.IntegerField( default='')
    school_end_month_1= models.CharField(max_length=70, default='')
    school_end_year_1= models.CharField(max_length=5, default='')
    skills= models.CharField(max_length=80, default='')
    

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        exclude = ()
        
        


# Blogs table model 
class Blog(models.Model):
    urlToImage = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ()        
        