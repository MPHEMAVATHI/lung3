# Project packaging notes

This GitHub package is deliberately kept small.

Excluded:
- best_model.hdf5
- CT dataset image files

Included:
- Streamlit inference app
- original notebook
- original training script
- requirements
- README
- HDFS structure and commands
- .gitignore

Before local inference, copy the trained weights to:
model/best_model.hdf5
