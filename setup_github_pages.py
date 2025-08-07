import requests
import webbrowser
import time
import os

def setup_github_pages():
    """Script interactivo para configurar GitHub Pages"""
    
    print("🚀 CONFIGURACIÓN DE GITHUB PAGES")
    print("=" * 50)
    
    # URLs importantes
    repo_url = "https://github.com/isabelaosoriomartinez/propuesta-cheaf"
    pages_url = "https://isabelaosoriomartinez.github.io/propuesta-cheaf/"
    settings_url = f"{repo_url}/settings/pages"
    
    print(f"📁 Repositorio: {repo_url}")
    print(f"🌐 GitHub Pages: {pages_url}")
    print(f"⚙️  Settings: {settings_url}")
    print()
    
    # Paso 1: Abrir el repositorio
    print("📋 PASO 1: Abrir el repositorio")
    print("Voy a abrir tu repositorio en el navegador...")
    
    open_repo = input("¿Quieres abrir el repositorio ahora? (s/n): ").lower()
    if open_repo == 's':
        webbrowser.open(repo_url)
        print("🌐 Abriendo repositorio...")
    
    print()
    print("📋 PASO 2: Configurar GitHub Pages")
    print("1. Haz clic en 'Settings' en la parte superior")
    print("2. Busca 'Pages' en el menú lateral izquierdo")
    print("3. En 'Source', selecciona 'Deploy from a branch'")
    print("4. En 'Branch', selecciona 'master' y '/(root)'")
    print("5. Haz clic en 'Save'")
    print()
    
    open_settings = input("¿Quieres abrir directamente la página de Settings? (s/n): ").lower()
    if open_settings == 's':
        webbrowser.open(settings_url)
        print("⚙️  Abriendo configuración...")
    
    print()
    print("⏳ Después de configurar, espera 2-5 minutos...")
    print()
    
    # Verificar estado
    print("🔍 Verificando estado de GitHub Pages...")
    check_status(pages_url)
    
    # Verificar foto
    check_photo()
    
    print()
    print("🎉 ¡Configuración completada!")
    print(f"Tu landing page estará disponible en: {pages_url}")

def check_status(pages_url):
    """Verifica el estado de GitHub Pages"""
    max_attempts = 10
    attempt = 0
    
    while attempt < max_attempts:
        try:
            response = requests.get(pages_url, timeout=10)
            if response.status_code == 200:
                print("✅ ¡GitHub Pages está activo!")
                print(f"🎉 Tu landing page está disponible en: {pages_url}")
                
                open_page = input("¿Quieres abrir la página ahora? (s/n): ").lower()
                if open_page == 's':
                    webbrowser.open(pages_url)
                
                return True
            else:
                print(f"⏳ Intento {attempt + 1}/{max_attempts}: Página aún no disponible...")
        except requests.exceptions.RequestException:
            print(f"⏳ Intento {attempt + 1}/{max_attempts}: Verificando...")
        
        attempt += 1
        if attempt < max_attempts:
            time.sleep(30)  # Esperar 30 segundos entre intentos
    
    print("⚠️  GitHub Pages aún no está activo después de varios intentos.")
    print("📋 Verifica que hayas configurado correctamente en Settings > Pages")
    return False

def check_photo():
    """Verifica si existe la foto del perfil"""
    photo_path = "Foto.jpg"
    
    if os.path.exists(photo_path):
        print("✅ Foto de perfil encontrada")
    else:
        print("⚠️  Foto de perfil no encontrada")
        print("📸 Para agregar tu foto:")
        print("1. Coloca tu foto en la carpeta del proyecto")
        print("2. Nómbrala exactamente 'Foto.jpg'")
        print("3. Ejecuta: git add Foto.jpg && git commit -m 'Add photo' && git push origin master")

if __name__ == "__main__":
    setup_github_pages()
