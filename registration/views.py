from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMultiAlternatives
from django.urls import reverse_lazy
from django import forms
from .models import Profile

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profiles_form.html'

    def get_object(self):
        #recuperasmo el objeto a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    
    def get_form(self, form_class=None):
        form = super(SignUpView,self).get_form()
        #modificamos en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Dirección de correo'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Ingrese su contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Re ingrese su contraseña'})    
        return form

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('check_group_main')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        #recuperasmo el objeto a editar
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super(EmailUpdate,self).get_form()
        #modificamos en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Dirección de correo'})
        return form
@method_decorator(login_required, name='dispatch')
class EmailUpdateCard(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('card_main')
    template_name = 'registration/profile_email_card.html'

    def get_object(self):
        #recuperasmo el objeto a editar
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super(EmailUpdateCard,self).get_form()
        #modificamos en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Dirección de correo'})
        return form
@login_required 
def contact_form(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if request.method == 'POST':
        users = User.objects.get(pk=request.user.id)
        student = Student.objects.get(user_id = request.user.id)
        name = student.name+' '+student.last_name
        carrera = student.profession
        campus = student.campus        
        message = request.POST.get('mensaje')
        subject = 'Solicitud de soporte - Unab - Transporte'
        from_email = 'noreply@unab.cl'
        mail_contact = 'renegalarcegodoy@gmail.com'
        mail_contact2 = 'desaclau@gmail.com'
        #mail admin
        text_content = 'El usuario '+name+' ha enviado el siguiente mensaje '+message
        html_content = '<h3>Unab Transporte Informa</h3><p>El estudiante <strong>'+name+'</strong> registra problemas, favor contactrse a la brevedad</p><p>Nombre: '+name+'</p><p>Carrera: '+str(carrera)+'</p><p>Campus: '+str(campus)+'</p><p>Correo: '+users.email+'</p><p>Estado Tarjeta: '+student.state_card+'</p><p>Mensaje:'+message+'</p><br/><br/><p>Que tenga un buen día .....</p><p>UNAB</p>'
        msg = EmailMultiAlternatives(subject, html_content, from_email, [mail_contact,mail_contact2])
        msg.content_subtype = "html"
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        #mail student
        text_content = 'Estimado '+name+' su mensaje "'+message+'" ha sido enviado a '+mail_contact+' Lo contactaremos a la brevedad'
        html_content = '<h3>Unab Transporte Informa</h3><p>Su mensaje "'+message+'" ha sido enviado a '+mail_contact+' Lo contactaremos a la brevedad'
        msg = EmailMultiAlternatives(subject, html_content, from_email, [users.email])
        msg.content_subtype = "html"
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        messages.add_message(request, messages.INFO, 'Correo enviado correctamente')                             
    template_name = 'registration/contact_form.html' 
    return render(request, template_name)