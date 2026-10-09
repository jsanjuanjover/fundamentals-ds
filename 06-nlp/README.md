# 06 · NLP

Procesamiento del lenguaje natural, desde las representaciones clásicas de texto hasta los transformers (Hugging Face). Las arquitecturas generales (recurrentes, atención, *transformers*) se explican en [05 · Deep Learning](../05-deep-learning/); aquí se aplican al texto.

## Notebooks

| # | Notebook | Temas |
|---|---|---|
| 01 | [Preprocesamiento de texto](01-preprocesamiento-de-texto.ipynb) | Tokenización, normalización, etiquetado gramatical (PoS), lematización y *stemming*, palabras vacías, ley de Zipf |
| 02 | [N-gramas y colocaciones](02-n-gramas-y-colocaciones.ipynb) | N-gramas, colocaciones, información mutua puntual (PMI), razón de verosimilitud, términos compuestos |
| 03 | [Representación vectorial y TF-IDF](03-representacion-vectorial-tfidf.ipynb) | Bolsa de palabras, TF-IDF, similitud del coseno entre documentos |
| 04 | [Embeddings de palabras](04-embeddings-de-palabras.ipynb) | Word2Vec, GloVe, distancias semánticas, analogías, embeddings preentrenados |
| 05 | [Detección de temas](05-deteccion-de-temas.ipynb) | LDA, similitud semántica con WordNet y ConceptNet, comparación con la similitud de los embeddings |
| 06 | [Clasificación de texto](06-clasificacion-de-texto.ipynb) | TF-IDF con regresión logística, Naive Bayes, SVM y Random Forest; evaluación (curva ROC, métricas por clase) |
| 07 | `07-analisis-de-sentimientos` | Componentes de una opinión (objetivo, aspecto, polaridad, autor), léxicos de sentimiento, análisis por aspectos |
| 08 | `08-sentimientos-con-deep-learning` | BiLSTM, embeddings contextuales de BERT, comparación con el modelo clásico |
| 09 | `09-traduccion-automatica` | Codificador-decodificador (*seq2seq*), embeddings preentrenados, evaluación de la traducción |
| 10 | `10-modelos-de-lenguaje-preentrenados` | BERT y modelos fundacionales con Hugging Face, completar huecos, embeddings contextuales, *fine-tuning*, eficiencia |
| 11 | `11-reconocimiento-de-entidades` | NER con spaCy, detección por patrones, entrenar un tipo de entidad nuevo, evaluación |
| 12 | `12-enlace-de-entidades` | Enlace a bases de conocimiento (DBpedia), desambiguación |
