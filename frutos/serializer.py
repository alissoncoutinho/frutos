from rest_framework import serializers
from frutos.models import Pessoa, Reuniao, Frequencia
from datetime import datetime

class PessoaSerializer(serializers.ModelSerializer):
    data_cadastro = serializers.HiddenField(default=datetime.now)
    class Meta:
        model = Pessoa
        fields = ['id', 'nome','celular', 'data_nascimento', 'tipo','observacao', 'ativo','data_cadastro']
    def validate_nome(self, nome):
        if len(nome) < 3:
            raise serializers.ValidationError("O nome deve ter mais que 2 caracteres")
        return nome

class ReuniaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reuniao
        fields = '__all__'

class FrequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequencia
        exclude = []

class FrequenciaPorPessoaSerializer(serializers.ModelSerializer):
    data_reuniao = serializers.ReadOnlyField(source='reuniao.data_reuniao')
    tipo_reuniao = serializers.ReadOnlyField(source='reuniao.tipo')
    #tipo_reuniao = serializers.SerializerMethodField()
    #def get_tipo_reuniao(self,obj):
    #    return obj.get_tipo_reuniao_display()
    class Meta:
        model = Frequencia
        fields = ['data_reuniao', 'tipo_reuniao']

class FrequenciaPorReuniaoSerializer(serializers.ModelSerializer):
    pessoa_nome = serializers.ReadOnlyField(source='pessoa.nome')
    class Meta:
        model = Frequencia
        fields = ['pessoa_nome']
