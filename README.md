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

## Contributors
Ben Allen, Jonathan Mak, Ian Rundle, Lauren Yu (Rice University)
