from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages


def register_request(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso")
            return redirect("main:homepage")
        messages.error(
            request, "No se pudo hacer el registro")
    form = RegistrationForm()
    return render(request=request, template_name="signup.html", context={"register_form": form})
