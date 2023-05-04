from django.db import models

class Carga(models.Model):
<<<<<<< HEAD
    year = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
=======
    year = models.DecimalField(max_digits=5, decimal_places=0)
>>>>>>> 52b33dc9cd071236c943a40a899eb719b906e950
    ciclo_acad = models.CharField(max_length=255)
    
    estados = (
        ('Solicitado', 'Solicitado'),
        ('En proceso', 'En proceso'),
        ('Aprobado', 'Aprobado'),
        ('No aprobado', 'No aprobado')
    )
    estado = models.CharField(max_length=255, choices=estados, default='En proceso')
    fecha_envio = models.DateField() 
    fecha_aprob = models.DateField()

    def get_created_at(self):
        return self.fecha_envio.strftime('%d-%m-%Y')
    