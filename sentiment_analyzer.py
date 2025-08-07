import pandas as pd
import numpy as np
import re
import nltk
from textblob import TextBlob
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import logging
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SentimentAnalyzer:
    """
    Analizador de sentimiento y extracción de temas para reseñas de Google Play
    """
    
    def __init__(self):
        # Descargar recursos de NLTK si no están disponibles
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')
        
        # Palabras clave para detección de temas
        self.feature_keywords = {
            'funcionalidad': ['app', 'aplicación', 'funciona', 'funcionalidad', 'característica', 'feature'],
            'interfaz': ['interfaz', 'ui', 'ux', 'diseño', 'pantalla', 'botón', 'menú'],
            'rendimiento': ['lento', 'rápido', 'velocidad', 'carga', 'performance', 'optimización'],
            'conectividad': ['internet', 'conexión', 'wifi', 'datos', 'online', 'offline'],
            'ubicación': ['ubicación', 'gps', 'localización', 'mapa', 'cerca', 'distancia'],
            'precio': ['precio', 'costo', 'gratis', 'pago', 'oferta', 'descuento'],
            'comida': ['comida', 'alimento', 'restaurante', 'tienda', 'producto', 'rescate'],
            'soporte': ['soporte', 'ayuda', 'atención', 'servicio', 'cliente'],
            'actualización': ['actualización', 'update', 'versión', 'nuevo', 'cambio'],
            'bug': ['error', 'bug', 'problema', 'falla', 'crash', 'no funciona']
        }
        
        # Palabras clave para feature requests
        self.feature_request_keywords = [
            'quisiera', 'me gustaría', 'debería', 'necesito', 'falta', 'agregar',
            'implementar', 'añadir', 'incluir', 'sugerencia', 'propuesta'
        ]
        
        # Palabras clave para bugs
        self.bug_keywords = [
            'error', 'bug', 'problema', 'falla', 'crash', 'no funciona', 'no carga',
            'se cuelga', 'se cierra', 'bloquea', 'lento', 'no responde'
        ]
    
    def analyze_sentiment(self, text: str) -> Dict[str, float]:
        """
        Analiza el sentimiento de un texto usando un enfoque mejorado
        
        Args:
            text: Texto a analizar
            
        Returns:
            Diccionario con polaridad y subjetividad
        """
        try:
            # Análisis base con TextBlob
            blob = TextBlob(text)
            base_polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity
            
            # Análisis mejorado con palabras clave específicas
            enhanced_polarity = self._enhance_sentiment_analysis(text, base_polarity)
            
            return {
                'polarity': enhanced_polarity,
                'subjectivity': subjectivity
            }
        except Exception as e:
            logger.warning(f"Error al analizar sentimiento: {str(e)}")
            return {'polarity': 0.0, 'subjectivity': 0.0}
    
    def _enhance_sentiment_analysis(self, text: str, base_polarity: float) -> float:
        """
        Mejora el análisis de sentimiento usando palabras clave específicas
        """
        text_lower = text.lower()
        
        # Palabras muy negativas (peso alto)
        very_negative_words = [
            'pésima', 'terrible', 'horrible', 'muy mal', 'muy mala', 'decepcionada',
            'decepcionado', 'no funciona', 'no carga', 'se cuelga', 'se cierra',
            'bloquea', 'error', 'bug', 'problema', 'falla', 'crash', 'no responde',
            'basura', 'inútil', 'inutil', 'no sirve', 'no sirve', 'desinstalar',
            'desinstalé', 'desinstale', 'no recomiendo', 'no recomiendo', 'pésimo',
            'malísimo', 'malisimo', 'porquería', 'porqueria', 'falsa', 'estafa',
            'estafan', 'mentira', 'mentiroso', 'engaño', 'engañan', 'fraude'
        ]
        
        # Palabras negativas (peso medio)
        negative_words = [
            'mal', 'mala', 'malo', 'problema', 'problemas', 'difícil', 'dificil',
            'complicado', 'lento', 'lenta', 'tarda', 'demora', 'molesto', 'molesta',
            'frustrante', 'frustración', 'frustracion', 'decepción', 'decepcion',
            'decepcionada', 'decepcionado', 'no me gusta', 'no me gustó', 'no me gusto',
            'no funciona', 'no carga', 'no responde', 'no sirve', 'no sirve',
            'no recomiendo', 'no recomiendo', 'no volvería', 'no volveria',
            'no volveré', 'no volvere', 'no lo recomiendo', 'no la recomiendo'
        ]
        
        # Palabras muy positivas (peso alto)
        very_positive_words = [
            'excelente', 'perfecta', 'perfecto', 'maravillosa', 'maravilloso',
            'increíble', 'increible', 'fantástica', 'fantastica', 'fantástico',
            'fantastico', 'genial', 'brillante', 'espectacular', 'magnífica',
            'magnifica', 'magnífico', 'magnifico', 'extraordinaria', 'extraordinario',
            'sobresaliente', 'excepcional', 'increíble', 'increible', 'asombrosa',
            'asombroso', 'sorprendente', 'increíble', 'increible', 'fantástica'
        ]
        
        # Palabras positivas (peso medio)
        positive_words = [
            'buena', 'bueno', 'buen', 'excelente', 'perfecta', 'perfecto',
            'me gusta', 'me gustó', 'me gusto', 'me encanta', 'me encantó',
            'me encanto', 'genial', 'brillante', 'fantástica', 'fantastica',
            'fantástico', 'fantastico', 'increíble', 'increible', 'maravillosa',
            'maravilloso', 'espectacular', 'magnífica', 'magnifica', 'magnífico',
            'magnifico', 'extraordinaria', 'extraordinario', 'sobresaliente',
            'excepcional', 'asombrosa', 'asombroso', 'sorprendente', 'increíble'
        ]
        
        # Calcular puntuación mejorada
        score = base_polarity
        
        # Ajustar por palabras muy negativas
        for word in very_negative_words:
            if word in text_lower:
                score -= 0.3  # Peso alto para palabras muy negativas
        
        # Ajustar por palabras negativas
        for word in negative_words:
            if word in text_lower:
                score -= 0.15  # Peso medio para palabras negativas
        
        # Ajustar por palabras muy positivas
        for word in very_positive_words:
            if word in text_lower:
                score += 0.3  # Peso alto para palabras muy positivas
        
        # Ajustar por palabras positivas
        for word in positive_words:
            if word in text_lower:
                score += 0.15  # Peso medio para palabras positivas
        
        # Ajustar por rating (si está disponible en el contexto)
        # Los ratings bajos (1-2) tienden a indicar sentimiento negativo
        # Los ratings altos (4-5) tienden a indicar sentimiento positivo
        
        # Limitar el rango de polaridad
        score = max(-1.0, min(1.0, score))
        
        return score
    
    def get_sentiment_label(self, polarity: float) -> str:
        """Convierte la polaridad en una etiqueta de sentimiento con umbrales más precisos"""
        if polarity > 0.05:  # Umbral más bajo para positivo
            return 'positivo'
        elif polarity < -0.05:  # Umbral más bajo para negativo
            return 'negativo'
        else:
            return 'neutral'
    
    def extract_topics(self, text: str) -> List[str]:
        """
        Extrae temas mencionados en el texto
        
        Args:
            text: Texto a analizar
            
        Returns:
            Lista de temas encontrados
        """
        text_lower = text.lower()
        topics = []
        
        for topic, keywords in self.feature_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    topics.append(topic)
                    break
        
        return list(set(topics))
    
    def detect_feature_requests(self, text: str) -> bool:
        """Detecta si el texto contiene una solicitud de feature"""
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.feature_request_keywords)
    
    def detect_bugs(self, text: str) -> bool:
        """Detecta si el texto menciona un bug o problema"""
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.bug_keywords)
    
    def analyze_reviews(self, reviews_df: pd.DataFrame) -> pd.DataFrame:
        """
        Analiza todas las reseñas y agrega columnas de análisis
        
        Args:
            reviews_df: DataFrame con las reseñas
            
        Returns:
            DataFrame con análisis agregado
        """
        logger.info("Iniciando análisis de sentimiento y temas...")
        
        # Crear copia del DataFrame
        analyzed_df = reviews_df.copy()
        
        # Analizar sentimiento
        sentiment_results = []
        topics_list = []
        feature_requests = []
        bugs_detected = []
        
        for idx, row in analyzed_df.iterrows():
            text = row.get('full_text', '') or row.get('content', '') or ''
            rating = row.get('rating', 3)  # Rating por defecto si no está disponible
            
            # Análisis de sentimiento con consideración del rating
            sentiment = self.analyze_sentiment(text)
            adjusted_sentiment = self._adjust_sentiment_by_rating(sentiment, rating)
            sentiment_results.append(adjusted_sentiment)
            
            # Extracción de temas
            topics = self.extract_topics(text)
            topics_list.append(topics)
            
            # Detección de feature requests y bugs
            feature_requests.append(self.detect_feature_requests(text))
            bugs_detected.append(self.detect_bugs(text))
        
        # Agregar columnas de análisis
        analyzed_df['polarity'] = [r['polarity'] for r in sentiment_results]
        analyzed_df['subjectivity'] = [r['subjectivity'] for r in sentiment_results]
        analyzed_df['sentiment_label'] = [self.get_sentiment_label(r['polarity']) for r in sentiment_results]
        analyzed_df['topics'] = topics_list
        analyzed_df['feature_request'] = feature_requests
        analyzed_df['bug_mentioned'] = bugs_detected
        
        logger.info("Análisis completado")
        return analyzed_df
    
    def _adjust_sentiment_by_rating(self, sentiment: Dict[str, float], rating: int) -> Dict[str, float]:
        """
        Ajusta el sentimiento basado en el rating del usuario
        
        Args:
            sentiment: Diccionario con polaridad y subjetividad
            rating: Rating del usuario (1-5)
            
        Returns:
            Sentimiento ajustado
        """
        polarity = sentiment['polarity']
        subjectivity = sentiment['subjectivity']
        
        # Ajustar polaridad basado en el rating
        if rating == 1:
            # Rating 1: Muy negativo, ajustar hacia negativo
            polarity = min(polarity - 0.2, -0.3)
        elif rating == 2:
            # Rating 2: Negativo, ajustar ligeramente hacia negativo
            polarity = min(polarity - 0.1, -0.1)
        elif rating == 3:
            # Rating 3: Neutral, mantener
            pass
        elif rating == 4:
            # Rating 4: Positivo, ajustar ligeramente hacia positivo
            polarity = max(polarity + 0.1, 0.1)
        elif rating == 5:
            # Rating 5: Muy positivo, ajustar hacia positivo
            polarity = max(polarity + 0.2, 0.3)
        
        # Limitar el rango de polaridad
        polarity = max(-1.0, min(1.0, polarity))
        
        return {
            'polarity': polarity,
            'subjectivity': subjectivity
        }
    
    def generate_summary_stats(self, analyzed_df: pd.DataFrame) -> Dict:
        """Genera estadísticas resumidas del análisis"""
        summary = {
            'total_reviews': len(analyzed_df),
            'sentiment_distribution': analyzed_df['sentiment_label'].value_counts().to_dict(),
            'average_polarity': analyzed_df['polarity'].mean(),
            'average_subjectivity': analyzed_df['subjectivity'].mean(),
            'feature_requests_count': analyzed_df['feature_request'].sum(),
            'bugs_count': analyzed_df['bug_mentioned'].sum(),
            'topics_frequency': self._get_topics_frequency(analyzed_df),
            'rating_sentiment_correlation': analyzed_df['rating'].corr(analyzed_df['polarity'])
        }
        
        return summary
    
    def _get_topics_frequency(self, df: pd.DataFrame) -> Dict[str, int]:
        """Calcula la frecuencia de temas"""
        all_topics = []
        for topics in df['topics']:
            all_topics.extend(topics)
        
        return dict(Counter(all_topics))
    
    def create_visualizations(self, analyzed_df: pd.DataFrame, output_dir: str = '.'):
        """Crea visualizaciones del análisis"""
        logger.info("Generando visualizaciones...")
        
        # Configurar estilo
        plt.style.use('default')
        sns.set_palette("husl")
        
        # 1. Distribución de sentimientos
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Sentiment distribution
        sentiment_counts = analyzed_df['sentiment_label'].value_counts()
        axes[0, 0].pie(sentiment_counts.values, labels=sentiment_counts.index, autopct='%1.1f%%')
        axes[0, 0].set_title('Distribución de Sentimientos')
        
        # Rating vs Sentiment
        sentiment_rating = analyzed_df.groupby('sentiment_label')['rating'].mean()
        axes[0, 1].bar(sentiment_rating.index, sentiment_rating.values)
        axes[0, 1].set_title('Rating Promedio por Sentimiento')
        axes[0, 1].set_ylabel('Rating Promedio')
        
        # Polarity distribution
        axes[1, 0].hist(analyzed_df['polarity'], bins=20, alpha=0.7)
        axes[1, 0].set_title('Distribución de Polaridad')
        axes[1, 0].set_xlabel('Polaridad')
        axes[1, 0].set_ylabel('Frecuencia')
        
        # Topics frequency
        topics_freq = self._get_topics_frequency(analyzed_df)
        if topics_freq:
            topics_df = pd.DataFrame(list(topics_freq.items()), columns=['Tema', 'Frecuencia'])
            topics_df = topics_df.sort_values('Frecuencia', ascending=True)
            axes[1, 1].barh(topics_df['Tema'], topics_df['Frecuencia'])
            axes[1, 1].set_title('Frecuencia de Temas')
            axes[1, 1].set_xlabel('Frecuencia')
        
        plt.tight_layout()
        plt.savefig(f'{output_dir}/sentiment_analysis.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # 2. Word Cloud
        self._create_wordcloud(analyzed_df, output_dir)
        
        # 3. Interactive plots con Plotly
        self._create_interactive_plots(analyzed_df, output_dir)
        
        logger.info("Visualizaciones guardadas")
    
    def _create_wordcloud(self, df: pd.DataFrame, output_dir: str):
        """Crea word cloud de las reseñas"""
        # Combinar todos los textos
        all_text = ' '.join(df['full_text'].fillna(''))
        
        # Limpiar texto
        all_text = re.sub(r'[^\w\s]', '', all_text.lower())
        
        # Crear word cloud
        wordcloud = WordCloud(
            width=800, 
            height=400, 
            background_color='white',
            max_words=100,
            colormap='viridis'
        ).generate(all_text)
        
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Palabras más frecuentes en las reseñas')
        plt.savefig(f'{output_dir}/wordcloud.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def _create_interactive_plots(self, df: pd.DataFrame, output_dir: str):
        """Crea gráficos interactivos con Plotly"""
        
        # 1. Sentiment vs Rating scatter
        fig = px.scatter(
            df, 
            x='polarity', 
            y='rating',
            color='sentiment_label',
            title='Relación entre Sentimiento y Rating',
            labels={'polarity': 'Polaridad', 'rating': 'Rating'}
        )
        fig.write_html(f'{output_dir}/sentiment_rating_scatter.html')
        
        # 2. Topics frequency
        topics_freq = self._get_topics_frequency(df)
        if topics_freq:
            topics_df = pd.DataFrame(list(topics_freq.items()), columns=['Tema', 'Frecuencia'])
            fig = px.bar(
                topics_df, 
                x='Tema', 
                y='Frecuencia',
                title='Frecuencia de Temas Mencionados'
            )
            fig.write_html(f'{output_dir}/topics_frequency.html')
        
        # 3. Feature requests y bugs
        feature_bug_data = {
            'Tipo': ['Feature Requests', 'Bugs Reportados'],
            'Cantidad': [df['feature_request'].sum(), df['bug_mentioned'].sum()]
        }
        fig = px.bar(
            feature_bug_data, 
            x='Tipo', 
            y='Cantidad',
            title='Feature Requests vs Bugs Reportados'
        )
        fig.write_html(f'{output_dir}/feature_requests_bugs.html')
    
    def generate_report(self, analyzed_df: pd.DataFrame, output_dir: str = '.') -> str:
        """Genera un reporte completo del análisis"""
        logger.info("Generando reporte...")
        
        summary = self.generate_summary_stats(analyzed_df)
        
        # Crear reporte HTML
        report_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Análisis de Reseñas - Cheaf App</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
                .section {{ margin: 20px 0; padding: 15px; border-left: 4px solid #007bff; }}
                .metric {{ display: inline-block; margin: 10px; padding: 10px; background-color: #e9ecef; border-radius: 5px; }}
                .positive {{ color: green; }}
                .negative {{ color: red; }}
                .neutral {{ color: orange; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>📊 Análisis de Reseñas - Cheaf App</h1>
                <p>Reporte generado el {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            
            <div class="section">
                <h2>📈 Estadísticas Generales</h2>
                <div class="metric">
                    <strong>Total de Reseñas:</strong> {summary.get('total_reviews', 0)}
                </div>
                <div class="metric">
                    <strong>Polaridad Promedio:</strong> {summary.get('average_polarity', 0):.3f}
                </div>
                <div class="metric">
                    <strong>Subjetividad Promedio:</strong> {summary.get('average_subjectivity', 0):.3f}
                </div>
                <div class="metric">
                    <strong>Correlación Rating-Sentimiento:</strong> {summary.get('rating_sentiment_correlation', 0):.3f}
                </div>
            </div>
            
            <div class="section">
                <h2>😊 Distribución de Sentimientos</h2>
                <ul>
        """
        
        for sentiment, count in summary.get('sentiment_distribution', {}).items():
            percentage = (count / summary.get('total_reviews', 1)) * 100
            report_html += f"<li><strong>{sentiment.title()}:</strong> {count} ({percentage:.1f}%)</li>"
        
        report_html += """
                </ul>
            </div>
            
            <div class="section">
                <h2>🔍 Temas Más Mencionados</h2>
                <ul>
        """
        
        for topic, frequency in sorted(summary.get('topics_frequency', {}).items(), key=lambda x: x[1], reverse=True):
            report_html += f"<li><strong>{topic.title()}:</strong> {frequency} menciones</li>"
        
        report_html += """
                </ul>
            </div>
            
            <div class="section">
                <h2>🚀 Feature Requests y Bugs</h2>
                <div class="metric">
                    <strong>Feature Requests Detectados:</strong> {summary.get('feature_requests_count', 0)}
                </div>
                <div class="metric">
                    <strong>Bugs Reportados:</strong> {summary.get('bugs_count', 0)}
                </div>
            </div>
            
            <div class="section">
                <h2>📊 Visualizaciones</h2>
                <p>Las siguientes visualizaciones han sido generadas:</p>
                <ul>
                    <li>sentiment_analysis.png - Análisis de sentimiento</li>
                    <li>wordcloud.png - Nube de palabras</li>
                    <li>sentiment_rating_scatter.html - Gráfico interactivo de sentimiento vs rating</li>
                    <li>topics_frequency.html - Frecuencia de temas</li>
                    <li>feature_requests_bugs.html - Feature requests vs bugs</li>
                </ul>
            </div>
        </body>
        </html>
        """.format(**summary)
        
        # Guardar reporte
        report_path = f'{output_dir}/analysis_report.html'
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_html)
        
        logger.info(f"Reporte guardado en: {report_path}")
        return report_path
        return report_path

def main():
    """Función principal para ejecutar el análisis"""
    # Cargar datos de ejemplo (asumiendo que ya tenemos un CSV)
    try:
        df = pd.read_csv('cheaf_reviews.csv')
        analyzer = SentimentAnalyzer()
        
        # Analizar reseñas
        analyzed_df = analyzer.analyze_reviews(df)
        
        # Generar visualizaciones
        analyzer.create_visualizations(analyzed_df)
        
        # Generar reporte
        report_path = analyzer.generate_report(analyzed_df)
        
        print(f"Análisis completado. Reporte disponible en: {report_path}")
        
    except FileNotFoundError:
        print("No se encontró el archivo de reseñas. Ejecuta primero el scraper.")
    except Exception as e:
        logger.error(f"Error en el análisis: {str(e)}")

if __name__ == "__main__":
    main() 