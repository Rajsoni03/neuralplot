# Neural Plot

[![PyPI version](https://img.shields.io/badge/pypi-v%200.0.8-green.svg)](https://pypi.org/project/neuralplot/)
[![Python version](https://img.shields.io/badge/python-v3.6%20v3.7%20v3.8-red.svg)](https://www.python.org/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/Rajsoni03/neuralplot/blob/master/LICENSE)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Rajsoni03/neuralplot/blob/master/others/Example%20Notebook.ipynb) 

Neural Plot is a python library for visualizing Neural Networks.
It helps to plot Keras/Tensorflow model with matplotlib backend.

[![NeuralPlot](https://i.ytimg.com/an_webp/CsWnmWdk5-g/mqdefault_6s.webp?du=3000&sqp=CKjGj48G&rs=AOn4CLDi530RQLCprZL1_Gec3eflE-Gf8Q)](https://youtu.be/CsWnmWdk5-g "NeuralPlot")
<br>https://youtu.be/CsWnmWdk5-g


## Installation

Run the following to install:
```sh
$ pip install neuralplot
```


## Example

```python
# Importing Libraries
from neuralplot import ModelPlot
import tensorflow as tf
import numpy as np
```
```python
# Uncomment while using Colab.
# %matplotlib inline 

# Uncomment while using jupyter notebook. This feature is not working in colab.
%matplotlib notebook 
```
```python
#Creating Model
X_input = tf.keras.layers.Input(shape=(32,32,3))
X = tf.keras.layers.Conv2D(4, 3, activation='relu')(X_input)
X = tf.keras.layers.MaxPool2D(2,2)(X)
X = tf.keras.layers.Conv2D(16, 3, activation='relu')(X)
X = tf.keras.layers.MaxPool2D(2,2)(X)
X = tf.keras.layers.Conv2D(8, 3, activation='relu')(X)
X = tf.keras.layers.MaxPool2D(2,2)(X)
X = tf.keras.layers.Flatten()(X)
X = tf.keras.layers.Dense(10, activation='relu')(X)
X = tf.keras.layers.Dense(2, activation='softmax')(X)

model = tf.keras.models.Model(inputs=X_input, outputs=X)
```
```python
modelplot = ModelPlot(model=model, grid=True, connection=True, linewidth=0.1)
modelplot.show()
```
[![modelplot with grid](https://raw.githubusercontent.com/Rajsoni03/neuralplot/master/others/images/Image-01.png)]()

```python
modelplot = ModelPlot(model=model, grid=False, connection=True, linewidth=0.1)
modelplot.show()
```
[![modelplot with grid](https://raw.githubusercontent.com/Rajsoni03/neuralplot/master/others/images/Image-02.png)]()


License
----
MIT


