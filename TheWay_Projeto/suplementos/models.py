from django.db import models

class ConsultaSuplemento(models.Model):
    nome = models.CharField(max_length=100)
    peso = models.FloatField()
    altura = models.FloatField()
    recomendacao = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        # Lógica de decisão (Slide de Python: if/elif/else)
        imc = self.peso / (self.altura ** 2)
        
        if imc < 18.5:
            self.recomendacao = "Foco em Hipercalóricos e Proteínas."
        elif 18.5 <= imc < 25:
            self.recomendacao = "Foco em Creatina e Whey Protein."
        else:
            self.recomendacao = "Foco em Termogênicos e controle de dieta."
            
        super().save(*args, **kwargs)