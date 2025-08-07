#!/usr/bin/env python3
"""
Script de configuración para el proyecto de análisis de reseñas de Cheaf
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Verifica que la versión de Python sea compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Se requiere Python 3.8 o superior")
        print(f"   Versión actual: {sys.version}")
        return False
    else:
        print(f"✅ Python {sys.version.split()[0]} - Compatible")
        return True

def install_dependencies():
    """Instala las dependencias del proyecto"""
    print("\n📦 Instalando dependencias...")
    
    try:
        # Verificar si pip está disponible
        subprocess.run([sys.executable, "-m", "pip", "--version"], 
                      check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("❌ Error: pip no está disponible")
        return False
    
    try:
        # Instalar dependencias
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True)
        print("✅ Dependencias instaladas correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al instalar dependencias: {e}")
        return False

def download_nltk_data():
    """Descarga los datos necesarios de NLTK"""
    print("\n📚 Descargando datos de NLTK...")
    
    try:
        import nltk
        
        # Descargar recursos necesarios
        resources = ['punkt', 'stopwords', 'averaged_perceptron_tagger']
        
        for resource in resources:
            try:
                nltk.data.find(f'tokenizers/{resource}' if resource == 'punkt' else f'corpora/{resource}')
                print(f"   ✅ {resource} ya está disponible")
            except LookupError:
                print(f"   📥 Descargando {resource}...")
                nltk.download(resource, quiet=True)
                print(f"   ✅ {resource} descargado")
        
        return True
    except ImportError:
        print("❌ Error: NLTK no está instalado")
        return False
    except Exception as e:
        print(f"❌ Error al descargar datos de NLTK: {e}")
        return False

def test_imports():
    """Prueba que todas las librerías se importen correctamente"""
    print("\n🧪 Probando importaciones...")
    
    required_modules = [
        'requests',
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'plotly',
        'wordcloud',
        'textblob',
        'nltk',
        'beautifulsoup4'
    ]
    
    failed_imports = []
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"   ✅ {module}")
        except ImportError:
            print(f"   ❌ {module}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"\n❌ Error: Los siguientes módulos no se pudieron importar: {', '.join(failed_imports)}")
        return False
    else:
        print("✅ Todas las importaciones exitosas")
        return True

def create_sample_data():
    """Crea datos de ejemplo para pruebas"""
    print("\n📝 Creando datos de ejemplo...")
    
    import pandas as pd
    from datetime import datetime, timedelta
    import random
    
    # Crear datos de ejemplo
    sample_reviews = [
        {
            'review_id': '1',
            'author': 'Usuario Ejemplo',
            'date': '2024-01-15',
            'rating': 5,
            'title': 'Excelente app',
            'content': 'Me encanta esta aplicación, me ha ayudado a ahorrar mucho dinero en comida.',
            'full_text': 'Excelente app - Me encanta esta aplicación, me ha ayudado a ahorrar mucho dinero en comida.'
        },
        {
            'review_id': '2',
            'author': 'Otro Usuario',
            'date': '2024-01-14',
            'rating': 4,
            'title': 'Muy buena',
            'content': 'La app funciona bien, pero me gustaría que agreguen más tiendas en mi zona.',
            'full_text': 'Muy buena - La app funciona bien, pero me gustaría que agreguen más tiendas en mi zona.'
        },
        {
            'review_id': '3',
            'author': 'Usuario Crítico',
            'date': '2024-01-13',
            'rating': 2,
            'title': 'Problemas técnicos',
            'content': 'La app se cuelga constantemente y no carga la lista de productos.',
            'full_text': 'Problemas técnicos - La app se cuelga constantemente y no carga la lista de productos.'
        }
    ]
    
    # Crear DataFrame
    df = pd.DataFrame(sample_reviews)
    
    # Guardar archivo de ejemplo
    df.to_csv('sample_reviews.csv', index=False, encoding='utf-8')
    print("✅ Archivo de ejemplo creado: sample_reviews.csv")
    
    return True

def run_test():
    """Ejecuta una prueba básica del sistema"""
    print("\n🧪 Ejecutando prueba del sistema...")
    
    try:
        # Importar módulos
        from sentiment_analyzer import SentimentAnalyzer
        import pandas as pd
        
        # Cargar datos de ejemplo
        df = pd.read_csv('sample_reviews.csv')
        
        # Crear analizador
        analyzer = SentimentAnalyzer()
        
        # Analizar una reseña de ejemplo
        test_text = "Me encanta esta aplicación, es muy útil para ahorrar dinero."
        sentiment = analyzer.analyze_sentiment(test_text)
        topics = analyzer.extract_topics(test_text)
        
        print(f"   ✅ Análisis de sentimiento: {sentiment}")
        print(f"   ✅ Temas detectados: {topics}")
        print("✅ Prueba del sistema exitosa")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en la prueba del sistema: {e}")
        return False

def main():
    """Función principal del setup"""
    print("🎯 CONFIGURACIÓN DEL PROYECTO - CHEAF APP")
    print("=" * 50)
    
    # Verificar versión de Python
    if not check_python_version():
        sys.exit(1)
    
    # Instalar dependencias
    if not install_dependencies():
        print("\n❌ Error: No se pudieron instalar las dependencias")
        print("   Intenta ejecutar: pip install -r requirements.txt")
        sys.exit(1)
    
    # Descargar datos de NLTK
    if not download_nltk_data():
        print("\n⚠️ Advertencia: No se pudieron descargar los datos de NLTK")
        print("   El análisis de sentimiento puede no funcionar correctamente")
    
    # Probar importaciones
    if not test_imports():
        print("\n❌ Error: Algunas librerías no se pudieron importar")
        sys.exit(1)
    
    # Crear datos de ejemplo
    create_sample_data()
    
    # Ejecutar prueba del sistema
    if not run_test():
        print("\n❌ Error: La prueba del sistema falló")
        sys.exit(1)
    
    print("\n✅ CONFIGURACIÓN COMPLETADA")
    print("=" * 50)
    print("🎉 El proyecto está listo para usar")
    print("\n📋 Próximos pasos:")
    print("   1. Ejecuta: python main.py")
    print("   2. O prueba con: python sentiment_analyzer.py")
    print("   3. Revisa el README.md para más información")
    print("\n📁 Archivos disponibles:")
    print("   - main.py: Script principal")
    print("   - google_play_scraper.py: Scraper de reseñas")
    print("   - sentiment_analyzer.py: Analizador de sentimiento")
    print("   - sample_reviews.csv: Datos de ejemplo")
    print("   - README.md: Documentación completa")

if __name__ == "__main__":
    main() 