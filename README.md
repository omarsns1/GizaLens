# GizaLens 📜

**Exploring machine learning for historical Arabic handwriting and digital humanities.**

GizaLens is an independent research project exploring how machine learning can make historical Arabic manuscripts more accessible, searchable, and easier to study.

The project focuses on preparing handwritten documents for recognition: organising manuscript images, extracting existing transcriptions, generating line-level image crops, and investigating the challenges of Arabic Handwritten Text Recognition (HTR).

> **Dataset note:** The current dataset contains historical Arabic handwritten material. It has not been established as a collection of Giza excavation records. GizaLens is an independent project and is not affiliated with any archaeological institution.

## Research and development

Work completed so far:

- Built a data-inspection pipeline to organise manuscript images and extract their paired DOCX transcriptions.
- Processed **40 manuscript pages**, generating **575 line-level image crops** for recognition experiments.
- Evaluated an Arabic handwriting-recognition system.
- Investigated image-to-transcription alignment and identified limitations in using page-level text as ground truth for individual line crops.
- Documented segmentation and alignment issues rather than treating preliminary accuracy measurements as reliable.
- Developed an interactive Streamlit interface to explore manuscript images alongside their transcriptions.

## The manuscripts

The dataset contains historical Arabic scholarly and religious texts, including works relating to hadith, Islamic theology, jurisprudence, and history.

The project explores how machine learning could help preserve access to this material by making handwritten sources easier to inspect and eventually search.

## Live application

The Streamlit application provides an interactive interface for browsing manuscript images and viewing their available transcriptions.

**Current status:** This is a data-inspection prototype, not yet a fully functioning handwriting-recognition system. It does not currently generate OCR/HTR predictions from uploaded images.

## Repository structure

\`\`\`text
GizaLens/
├── app.py
├── requirements.txt
└── data/
    └── raw/
        └── Historical Arabic Handwritten Text Recognition Dataset/
            ├── Book1/
            ├── Book2/
            ├── Book3/
            └── Book4/
\`\`\`

The repository includes a small sample of the dataset for the live demo. The wider preprocessing and evaluation experiments
