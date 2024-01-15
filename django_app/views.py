from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse

import qrcode

from django_app import models


def index(request):
    return render(request, 'index.html')


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
    # TODO fix image. Привести к картинке, которую принял бы джанго
    alco.qr_image = img
    alco.save()

    return redirect(reverse("index"))










