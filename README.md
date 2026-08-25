# Lung Cancer CT Image Classification

A research/educational lung cancer CT image classification project using
Xception transfer learning and Streamlit.

## Classes

1. Normal
2. Adenocarcinoma
3. Large Cell Carcinoma
4. Squamous Cell Carcinoma

## Model

The training code uses ImageNet-pretrained Xception as a frozen feature
extractor followed by GlobalAveragePooling2D and Dense(4, softmax).

Image size: 350 x 350 RGB.

The original `best_model.hdf5` is a weights-only checkpoint. The Streamlit
application reconstructs the same architecture and then loads the weights.

## Repository structure

```text
Lung-Cancer-Prediction/
├── app.py
├── Lung_Cancer_Prediction.py
├── Lung_Cancer_Prediction.ipynb
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── model/
│   └── README.md
├── dataset/
│   └── README.md
├── hdfs/
│   └── hdfs_dataset_structure.txt
└── scripts/
    └── hdfs_upload.sh
```

## Why the model and dataset are not in GitHub

The complete CT dataset and `best_model.hdf5` are large binary files.
They are intentionally excluded from this repository using `.gitignore`.

Keep the model locally as:

```text
model/best_model.hdf5
```

Keep the dataset separately as documented in `dataset/README.md`, or store
it in HDFS using `hdfs/hdfs_dataset_structure.txt`.

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Run the Streamlit app

Make sure the model exists:

```text
model/best_model.hdf5
```

Then:

```bash
streamlit run app.py
```

Open the URL shown by Streamlit, normally:

```text
http://localhost:8501
```

## HDFS

See:

```text
hdfs/hdfs_dataset_structure.txt
```

For the upload commands and expected HDFS structure.

## Training

The original training notebook and Python script are included for reference.
The training pipeline uses image generators, normalization, horizontal flip
augmentation, Xception transfer learning, categorical crossentropy, Adam,
callbacks, and a four-class softmax output.

## Important

This project is for educational/research purposes only. It is not a medical
diagnostic system and must not be used as a substitute for professional
medical evaluation.

## Dataset

The dataset should be organized into `train`, `valid`, and `test` directories,
each containing the four classes. The complete images are not included in
this GitHub repository.

