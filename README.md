# Data Transformation Techniques

This project is for my **Machine Learning Programming** class. 
The goal is to practice 10 different ways to change and reduce data for machine learning.

## 10 Techniques Included:
1. **Min-Max Normalization**: Scales data between 0 and 1.
2. **Z-Score Normalization**: Centers data around 0 with a spread of 1.
3. **Distribution Fitting (Box-Cox)**: Fixes skewed data into a normal shape.
4. **Encoding**: Changes category words into numbers.
5. **Discretization**: Puts numbers into groups (bins).
6. **Clustering Concepts**: Finds similar data points.
7. **Clustering Visuals**: Shows the "Dendrogram" tree picture.
8. **Concept Hierarchies**: Rolls up small details (City) into big groups (Region).
9. **Data Reduction by Sampling**: Picks a small, fair group of data.
10. **Data Reduction by Aggregation**: Summarizes detailed data (Minutes to Hours).

## 📚 Project Structure & Techniques

I have organized the 10 techniques into two main categories based on our class lectures:

### 1. Data Transformation
The goal is to prepare data and make it structured for Machine Learning models.
* **Normalization**: 
    - `01 Min-Max`: Linear scaling (0 to 1).
    - `02 Z-Score`: Based on Mean and Standard Deviation.
    - `03 Distribution Fitting (Box-Cox)`: Makes data look like a Normal Distribution.
* **Encoding & Binning**:
    - `04 Encoding`: Changes words to numbers (Label/One-Hot).
    - `05 Discretization`: Changes continuous numbers into bins.
* **Groups & Hierarchy**:
    - `06 & 07 Clustering`: Groups similar objects together (07 focuses on the Dendrogram).
    - `08 Concept Hierarchies`: Rolls up details (City) to high-level concepts (Province).

### 2. Data Reduction
The goal is to reduce the data size while keeping important information.
* **09 Sampling**: Uses a representative subset (SRSWOR or Stratified Sampling).
* **10 Aggregation**: Replaces raw data with summary statistics (e.g., Min to Hour).
---

## I. Data Transformation (Preparing the Structure)
| Category | Technique | Key Purpose |
| :--- | :--- | :--- |
| **Normalization** | 01, 02, 03 | Scale numbers and fix data shapes (Normal Distribution). |
| **Encoding** | 04 | Turn categories (text) into numbers. |
| **Discretization** | 05 | Slice continuous data into discrete intervals (bins). |
| **Clustering** | 06, 07 | Find similar groups and visualize them (Dendrogram). |
| **Hierarchy** | 08 | Roll up detailed data into general concepts. |

---

## II. Data Reduction (Reducing Data Volume)
| Category | Technique | Key Purpose |
| :--- | :--- | :--- |
| **Sampling** | 09 | Pick a smaller, fair group of data (SRS or Stratified). |
| **Aggregation** | 10 | Use SUM/AVG to replace millions of detailed rows. |

---


## How to use:
1. Run `data_generator.py` to create the practice data.
2. Open the `.ipynb` files in VS Code.
3. Select the `venv` kernel to run the code.

## Tools used:
* Python (Pandas, Numpy, Scikit-Learn, Scipy)
* Jupyter Notebook
