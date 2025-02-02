# RiceDatathon2025

## Project Summary
In this project, we explore EEG data from healthy individuals and individuals with psychiatric disorders including addictive disorder, anxiety disorder, mood disorder, obsessive compulsive disorder, schizophrenia, and trauma and stress related disorder. 

The data used in this project consists of minimal demographic data and two types of EEG data collected from 19 electrodes: power spectrum density (PSD) and coherence. 

![Power Spectrum Density Averages across Bands](https://github.com/benwillallen/RiceDatathon2025/blob/main/EDA/Visualizations/PSD.png)

After data cleaning and exploratory data analysis, we trained and evaluated the performances of several multi-class classification models to predict an individual's psychiatric disorder (or lack thereof) using PSD and coherence data. We also looked into feature engineering, such as hemisphere asymmetries, specifically frontal alpha asymmetry, an indicator associated with disorders such as depression. 

We started with classical machine learning models, including tree-based models such as random forest and light gradient-boosting machine (LightGBM). Then, we moved on to more complex neural networks.

## Getting Started
Install required Python packages with the following commands:
```
pip install pandas
pip install numpy
pip install matplotlib
pip install scikit-learn
pip install mne
pip install torch
pip install torchviz
pip install torch
pip install torchsummary
pip install torch_geometric
pip install imblearn
pip install lightgbm
```

## Model
Our highest performing model was in `gnn5.ipynb`, a combination of a graph convolutional neural network and a standard convolutional neural network. This consisted of the following components:

- Six graph neural networks for each band, with edges connecting the locations with the maximum average coherence on that band. Power density values were convolved across these edges to create 128 features each.
- Six standard convolutional neural networks for each band. These processed the raw coherence (COH) data in a 19x19 table for each band, turning them into features to be concatenated with their respected graph neural net features
- Each band's concatenated results were put through a dense layer before all bands were concatenated for further processing by dense layers.
- The output is 7 logits that can be used to determine mental illness with a `~38.5%` test accuracy!

## Innovative Design
We used our domain-specific knowledge by using the average coherence values to give the graph networks an idea of the physical structure of the brain and how components with high coherence interact with each other. Therefore, learnable structures would likely be found across these edges. Additionally, since the coherence grid also contains spatial data because of the ordering of the electrodes, using a convolutional neural network to find coherence structures also made sense.

## Contributors
Ben Allen, Jonathan Mak, Ian Rundle, Lauren Yu (Rice University)
