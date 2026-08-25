# Dataset

The complete CT-image dataset is intentionally excluded from this GitHub repository because
of its large size.

Expected local/HDFS structure:

dataset/
├── train/
│   ├── normal/
│   ├── adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib/
│   ├── large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa/
│   └── squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa/
├── valid/
│   ├── normal/
│   ├── adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib/
│   ├── large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa/
│   └── squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa/
└── test/
    ├── normal/
    ├── adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib/
    ├── large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa/
    └── squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa/

See hdfs/hdfs_dataset_structure.txt for HDFS commands.
