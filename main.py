#!/usr/bin/env python3
"""
Script principal para scraping y análisis de reseñas de Google Play
Análisis de sentimiento, temas, feature requests y bugs para la app Cheaf
"""

import os
import sys
import logging
from datetime import datetime
import pandas as pd
from scraper import GooglePlayScraper
from sentiment_analyzer import SentimentAnalyzer

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraping_analysis.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def create_output_directory():
    """Crea el directorio de salida para los resultados"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"results_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    logger.info(f"Directorio de salida creado: {output_dir}")
    return output_dir

def run_scraping(url: str, max_reviews: int = 500, output_dir: str = "."):
    """
    Ejecuta el proceso de scraping
    
    Args:
        url: URL de la aplicación en Google Play
        max_reviews: Número máximo de reseñas a obtener
        output_dir: Directorio donde guardar los resultados
        
    Returns:
        Lista de reseñas y nombre del archivo CSV
    """
    logger.info("🚀 Iniciando proceso de scraping...")
    
    try:
        scraper = GooglePlayScraper()
        
        # Extraer ID de la aplicación
        app_id = scraper.extract_app_id(url)
        logger.info(f"📱 ID de la aplicación: {app_id}")
        
        # Obtener reseñas
        reviews = scraper.get_reviews(app_id, max_reviews=max_reviews)
        
        if not reviews:
            logger.error("❌ No se obtuvieron reseñas")
            return [], None
        
        # Guardar reseñas en CSV
        csv_filename = f"{output_dir}/cheaf_reviews.csv"
        scraper.save_reviews_to_csv(reviews, csv_filename)
        
        # Generar resumen
        summary = scraper.get_reviews_summary(reviews)
        logger.info("📊 Resumen del scraping:")
        logger.info(f"   Total de reseñas: {summary['total_reviews']}")
        logger.info(f"   Rating promedio: {summary['average_rating']:.2f}")
        logger.info(f"   Distribución de ratings: {summary['rating_distribution']}")
        
        return reviews, csv_filename
        
    except Exception as e:
        logger.error(f"❌ Error durante el scraping: {str(e)}")
        return [], None

def run_analysis(csv_filename: str, output_dir: str = "."):
    """
    Ejecuta el análisis de sentimiento y temas
    
    Args:
        csv_filename: Archivo CSV con las reseñas
        output_dir: Directorio donde guardar los resultados
        
    Returns:
        DataFrame analizado y ruta del reporte
    """
    logger.info("🔍 Iniciando análisis de sentimiento y temas...")
    
    try:
        # Cargar datos
        df = pd.read_csv(csv_filename)
        logger.info(f"📖 Cargadas {len(df)} reseñas para análisis")
        
        # Crear analizador
        analyzer = SentimentAnalyzer()
        
        # Analizar reseñas
        analyzed_df = analyzer.analyze_reviews(df)
        
        # Generar visualizaciones
        analyzer.create_visualizations(analyzed_df, output_dir)
        
        # Generar reporte
        try:
            report_path = analyzer.generate_report(analyzed_df, output_dir)
        except Exception as e:
            logger.warning(f"Error generando reporte: {str(e)}")
            report_path = None
        
        # Guardar DataFrame analizado
        analyzed_csv = f"{output_dir}/analyzed_reviews.csv"
        analyzed_df.to_csv(analyzed_csv, index=False, encoding='utf-8')
        logger.info(f"💾 DataFrame analizado guardado en: {analyzed_csv}")
        
        # Mostrar resumen del análisis
        try:
            summary = analyzer.generate_summary_stats(analyzed_df)
            logger.info("📈 Resumen del análisis:")
            logger.info(f"   Sentimientos: {summary.get('sentiment_distribution', {})}")
            logger.info(f"   Polaridad promedio: {summary.get('average_polarity', 0):.3f}")
            logger.info(f"   Feature requests: {summary.get('feature_requests_count', 0)}")
            logger.info(f"   Bugs reportados: {summary.get('bugs_count', 0)}")
            logger.info(f"   Temas más frecuentes: {dict(list(summary.get('topics_frequency', {}).items())[:5])}")
        except Exception as e:
            logger.warning(f"Error generando resumen: {str(e)}")
        
        return analyzed_df, report_path
        
    except Exception as e:
        logger.error(f"❌ Error durante el análisis: {str(e)}")
        return None, None

def generate_detailed_insights(analyzed_df: pd.DataFrame, output_dir: str = "."):
    """
    Genera insights detallados del análisis
    
    Args:
        analyzed_df: DataFrame con el análisis
        output_dir: Directorio donde guardar los resultados
    """
    logger.info("💡 Generando insights detallados...")
    
    try:
        insights = []
        
        # 1. Feature requests más comunes
        feature_requests = analyzed_df[analyzed_df['feature_request'] == True]
        if not feature_requests.empty:
            insights.append("🚀 FEATURE REQUESTS DETECTADOS:")
            for idx, row in feature_requests.head(10).iterrows():
                insights.append(f"   - {row['full_text'][:100]}...")
        
        # 2. Bugs más reportados
        bugs = analyzed_df[analyzed_df['bug_mentioned'] == True]
        if not bugs.empty:
            insights.append("\n🐛 BUGS REPORTADOS:")
            for idx, row in bugs.head(10).iterrows():
                insights.append(f"   - {row['full_text'][:100]}...")
        
        # 3. Reseñas más positivas
        positive_reviews = analyzed_df[analyzed_df['sentiment_label'] == 'positivo'].sort_values('polarity', ascending=False)
        if not positive_reviews.empty:
            insights.append("\n😊 RESEÑAS MÁS POSITIVAS:")
            for idx, row in positive_reviews.head(5).iterrows():
                insights.append(f"   - Rating {row['rating']}: {row['full_text'][:100]}...")
        
        # 4. Reseñas más negativas
        negative_reviews = analyzed_df[analyzed_df['sentiment_label'] == 'negativo'].sort_values('polarity', ascending=True)
        if not negative_reviews.empty:
            insights.append("\n😞 RESEÑAS MÁS NEGATIVAS:")
            for idx, row in negative_reviews.head(5).iterrows():
                insights.append(f"   - Rating {row['rating']}: {row['full_text'][:100]}...")
        
        # 5. Análisis por rating
        insights.append("\n⭐ ANÁLISIS POR RATING:")
        for rating in sorted(analyzed_df['rating'].unique()):
            rating_reviews = analyzed_df[analyzed_df['rating'] == rating]
            avg_polarity = rating_reviews['polarity'].mean()
            insights.append(f"   - Rating {rating}: {len(rating_reviews)} reseñas, polaridad promedio: {avg_polarity:.3f}")
        
        # Guardar insights
        insights_file = f"{output_dir}/detailed_insights.txt"
        with open(insights_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(insights))
        
        logger.info(f"💾 Insights detallados guardados en: {insights_file}")
        
        # Mostrar algunos insights en consola
        print("\n" + "="*50)
        print("💡 INSIGHTS PRINCIPALES")
        print("="*50)
        for insight in insights[:20]:  # Mostrar solo los primeros 20
            print(insight)
        print("="*50)
        
    except Exception as e:
        logger.error(f"❌ Error generando insights: {str(e)}")

def main():
    """Función principal"""
    print("🎯 ANÁLISIS DE RESEÑAS - CHEAF APP")
    print("="*50)
    
    # URL de la aplicación Cheaf
    url = "https://play.google.com/store/apps/details?id=com.cheaf.app&pcampaignid=web_share&pli=1"
    
    # Crear directorio de salida
    output_dir = create_output_directory()
    
    try:
        # Paso 1: Scraping
        print("\n📱 PASO 1: SCRAPING DE RESEÑAS")
        print("-" * 30)
        reviews, csv_filename = run_scraping(url, max_reviews=500, output_dir=output_dir)
        
        if not reviews:
            print("❌ No se pudieron obtener reseñas. Saliendo...")
            return
        
        # Paso 2: Análisis
        print("\n🔍 PASO 2: ANÁLISIS DE SENTIMIENTO Y TEMAS")
        print("-" * 30)
        analyzed_df, report_path = run_analysis(csv_filename, output_dir)
        
        if analyzed_df is None:
            print("❌ Error en el análisis. Saliendo...")
            return
        
        # Paso 3: Insights detallados
        print("\n💡 PASO 3: GENERANDO INSIGHTS DETALLADOS")
        print("-" * 30)
        generate_detailed_insights(analyzed_df, output_dir)
        
        # Resumen final
        print("\n✅ PROCESO COMPLETADO")
        print("="*50)
        print(f"📁 Directorio de resultados: {output_dir}")
        print(f"📊 Archivos generados:")
        print(f"   - {csv_filename}")
        print(f"   - {output_dir}/analyzed_reviews.csv")
        print(f"   - {report_path}")
        print(f"   - {output_dir}/detailed_insights.txt")
        print(f"   - {output_dir}/sentiment_analysis.png")
        print(f"   - {output_dir}/wordcloud.png")
        print(f"   - {output_dir}/*.html (gráficos interactivos)")
        print("\n🎉 ¡Análisis completado exitosamente!")
        
    except KeyboardInterrupt:
        print("\n⚠️ Proceso interrumpido por el usuario")
    except Exception as e:
        logger.error(f"❌ Error general: {str(e)}")
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main() 