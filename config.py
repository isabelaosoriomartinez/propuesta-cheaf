"""
Archivo de configuración para el proyecto de análisis de reseñas de Cheaf
"""

# Configuración del scraper
SCRAPER_CONFIG = {
    'max_reviews': 2695,  # Número máximo de reseñas a obtener (TODAS las reseñas disponibles)
    'delay_between_requests': 2,  # Pausa entre solicitudes (segundos)
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'language': 'es',  # Idioma de las reseñas
    'country': 'MX',   # País para las reseñas
}

# Configuración del análisis de sentimiento
SENTIMENT_CONFIG = {
    'positive_threshold': 0.1,    # Umbral para sentimiento positivo
    'negative_threshold': -0.1,   # Umbral para sentimiento negativo
    'min_text_length': 10,        # Longitud mínima del texto para análisis
}

# Palabras clave para detección de temas
TOPIC_KEYWORDS = {
    'funcionalidad': [
        'app', 'aplicación', 'funciona', 'funcionalidad', 'característica', 
        'feature', 'herramienta', 'utilidad', 'servicio'
    ],
    'interfaz': [
        'interfaz', 'ui', 'ux', 'diseño', 'pantalla', 'botón', 'menú',
        'navegación', 'layout', 'visual', 'apariencia'
    ],
    'rendimiento': [
        'lento', 'rápido', 'velocidad', 'carga', 'performance', 'optimización',
        'fluido', 'responsivo', 'eficiente', 'rendimiento'
    ],
    'conectividad': [
        'internet', 'conexión', 'wifi', 'datos', 'online', 'offline',
        'red', 'conectividad', 'señal', 'conexión'
    ],
    'ubicación': [
        'ubicación', 'gps', 'localización', 'mapa', 'cerca', 'distancia',
        'zona', 'área', 'local', 'proximidad'
    ],
    'precio': [
        'precio', 'costo', 'gratis', 'pago', 'oferta', 'descuento',
        'económico', 'barato', 'caro', 'valor'
    ],
    'comida': [
        'comida', 'alimento', 'restaurante', 'tienda', 'producto', 'rescate',
        'comida', 'platillo', 'ingrediente', 'fresco'
    ],
    'soporte': [
        'soporte', 'ayuda', 'atención', 'servicio', 'cliente',
        'asistencia', 'contacto', 'respuesta', 'atención'
    ],
    'actualización': [
        'actualización', 'update', 'versión', 'nuevo', 'cambio',
        'mejora', 'nueva versión', 'actualizar', 'renovar'
    ],
    'bug': [
        'error', 'bug', 'problema', 'falla', 'crash', 'no funciona',
        'se cuelga', 'se cierra', 'bloquea', 'lento', 'no responde'
    ]
}

# Palabras clave para feature requests
FEATURE_REQUEST_KEYWORDS = [
    'quisiera', 'me gustaría', 'debería', 'necesito', 'falta', 'agregar',
    'implementar', 'añadir', 'incluir', 'sugerencia', 'propuesta',
    'sería bueno', 'podrían', 'sugiero', 'recomiendo'
]

# Palabras clave para bugs
BUG_KEYWORDS = [
    'error', 'bug', 'problema', 'falla', 'crash', 'no funciona', 'no carga',
    'se cuelga', 'se cierra', 'bloquea', 'lento', 'no responde',
    'defecto', 'mal funcionamiento', 'inconveniente', 'trabado'
]

# Configuración de visualizaciones
VISUALIZATION_CONFIG = {
    'figure_size': (15, 12),
    'dpi': 300,
    'style': 'default',
    'color_palette': 'husl',
    'wordcloud': {
        'width': 800,
        'height': 400,
        'max_words': 100,
        'colormap': 'viridis'
    }
}

# Configuración de reportes
REPORT_CONFIG = {
    'include_charts': True,
    'include_wordcloud': True,
    'include_interactive': True,
    'max_insights': 20,
    'max_feature_requests': 10,
    'max_bugs': 10,
    'max_positive_reviews': 5,
    'max_negative_reviews': 5
}

# URLs de aplicaciones (para facilitar el cambio)
APP_URLS = {
    'cheaf': 'https://play.google.com/store/apps/details?id=com.cheaf.app&pcampaignid=web_share&pli=1',
    # Agregar más aplicaciones aquí si es necesario
}

# Configuración de logging
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(levelname)s - %(message)s',
    'file': 'scraping_analysis.log'
}

# Configuración de salida
OUTPUT_CONFIG = {
    'create_timestamped_dir': True,
    'save_raw_data': True,
    'save_analyzed_data': True,
    'generate_report': True,
    'generate_insights': True,
    'generate_visualizations': True
}

def get_app_id_from_url(url):
    """Extrae el ID de la aplicación desde una URL de Google Play"""
    import re
    match = re.search(r'id=([^&]+)', url)
    if match:
        return match.group(1)
    raise ValueError("No se pudo extraer el ID de la aplicación de la URL")

def validate_config():
    """Valida la configuración del proyecto"""
    errors = []
    
    # Validar configuración del scraper
    if SCRAPER_CONFIG['max_reviews'] <= 0:
        errors.append("max_reviews debe ser mayor a 0")
    
    if SCRAPER_CONFIG['delay_between_requests'] < 0:
        errors.append("delay_between_requests debe ser mayor o igual a 0")
    
    # Validar configuración de sentimiento
    if SENTIMENT_CONFIG['positive_threshold'] <= SENTIMENT_CONFIG['negative_threshold']:
        errors.append("positive_threshold debe ser mayor a negative_threshold")
    
    # Validar palabras clave
    if not TOPIC_KEYWORDS:
        errors.append("TOPIC_KEYWORDS no puede estar vacío")
    
    if not FEATURE_REQUEST_KEYWORDS:
        errors.append("FEATURE_REQUEST_KEYWORDS no puede estar vacío")
    
    if not BUG_KEYWORDS:
        errors.append("BUG_KEYWORDS no puede estar vacío")
    
    if errors:
        raise ValueError(f"Errores en la configuración: {', '.join(errors)}")
    
    return True

# Validar configuración al importar el módulo
try:
    validate_config()
except ValueError as e:
    print(f"⚠️ Advertencia de configuración: {e}") 