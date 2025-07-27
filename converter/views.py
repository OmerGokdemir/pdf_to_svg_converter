import os
import subprocess
from django.shortcuts import render, redirect
from .forms import PlanUploadForm
from .models import PlanFile
from django.conf import settings

def convert_pdf_to_svg(pdf_path, output_rel_path):
    output_abs_path = os.path.join(settings.MEDIA_ROOT, output_rel_path)
    os.makedirs(os.path.dirname(output_abs_path), exist_ok=True)
    output_path = output_abs_path

    pdftocairo_path = r"C:\Program Files\poppler\poppler-24.08.0\Library\bin\pdftocairo.exe"

    try:
        subprocess.run([
            pdftocairo_path,
            "-svg",
            pdf_path,
            output_path
        ], check=True)
    except subprocess.CalledProcessError as e:
        print("Hata:", e)
        raise e
    
def upload_and_convert(request):
    if request.method == 'POST':
        form = PlanUploadForm(request.POST, request.FILES)
        if form.is_valid():
            plan = form.save()
            svg_filename = f"converted/svg_{plan.id}.svg"  # Uzantıyı burada bırak
            convert_pdf_to_svg(plan.pdf_file.path, svg_filename)
            plan.svg_file.name = svg_filename  # Uzantılı olarak ver
            plan.save()
            return redirect('converted_list')
    else:
        form = PlanUploadForm()
    return render(request, 'upload.html', {'form': form})


def converted_list(request):
    plans = PlanFile.objects.all()
    return render(request, 'converted-list.html', {'plans': plans})
