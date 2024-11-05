
## Parcial de diseño de sistemas

### Alumno: Dino Meschini

### Programa que detecta si una secuencia de ADN corresponde a humano o mutante


Hosteado con render en https://mutant-checker.onrender.com

### Instrucciones para correr el programa
- Clonar el repositorio
- Instalar las dependencias con `pip install -r requirements.txt`
- Correr el programa con `python app.py`
- Realizar HTTP requests al puerto 8000

### También corre en docker con:
- `docker build -t mutant-checker .`
- `docker run -p 8000:8000 mutant-checker`