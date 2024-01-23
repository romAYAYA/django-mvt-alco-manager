from datetime import datetime
from io import BytesIO

from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.urls import reverse

import qrcode

from django_app import models
from django_app.models import AlcoInfo


def index(request):
    alco_info = AlcoInfo.objects.all()
    return render(request, 'index.html', {"alco_info": alco_info})


def create_alco(request):
    return render(request, 'form.html')


def post_alco(request):
    title = str(request.POST["title"])
    description = str(request.POST["description"])
    expired_date = datetime.strptime(request.POST["expired_date"], "%Y-%m-%d")

    alco = models.AlcoInfo.objects.create(title=title, description=description, expired=expired_date)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(f'http://127.0.0.1:8000/alco/{alco.id}')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    image_io = BytesIO()
    img.save(image_io, format='PNG')
    image_file = ContentFile(image_io.getvalue())

    alco.qr_image.save(f'qr_code_{alco.id}.png', image_file)

    alco.save()

    return redirect(reverse("index"))


def alco_detail(request, alco_id):
    alco = models.AlcoInfo.objects.get(id=int(alco_id))
    return render(request, 'alco_detail.html', {'alco': alco})





















