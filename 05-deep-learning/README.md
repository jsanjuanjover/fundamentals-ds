# 05 · Deep Learning

Redes neuronales con PyTorch: de la red densa a los modelos generativos. Los notebooks son independientes del tipo de dato; el uso específico con texto (traducción, modelos de lenguaje preentrenados, análisis de sentimientos) está en [06 · NLP](../06-nlp/).

## Notebooks

| # | Notebook | Temas |
|---|---|---|
| 01 | [Redes neuronales densas](01-redes-neuronales-densas.ipynb) | Perceptrón multicapa, funciones de activación, retropropagación, funciones de pérdida, optimizadores (SGD, Adam), bucle de entrenamiento en PyTorch |
| 02 | [Entrenamiento y regularización](02-entrenamiento-y-regularizacion.ipynb) | Sobreajuste, *dropout*, normalización por lotes, parada temprana, tasa de aprendizaje, búsqueda de hiperparámetros |
| 03 | [Redes convolucionales](03-redes-convolucionales.ipynb) | Convolución, *padding* y *stride*, *pooling*, CNN pequeña para clasificar imágenes |
| 04 | [Transfer learning](04-transfer-learning.ipynb) | Arquitecturas CNN profundas, modelos preentrenados, extracción de características y *fine-tuning* |
| 05 | [Autoencoders](05-autoencoders.ipynb) | Codificador y decodificador, espacio latente, error de reconstrucción, detección de anomalías |
| 06 | [Redes recurrentes](06-redes-recurrentes.ipynb) | RNN, LSTM y GRU, gradiente que se desvanece, ventanas deslizantes y líneas base ingenuas, series multivariantes, predicción a varios pasos, atención sobre los estados ocultos |
| 07 | [Atención y transformers](07-atencion-y-transformers.ipynb) | Mecanismo de atención, autoatención multicabeza, máscaras causal y de *padding*, codificación posicional, arquitectura del *transformer*, modelo de lenguaje y perplejidad, comparación con LSTM |
| 08 | [GAN](08-gan.ipynb) | Generador y discriminador, juego minimax y pérdida no saturante, DCGAN, inestabilidad y colapso de modos, evaluación (distancia de Fréchet, diversidad), interpolación latente |
| 09 | `09-modelos-de-difusion` | Proceso directo (ruido) e inverso (eliminación de ruido), DDPM, comparación con las GAN |
