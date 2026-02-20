import json
import os

# 1. add 10 data 
files = [
    "01_Min-Max_Normalization.ipynb",
    "02_Z-Score_Normalization.ipynb",
    "03_Distribution_Fitting_Box-Cox.ipynb",
    "04_Encoding.ipynb",
    "05_Discretization.ipynb",
    "06_Clustering_Concepts_and_Similarity.ipynb",
    "07_Clustering_Visual_Examples.ipynb",
    "08_Concept_Hierarchies.ipynb",
    "09_Sampling.ipynb",
    "10_Aggregation.ipynb"
]

# 2.  Jupyter Notebook modle
def create_nb_content(tech_name):
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"# Technique: {tech_name.replace('_', ' ')}\n", "Practicing Data Transformation techniques from class."]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "import pandas as pd\n",
                    "import numpy as np\n",
                    "import matplotlib.pyplot as plt\n",
                    "import seaborn as sns\n",
                    "from data_generator import generate_dtt_dataset, GLOBAL_SEED\n",
                    "\n",
                    "# Initialize Dataset\n",
                    "df = generate_dtt_dataset()\n",
                    "print(f'Dataset loaded with Global Seed: {GLOBAL_SEED}')\n",
                    "df.head()"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.10.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

# 3. intall
for f in files:
    with open(f, 'w', encoding='utf-8') as f_out:
        json.dump(create_nb_content(f.replace('.ipynb', '')), f_out, indent=1)
    print(f"Successfully created: {f}")