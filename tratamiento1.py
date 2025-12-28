import os
import shutil
from tqdm import tqdm  # Si no tienes tqdm: pip install tqdm

# --- CONFIGURACIÓN ---
# 1. Ruta donde están las 27 carpetas (La misma que usaste para ver la lista)
# Ejemplo: "C:/Users/oicas/Desktop/Datasets/wikiart"
ORIGEN = r'C:\Users\oicas\OneDrive\Desktop\Intro a las App de Algoritmos de ML y DL\Proyecto\Dataset\WikiArt' 

# 2. Ruta donde se creará tu dataset limpio
DESTINO = r'C:\Users\oicas\OneDrive\Desktop\Intro a las App de Algoritmos de ML y DL\Proyecto\Dataset\dataset_proyecto_final'

# 3. Lista validada de estilos (Extraída de tu output)
ESTILOS_A_USAR = [
    'Cubism', 'Ukiyo_e', 'Impressionism', 'Pop_Art', 'Realism', 'Abstract_Expressionism' 
]

# --- PROCESO ---
def crear_dataset_filtrado():
    # Crear carpeta principal de destino
    if not os.path.exists(DESTINO):
        os.makedirs(DESTINO)
        print(f"Carpeta creada: {os.path.abspath(DESTINO)}")

    print(f"Iniciando extracción de {len(ESTILOS_A_USAR)} estilos...")

    for estilo in ESTILOS_A_USAR:
        ruta_estilo_origen = os.path.join(ORIGEN, estilo)
        ruta_estilo_destino = os.path.join(DESTINO, estilo)
        
        # 1. Verificar que la carpeta de origen existe
        if not os.path.exists(ruta_estilo_origen):
            print(f"ERROR: No encontré la carpeta '{estilo}' en {ORIGEN}")
            continue
            
        # 2. Verificar si ya la copiamos antes (para no repetir)
        if os.path.exists(ruta_estilo_destino):
            n_existentes = len(os.listdir(ruta_estilo_destino))
            print(f"ℹ'{estilo}' ya existe con {n_existentes} imágenes. Saltando...")
            continue
            
        # 3. Copiar la carpeta entera
        try:
            print(f"Copiando {estilo}...", end="\r")
            shutil.copytree(ruta_estilo_origen, ruta_estilo_destino)
            
            # Confirmación
            n_imgs = len(os.listdir(ruta_estilo_destino))
            print(f"{estilo}: Copiado con éxito ({n_imgs} imágenes).")
        except Exception as e:
            print(f"Error copiando {estilo}: {e}")

    print("\n✨ ¡Todo listo! Tu dataset está en la carpeta 'dataset_proyecto_final'.")

if __name__ == "__main__":
    # Verificación de seguridad antes de correr
    if os.path.exists(ORIGEN):
        crear_dataset_filtrado()
    else:
        print("La ruta de ORIGEN no es válida. Por favor edita la variable ORIGEN en el código.")