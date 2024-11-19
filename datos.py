import pandas as pd
import numpy as np

# Definir las columnas del conjunto de datos
columnas = ['ID', 'Edad', 'Género', 'Tipo de enseñanza', 'Nivel socioeconómico', 'Grado', 'Materia', 'Nota', 'Repeticiones', 'Abandonos', 'Actividades extracurriculares', 'Tipo de escuela']

# Generar datos aleatorios para cada columna
datos = {
    'ID': np.arange(1, 301),
    'Edad': np.random.randint(11, 17, size=300),
    'Nombres':np.random.choice(['Nombres'], size=300),
    'Género': np.random.choice(['M', 'F'], size=300),
    'Tipo de enseñanza': np.random.choice(['Pública', 'Privada'], size=300),
    'Nivel socioeconómico': np.random.choice(['Bajo', 'Medio', 'Alto'], size=300),
    'Grado': np.random.randint(6, 12, size=300),
    'Materia': np.random.choice(['Matemática', 'Física', 'Español', 'Sociales'], size=300),
    'Nota': np.random.uniform(0, 10, size=300),
    
    'Repeticiones': np.random.randint(0, 3, size=300),
    'Abandonos': np.random.randint(0, 3, size=300),
    'Actividades extracurriculares': np.random.choice(['Sí', 'No'], size=300),
    'Tipo de escuela': np.random.choice(['Urbana', 'Rural'], size=300)
}


# Crear el conjunto de datos
df = pd.DataFrame(datos)

# Guardar el conjunto de datos en un archivo Excel
df.to_excel('Institucion.xlsx', index=False)