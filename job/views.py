from django.shortcuts import render
from .models import Job

def job_list(request):
    jobs = Job.objects.all()
    # context = {'jobs':jobs}
    return render(request, 'job_list.html', {'jobs':jobs})

def job_detail(request, id):
    job = Job.objects.get(id=id)
    context = {'job':job}
    return render(request, 'job_detail.html', context=context)
