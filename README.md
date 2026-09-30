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

Todos los datasets se cargan desde fuentes públicas (scikit-learn, seaborn, OpenML, Hugging Face o URLs públicas), así que no hace falta ningún dato local.

```bash
uv sync
uv run jupyter lab
```
