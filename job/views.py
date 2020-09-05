from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job
from .form import ApplyForm

def job_list(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs':page_obj}
    return render(request, 'job_list.html', context)

def job_detail(request, slug):
    job = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform = form.save()
    else:
        form = ApplyForm()
    context = {'job':job, 'form': form}
    return render(request, 'job_detail.html', context=context)

def add_job(request):
    pass
