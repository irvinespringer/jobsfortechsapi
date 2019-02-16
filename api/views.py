from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Contact, ContactSerializer,Job, JobSerializer,Candidate, CandidateSerializer,Blog, BlogSerializer


class ContactsView(APIView):
    def get(self, request, contact_id=None):

        if contact_id is not None:
            contact = Contact.objects.get(id=contact_id)
            serializer = ContactSerializer(contact, many=False)
            return Response(serializer.data)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)
        
    def post(self, request):
            
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self, request, contact_id):
        
        contact = Contact.objects.get(id=contact_id)
        contact.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
  
#jobs api view

class JobsView(APIView):
    def get(self, request, job_id=None):

        if job_id is not None:
           job = Job.objects.get(id=job_id)
           serializer = JobSerializer(job, many=False)
           return Response(serializer.data)
        else:
            jobs = Job.objects.all()
            serializer = JobSerializer(jobs, many=True)
            return Response(serializer.data)
        
    def post(self, request):
            
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self, request, job_id):
        
        job = Job.objects.get(id=job_id)
        job.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)        
        
       

#candidate api view
class CandidatesView(APIView):
    def get(self, request, candidate_id=None):

        if candidate_id is not None:
            candidate = Candidate.objects.get(id=candidate_id)
            serializer = CandidateSerializer(candidate, many=False)
            return Response(serializer.data)
        else:
            candidates = Candidate.objects.all()
            serializer = CandidateSerializer(candidates, many=True)
            return Response(serializer.data)
        
    def post(self, request):
            
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self, request, candidate_id):
        
        candidate = Candidate.objects.get(id=candidate_id)
        candidate.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)        





#blog api view
class BlogsView(APIView):
    def get(self, request, blog_id=None):

        if blog_id is not None:
            blog = Blog.objects.get(id=blog_id)
            serializer = BlogSerializer(blog, many=False)
            return Response(serializer.data)
        else:
            blogs = Blog.objects.all()
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data)
        
    def post(self, request):
            
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self, request, candidate_id):
        
       blog = Blog.objects.get(id=blog_id)
       blog.delete()
        
       return Response(status=status.HTTP_204_NO_CONTENT)     
        