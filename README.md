# Modular-EEG-Alpha-Pipeline
Pipeline modulare per l'analisi automatizzata di segnali EEG e l'estrazione del ritmo Alpha. Il sistema integra filtri digitali per la rimozione di artefatti e trasforma dati grezzi in parametri quantitativi tramite analisi spettrale. Gestisce l'intero ciclo del dato, automatizzando report grafici e archiviazione.

To ensure scalability and clean code, the pipeline is divided into five specialized modules:

Param.ipynb (Configuration Engine): This is the "control panel" of the project. It centralizes all technical constants, such as frequency boundaries (1-45 Hz), notch filters (50 Hz), and quality thresholds. This allows for rapid system tuning without the risk of altering the core processing logic.

calc.ipynb (Processing & Analytics): The mathematical heart of the pipeline. Using the MNE-Python library, it performs the digital signal processing (DSP) required to clean the data and calculates the energy of the brainwaves.

graphics.ipynb (Visual Reporting): Handles the validation of the results. It generates high-fidelity plots to compare raw signals with processed data, ensuring that artifacts like muscle movements or electrical noise have been correctly removed.

createfile.ipynb (Data Persistence): The storage manager. It automatically creates a /reports directory and manages the saving of results into PNG and HTML formats, ensuring that every analysis is documented and archived with a timestamp.

main.ipynb (The Orchestrator): The entry point of the software. It coordinates the execution flow, calling functions from the other modules in the correct sequence to complete the analysis pipeline.
