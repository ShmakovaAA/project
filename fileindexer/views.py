from django.shortcuts import render
from django.db.models import Sum, Count, F
from .models import FileRecord

def index(request):
    total_size = FileRecord.objects.aggregate(total=Sum('size_bytes'))['total'] or 0
    total_gb = total_size / (1024**3)
    context = {
        'total_gb': total_gb,
    }
    return render(request, 'index.html', context)

def stats(request):
    extensions = FileRecord.objects.values('extension').annotate(count=Count('id')).order_by('-count')
    context = {
        'extensions': extensions,
    }
    return render(request, 'stats.html', context)

def top_files(request):
    top = FileRecord.objects.order_by('-size_bytes')[:10]
    context = {
        'top_files': top,
    }
    return render(request, 'top_files.html', context)

def top_images(request):
    top = FileRecord.objects.exclude(width__isnull=True).exclude(height__isnull=True) \
                            .annotate(area=F('width')*F('height')) \
                            .order_by('-area')[:10]
    context = {
        'top_images': top,
    }
    return render(request, 'top_images.html', context)

def top_docs(request):
    top = FileRecord.objects.exclude(page_count__isnull=True).order_by('-page_count')[:10]
    context = {
        'top_docs': top,
    }
    return render(request, 'top_docs.html', context)
