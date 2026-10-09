# Fundamentals

Apuntes en forma de notebooks de Jupyter sobre los fundamentos de la ciencia de datos. Cada notebook trata un único concepto y sigue la misma estructura:

1. **Idea clave**: qué problema resuelve y cuándo usarlo
2. **Conceptos importantes**: intuición, definiciones y matemáticas mínimas
3. **Código**: ejemplos mínimos con datasets públicos
4. **Parámetros importantes y errores comunes**
5. **Comparación** con métodos relacionados
6. **Referencias**

## Secciones

| Sección | Contenido |
|---|---|
| [01 · Python](01-python/) | Python y el ecosistema científico |
| [02 · Estadística](02-estadistica/) | Estadística descriptiva e inferencial, regresión |
| [03 · Preparación de datos](03-preparacion-datos/) | Limpieza, imputación, transformación, datos desbalanceados |
| [04 · Machine Learning](04-machine-learning/) | Flujo de trabajo, evaluación, métodos supervisados y no supervisados |
| [05 · Deep Learning](05-deep-learning/) | Redes neuronales con PyTorch |
| [06 · NLP](06-nlp/) | De la representación de texto a los transformers |

Los notebooks son autocontenidos: cada uno repite el preprocesamiento que necesita y enlaza al notebook de preparación de datos correspondiente para los detalles.

## Cómo ejecutar los notebooks

Todos los datasets se cargan desde fuentes públicas (scikit-learn, seaborn, OpenML, torchvision, Hugging Face o URLs públicas), así que no hace falta ningún dato local. Los que se descargan (por ejemplo, las imágenes de deep learning, o los vectores GloVe y las relaciones de ConceptNet de NLP) se guardan en una carpeta `data/` junto al notebook, excluida del repositorio.

```bash
uv sync
uv run jupyter lab
```

`uv sync` instala todas las dependencias del `pyproject.toml`, incluidos PyTorch y torchvision. En Linux, PyTorch se instala con soporte para CUDA, así que la primera instalación descarga varios GB y puede tardar unos minutos. También instala el modelo de inglés de spaCy (`en_core_web_sm`); los recursos de NLTK (tokenizador, etiquetador, WordNet, palabras vacías, léxicos de sentimiento) los descarga cada notebook de NLP la primera vez que se ejecuta.

Los notebooks de deep learning funcionan en CPU, pero son mucho más rápidos con una GPU NVIDIA (se usa automáticamente si está disponible). La primera vez que se ejecuta cada uno descarga su dataset y, si los usa, los pesos preentrenados; las ejecuciones siguientes reutilizan lo descargado.
