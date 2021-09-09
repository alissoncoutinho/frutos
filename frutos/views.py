from rest_framework import viewsets, generics
from frutos.models import Pessoa, Reuniao, Frequencia
from frutos.serializer import PessoaSerializer, ReuniaoSerializer, FrequenciaSerializer, FrequenciaPorPessoaSerializer, FrequenciaPorReuniaoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PessoasViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ReunioesViewSet(viewsets.ModelViewSet):
    queryset = Reuniao.objects.all()
    serializer_class = ReuniaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class FrequenciasViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

class ListaFrequenciasPorPessoa(generics.ListAPIView):
    def get_queryset(self):
        queryset = Frequencia.objects.filter(pessoa_id=self.kwargs['pk'])
        return queryset
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaPorPessoaSerializer

class ListaFrequenciasPorReuniao(generics.ListAPIView):
    def get_queryset(self):
        queryset = Frequencia.objects.filter(reuniao_id=self.kwargs['pk'])
        return queryset
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaPorReuniaoSerializer
