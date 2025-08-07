import requests
import time
import webbrowser

def check_github_pages_status():
    """Verifica el estado de GitHub Pages y genera el link"""
    
    # URL del repositorio
    repo_url = "https://github.com/isabelaosoriomartinez/propuesta-cheaf"
    pages_url = "https://isabelaosoriomartinez.github.io/propuesta-cheaf/"
    
    print("🔍 Verificando estado de GitHub Pages...")
    print(f"📁 Repositorio: {repo_url}")
    print(f"🌐 GitHub Pages: {pages_url}")
    print()
    
    # Verificar si la página está disponible
    try:
        response = requests.get(pages_url, timeout=10)
        if response.status_code == 200:
            print("✅ ¡GitHub Pages está activo!")
            print(f"🎉 Tu landing page está disponible en:")
            print(f"   {pages_url}")
            print()
            print("📋 Pasos para habilitar GitHub Pages:")
            print("1. Ve a tu repositorio en GitHub")
            print("2. Haz clic en 'Settings' (Configuración)")
            print("3. Busca 'Pages' en el menú lateral")
            print("4. En 'Source', selecciona 'Deploy from a branch'")
            print("5. En 'Branch', selecciona 'master' y '/(root)'")
            print("6. Haz clic en 'Save'")
            print()
            print("⏳ Después de configurar, espera unos minutos para que se active.")
            print()
            print("🔗 Links importantes:")
            print(f"   📊 Repositorio: {repo_url}")
            print(f"   🌐 Landing Page: {pages_url}")
            print(f"   📄 README: {repo_url}/blob/master/README.md")
            print()
            
            # Preguntar si quiere abrir el link
            open_browser = input("¿Quieres abrir la página en el navegador? (s/n): ").lower()
            if open_browser == 's':
                webbrowser.open(pages_url)
                print("🌐 Abriendo en el navegador...")
            
        else:
            print("⚠️  GitHub Pages aún no está configurado o activo.")
            print("📋 Sigue los pasos de configuración mencionados arriba.")
            
    except requests.exceptions.RequestException as e:
        print("⚠️  No se pudo verificar el estado de GitHub Pages.")
        print("📋 Esto es normal si aún no has configurado GitHub Pages.")
        print()
        print("🔗 Tu landing page estará disponible en:")
        print(f"   {pages_url}")
        print()
        print("📋 Pasos para habilitar GitHub Pages:")
        print("1. Ve a tu repositorio en GitHub")
        print("2. Haz clic en 'Settings' (Configuración)")
        print("3. Busca 'Pages' en el menú lateral")
        print("4. En 'Source', selecciona 'Deploy from a branch'")
        print("5. En 'Branch', selecciona 'master' y '/(root)'")
        print("6. Haz clic en 'Save'")
        print()
        print("⏳ Después de configurar, espera unos minutos para que se active.")

if __name__ == "__main__":
    check_github_pages_status() 