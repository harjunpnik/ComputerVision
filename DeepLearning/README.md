# Deep Learning

Build  a  Keras  (deep learning) model where  Tensorflow  works  in  backend. This  project is  to carry out on a hosuing price data set. The objective of this project is to predict of a house price above the median or not.

1. Data source: https://drive.google.com/file/d/1GfvKA0qznNVknghV4botnNxyH-KvODOC/view
2. Carry out some explanatory analysis to get to know your data.
3. If you need pre-processing (normalization) of the data, you can use MinMaxScaler.
4. Specify model architecture: 

    a. Input layer with Dense layer, 32 nodes, “relu” activation function

    b. One hidden layer with Dense layer, 32 nodes, “relu” activation function

    c. Output is with Dense layer, singlenode, “sigmoid” activation function
5. Compile the model:

    a.“sgd”optimizer

    b.Loss is “binary_crossentropy” 
6. Fitting the model: 

    a.Epochs 100

    b.Batch_size = 32 
7. Indicate the accuracy and loss of the model
8. Evaluation result