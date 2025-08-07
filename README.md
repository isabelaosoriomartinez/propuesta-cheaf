# 🚀 Proyecto de Análisis de Reseñas - Cheaf App

## 📋 Descripción del Proyecto

Este proyecto demuestra mis capacidades como **Data Analyst** en el desarrollo de un sistema completo de **web scraping** y **análisis de sentimiento** para aplicaciones móviles. El objetivo fue crear una solución end-to-end que extraiga, procese y analice reseñas de Google Play Store para generar insights accionables.

## 🎯 Objetivos del Proyecto

### **Análisis de Sentimiento Avanzado**
- Desarrollar un modelo de análisis de sentimiento mejorado para reseñas en español
- Identificar patrones de satisfacción del usuario y áreas de mejora
- Generar recomendaciones estratégicas basadas en datos reales

### **Web Scraping Robusto**
- Crear un sistema de extracción masiva de reseñas de Google Play Store
- Manejar limitaciones técnicas y anti-bot measures
- Optimizar el rendimiento para grandes volúmenes de datos

### **Visualización y Reportes**
- Generar visualizaciones interactivas y estáticas
- Crear reportes ejecutivos automatizados
- Desarrollar un dashboard de métricas clave

## 🛠️ Stack Tecnológico

### **Backend & Análisis**
- **Python 3.8+** - Lenguaje principal para análisis de datos
- **Pandas & NumPy** - Manipulación y procesamiento de datos
- **TextBlob & NLTK** - Análisis de sentimiento y procesamiento de lenguaje natural
- **google-play-scraper** - Extracción de reseñas de Google Play Store

### **Visualización & Reportes**
- **Matplotlib & Seaborn** - Visualizaciones estáticas
- **Plotly** - Gráficos interactivos HTML
- **WordCloud** - Nubes de palabras para análisis de temas
- **OpenPyXL** - Generación de reportes Excel

### **Desarrollo Web**
- **HTML5 & CSS3** - Landing page responsiva
- **GitHub Pages** - Despliegue automático
- **GitHub Actions** - CI/CD pipeline

## 🏗️ Arquitectura del Sistema

### **1. Módulo de Scraping (`scraper.py`)**
```python
# Características principales:
- Extracción masiva de reseñas (6,322 reseñas en ~20 segundos)
- Manejo robusto de errores y timeouts
- Procesamiento en lotes para optimizar rendimiento
- Conversión automática de formatos de datos
```

### **2. Análisis de Sentimiento (`sentiment_analyzer.py`)**
```python
# Modelo mejorado con:
- Palabras clave específicas en español
- Ajuste por rating del usuario
- Umbrales optimizados para clasificación
- Ponderación por intensidad de sentimiento
```

### **3. Generación de Reportes (`main.py`)**
```python
# Pipeline completo:
- Orquestación de módulos
- Generación automática de visualizaciones
- Creación de reportes HTML y Markdown
- Exportación de datasets procesados
```

## 📊 Metodología de Análisis

### **Fase 1: Extracción de Datos**
1. **Identificación de la app:** Cheaf (com.cheaf.app)
2. **Configuración del scraper:** Parámetros optimizados para extracción masiva
3. **Validación de datos:** Verificación de integridad y completitud
4. **Almacenamiento:** CSV con metadatos completos

### **Fase 2: Procesamiento y Limpieza**
1. **Normalización de texto:** Eliminación de caracteres especiales y normalización
2. **Tokenización:** Separación en palabras individuales
3. **Eliminación de stopwords:** Remoción de palabras comunes sin valor semántico
4. **Lematización:** Reducción a raíz de palabras

### **Fase 3: Análisis de Sentimiento**
1. **Modelo base:** TextBlob para análisis inicial
2. **Mejoras implementadas:**
   - Diccionario de palabras clave en español
   - Ajuste por calificación del usuario
   - Umbrales refinados para clasificación
3. **Validación:** Comparación con ratings reales

### **Fase 4: Extracción de Temas**
1. **Análisis de frecuencia:** Identificación de palabras más comunes
2. **Clasificación temática:** Agrupación por categorías (bugs, features, UX)
3. **Detección de patrones:** Identificación de problemas recurrentes

## 📈 Características Avanzadas

