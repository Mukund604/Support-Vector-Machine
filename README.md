# Support Vector Machine (SVM) Implementation

This repository contains a Python implementation of the Support Vector Machine (SVM) classifier.

## Overview

- [Introduction](#introduction)
- [File Description](#file-description)
- [SVM Overview](#svm-overview)
- [Methods and Parameters](#methods-and-parameters)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The SVM classifier is implemented using Python's NumPy library. This implementation provides a basic version of the SVM algorithm, capable of performing binary classification tasks by finding the optimal hyperplane that separates classes in a dataset.

## File Description

- `svm_classifier.py`: Python script containing the implementation of the SVM classifier.

## SVM Overview

The SVM algorithm aims to find the optimal hyperplane that best separates two classes in a dataset. It works by maximizing the margin between classes while minimizing classification errors.

## Methods and Parameters

- `__init__`: Constructor function initializing the SVM with parameters:
  - `lr`: Learning rate for gradient descent (default = 0.001).
  - `l_param`: Regularization parameter lambda (default = 0.1).
  - `n`: Number of iterations for training (default = 1000).

- `fit`: Fit method to train the SVM model using gradient descent.
  - `X`: Training data (features).
  - `y`: Target labels for training data.

- `predict`: Prediction method to classify new data points.
  - `X`: Data points to classify.

## Usage

To use this implementation:

1. Clone the repository:

    ```
    git clone https://github.com/Mukund604/SVM-Classifier.git
    ```

2. Ensure you have Python installed along with the necessary libraries, particularly numpy.

3. Import the `SVM` class from `svm_classifier.py` into your Python environment.

4. Create an instance of the `SVM` class with desired parameters and use the `fit` method to train the model with your training data.

5. Utilize the `predict` method to make predictions on new data points.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is not licensed. The code is open-source and can be used, modified, and distributed freely.
