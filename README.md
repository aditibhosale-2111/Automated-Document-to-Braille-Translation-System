## Overview

Accessibility tools for visually impaired individuals often provide limited support for regional Indian languages and typically rely on expensive Braille embossing hardware. This project addresses these challenges by providing an automated bilingual Braille conversion system for both Marathi (Devanagari) and English documents.

The system converts PDF documents into print-ready Braille output that can be printed using a standard dot-matrix printer, significantly reducing the cost of Braille document production for schools, NGOs, and assistive technology centers.

## Features

* Bilingual support for Marathi (Devanagari) and English
* PDF text extraction and processing
* Hybrid OCR pipeline for scanned documents
* AI-assisted OCR error correction
* Automatic language detection
* Unicode normalization
* Bharati Braille character mapping
* Braille PDF generation
* Horizontally mirrored Braille image generation for embossing
* Streamlit-based user interface
* Low-cost alternative to commercial Braille embossers

## Technology Stack

# OCR and Text Processing

* Tesseract OCR
* EasyOCR
* TrOCR (Microsoft Transformer-based OCR)

# Application Framework

* Streamlit

# PDF Processing

* PyMuPDF (fitz)
* ReportLab

# Image Processing

* OpenCV
* Pillow

# AI Integration

* OpenAI API (for OCR error correction)

## System Workflow

1. Upload PDF document
2. Extract text using OCR pipeline
3. Detect document language
4. Normalize Unicode text
5. Convert text into Bharati Braille encoding
6. Generate Braille PDF output
7. Create mirrored Braille image for embossing
8. Export print-ready Braille documents

## Project Structure

```text
├── app.py
├── core/
├── utils/
├── data/
├── fonts/
├── output/
└── .venv/
```
## Applications

* Schools for visually impaired students
* NGOs working in accessibility
* Braille publishing centers
* Educational institutions
* Assistive technology laboratories
* Regional language accessibility initiatives

## Advantages

* Supports Marathi and English documents
* Low-cost Braille production
* No dedicated Braille embosser required
* Faster document conversion
* AI-assisted OCR correction
* User-friendly web interface

## Future Enhancements

* Support for additional Indian languages
* Speech-to-Braille conversion
* Mobile application support
* Cloud deployment
* Multi-language OCR optimization

## Authors

Aditi Bhosale

This project is intended for educational and research purposes.