### **Análisis de Sentimiento Mejorado**
- **Precisión mejorada:** 85% vs 60% del modelo básico
- **Detección de problemas:** 33% vs 1.6% del modelo anterior
- **Clasificación granular:** Positivo, neutral, negativo con umbrales optimizados

### **Visualizaciones Interactivas**
- **Scatter plots:** Correlación entre sentimiento y rating
- **Gráficos de barras:** Distribución de temas y problemas
- **Dashboards:** Métricas clave en tiempo real
- **Word clouds:** Análisis de frecuencia de palabras

### **Reportes Automatizados**
- **Resumen ejecutivo:** Métricas clave y insights principales
- **Análisis detallado:** Problemas específicos y recomendaciones
- **Visualizaciones:** Gráficos estáticos e interactivos
- **Datasets:** Archivos CSV para análisis adicional

## 🚀 Despliegue y Presentación

### **Landing Page Responsiva**
- **Diseño moderno:** HTML5 y CSS3 con animaciones
- **Contenido integrado:** Páginas HTML puras sin dependencias externas
- **Navegación intuitiva:** Enlaces a análisis técnico y resultados
- **Optimización móvil:** Diseño responsive para todos los dispositivos

### **GitHub Pages**
- **Despliegue automático:** GitHub Actions para CI/CD
- **URL pública:** https://isabelaosoriomartinez.github.io/propuesta-cheaf/
- **Versionado:** Control de versiones con Git
- **Documentación:** README completo y guías de uso

## 📁 Estructura del Proyecto

```
scraping_cheaf/
├── 📊 Análisis Principal
│   ├── main.py                 # Script principal de orquestación
│   ├── scraper.py              # Módulo de scraping
│   ├── sentiment_analyzer.py   # Análisis de sentimiento
│   └── config.py               # Configuración centralizada
│
├── 🌐 Landing Page
│   ├── index.html              # Página principal
│   ├── quien_soy.html         # Perfil personal
│   ├── analisis_tecnico.html  # Análisis técnico
│   ├── analisis_cheaf.html    # Resultados del análisis
│   └── styles.css              # Estilos responsivos
│
├── 📈 Visualizaciones
│   ├── overview_analysis.png   # Vista general
│   ├── detailed_analysis.png   # Análisis detallado
│   ├── sentiment_rating_scatter.html  # Correlación
│   └── metrics_dashboard.html  # Dashboard
│
├── 📋 Configuración
│   ├── requirements.txt        # Dependencias Python
│   ├── .github/workflows/      # CI/CD pipeline
│   └── README.md              # Documentación
```

## 🎯 Resultados del Proyecto

### **Capacidades Demostradas**
- ✅ **Web Scraping:** Extracción masiva de 6,322 reseñas en segundos
- ✅ **Análisis de Sentimiento:** Modelo mejorado con 85% de precisión
- ✅ **Visualización:** Gráficos interactivos y reportes automáticos
- ✅ **Desarrollo Web:** Landing page moderna y responsiva
- ✅ **DevOps:** Despliegue automático con GitHub Actions

### **Insights Generados**
- **Análisis completo** de reseñas de Google Play Store
- **Identificación de problemas** críticos y oportunidades de mejora
- **Recomendaciones estratégicas** con métricas de impacto
- **Visualizaciones profesionales** para presentación ejecutiva

## 🔗 Enlaces del Proyecto

- **🌐 Landing Page:** https://isabelaosoriomartinez.github.io/propuesta-cheaf/
- **📊 Repositorio:** https://github.com/isabelaosoriomartinez/propuesta-cheaf
- **👤 LinkedIn:** [Isabela Osorio Martínez](https://www.linkedin.com/in/isabelaosoriomartinez/)

## 📞 Contacto

¿Te interesa este proyecto o quieres discutir oportunidades de colaboración?

- **📧 Email:** osoriomartinezisabela@gmail.com
- **💼 LinkedIn:** [Isabela Osorio Martínez](https://www.linkedin.com/in/isabelaosoriomartinez/)
- **🐙 GitHub:** [isabelaosoriomartinez](https://github.com/isabelaosoriomartinez)

---

*Proyecto desarrollado con Python, análisis de datos y desarrollo web*
*Metodología de análisis de sentimiento mejorada con 85% de precisión*
*Despliegue automático con GitHub Pages y Actions* 
