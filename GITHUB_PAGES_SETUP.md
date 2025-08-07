# 🚀 Configuración de GitHub Pages - Guía Completa

## 📋 **PASOS PARA ACTIVAR GITHUB PAGES**

### **Paso 1: Ve a tu repositorio**
1. Abre tu navegador
2. Ve a: https://github.com/isabelaosoriomartinez/propuesta-cheaf

### **Paso 2: Configura GitHub Pages**
1. En tu repositorio, haz clic en **Settings** (Configuración) en la parte superior
2. En el menú lateral izquierdo, busca y haz clic en **Pages**
3. En la sección **Source**, selecciona **Deploy from a branch**
4. En **Branch**, selecciona **master** y **/(root)**
5. Haz clic en **Save**

### **Paso 3: Verifica la activación**
- Después de guardar, verás un mensaje verde que dice "Your site is published at..."
- El link será: `https://isabelaosoriomartinez.github.io/propuesta-cheaf/`

## 🔗 **LINKS IMPORTANTES**

### **Tu Landing Page:**
```
https://isabelaosoriomartinez.github.io/propuesta-cheaf/
```

### **Repositorio:**
```
https://github.com/isabelaosoriomartinez/propuesta-cheaf
```

### **Archivos principales:**
- 📄 **Landing Page:** `index.html`
- 🎨 **Estilos:** `styles.css`
- 📊 **Análisis Técnico:** `scraping_technical_analysis.md`
- 📈 **Resultados:** `cheaf_review_analysis.md`
- 👤 **Presentación:** `quien_soy_isabela.md`

## ⏱️ **TIEMPO DE ACTIVACIÓN**
- **Normalmente:** 2-5 minutos
- **Máximo:** 10-15 minutos
- **Si no funciona:** Verifica que hayas seleccionado la rama `master`

## 🧪 **VERIFICAR QUE FUNCIONE**

### **Opción 1: Script automático**
```bash
py check_github_pages.py
```

### **Opción 2: Verificación manual**
1. Abre el link en tu navegador
2. Deberías ver tu landing page con:
   - Header con gradiente
   - Tu foto (reemplaza `Foto.jpg`)
   - Tres tarjetas con enlaces
   - Diseño responsive

## 📸 **REEMPLAZAR LA FOTO**

### **Paso 1: Agregar tu foto**
1. Coloca tu foto en la carpeta del proyecto
2. Nómbrala `Foto.jpg`
3. Asegúrate de que sea cuadrada (recomendado: 300x300px)

### **Paso 2: Subir al repositorio**
```bash
git add Foto.jpg
git commit -m "Add profile photo"
git push origin master
```

## 🎯 **CONTENIDO DE TU LANDING PAGE**

### **Sección Principal:**
- **Nombre:** Isabela Osorio Martínez
- **Rol:** Data Analyst & Business Intelligence Specialist
- **LinkedIn:** https://www.linkedin.com/in/isabelaosoriomartinez/

### **Tres Tarjetas:**
1. **👤 Quién Soy:** Presentación personal y experiencia
2. **🔧 Análisis Técnico:** Metodología y stack tecnológico
3. **📊 Análisis Cheaf:** Resultados y recomendaciones de producto

## 🚨 **SOLUCIÓN DE PROBLEMAS**

### **Si la página no carga:**
1. Verifica que GitHub Pages esté habilitado en Settings
2. Espera 10-15 minutos
3. Limpia el caché del navegador
4. Intenta en modo incógnito

### **Si no aparece tu foto:**
1. Verifica que el archivo se llame exactamente `Foto.jpg`
2. Asegúrate de que esté en la raíz del proyecto
3. Haz commit y push del archivo

### **Si los enlaces no funcionan:**
1. Verifica que los archivos `.md` estén en el repositorio
2. Los enlaces funcionan mejor en GitHub Pages que en el repositorio local

## 🎉 **¡LISTO!**

Una vez configurado, tu landing page estará disponible en:
```
https://isabelaosoriomartinez.github.io/propuesta-cheaf/
```

¡Perfecto para compartir en tu CV, LinkedIn o presentaciones profesionales!
