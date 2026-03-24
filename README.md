# EEG-Monitor Project

A Python-based framework for EEG signal processing, visualization, and report generation.

## Project Structure and File Descriptions

This project is organized into modular components to ensure portability and ease of maintenance. Below is a detailed presentation of what each file does:

### 1. [main.py](file:///c:/Users/Utente/Desktop/Biotech/antigravity/EEG-Monitor/main.py)
**The Project Coordinator.**  
This is the entry point of the application. It orchestrates the entire analysis pipeline:
- Calculates absolute paths for cross-platform compatibility.
- Loads raw EEG data (supporting `.fif` and other formats via MNE-Python).
- Executes the signal cleaning and extraction processes.
- Manages the saving of results and the generation of final reports (CSV and HTML).

### 2. [calc.py](file:///c:/Users/Utente/Desktop/Biotech/antigravity/EEG-Monitor/calc.py)
**The Processing Engine.**  
Dedicated to signal processing and feature extraction:
- **[pulizia_segnale](file:///c:/Users/Utente/Desktop/Biotech/antigravity/EEG-Monitor/calc.py#4-10)**: Applies filters (Notch at 50Hz and Band-pass) to remove electrical noise and isolate relevant frequencies.
- **[estrai_alpha](file:///c:/Users/Utente/Desktop/Biotech/antigravity/EEG-Monitor/calc.py#11-15)**: Calculates the average power of the Alpha rhythm (8-13 Hz) using Power Spectral Density (PSD) computation.

### 3. [graphics.py](file:///c:/Users/Utente/Desktop/Biotech/antigravity/EEG-Monitor/graphics.py)
**The Visualization Module.**  
Handles the graphical representation of the data:
- Core function: [genera_grafici](file:///c:/Users/Utente/Desktop/Biotech/antigravity/EEG-Monitor/graphics.py#5-37).
- Creates side-by-side plots comparing the raw (noisy) signal with the cleaned version.
- Automatically saves the visualizations as `.png` images for inclusion in reports.

### 4. [param.py](file:///c:/Users/Utente/Desktop/Biotech/antigravity/EEG-Monitor/param.py)
**The Configuration Hub.**  
Centralizes all analysis parameters and constants:
- Frequency ranges (Alpha, Beta).
- Filtering thresholds and durations.
- Output file names and column structures.
- Use this file to tune the analysis without modifying the core logic.

### 5. [createfile.py](file:///c:/Users/Utente/Desktop/Biotech/antigravity/EEG-Monitor/createfile.py)
**Data Persistence & Reporting.**  
Manages how the results are saved and presented:
- **CSV Logging**: Appends trial results into a persistent spreadsheet, handling folder creation automatically.
- **HTML Reporting**: Generates a professional, styled biological report containing metadata, results, and the corresponding signal plots.

---
## Getting Started
To run the analysis, ensure you have the required dependencies (`mne`, `pandas`, `matplotlib`) and execute:
```bash
python main.py
```
The results will be available in the `/reports` directory.
