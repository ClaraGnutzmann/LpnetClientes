from django.forms import ModelForm
from app.models import Cliente

# Create the form class.
class ClienteForm(ModelForm):
        class Meta:
            model = Cliente
            fields = ['Nome', 'DDD', 'Telefone', 'Cidade', 'Cidade', 'Idade','Valor']

