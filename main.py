import mne
import param
import calc
import graphics
import createfile
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

# --- CONFIGURAZIONE UTENTE ---
# Cambia questo percorso per caricare i tuoi file (.fif, .edf, .set, .cnt, ecc.)
# Se lasci None, il programma userà il segnale di esempio di MNE.
PERCORSO_FILE = None

# -----------------------------

print("🧠 Analisi avviata...")

# 1. Caricamento Dati
if PERCORSO_FILE is None:
    data_path = mne.datasets.sample.data_path()
    raw_fname = data_path / 'MEG' / 'sample' / 'sample_audvis_raw.fif'
    nome_segnale = "Esempio_MNE"
else:
    raw_fname = PERCORSO_FILE
    nome_segnale = os.path.basename(raw_fname).split('.')[0]

print(f"📂 Caricamento file: {nome_segnale}")
raw = mne.io.read_raw_fif(raw_fname, preload=True, verbose=False)
raw.pick_types(eeg=True)

# 2. Elaborazione
raw_pulito = calc.pulizia_segnale(raw)

# 3. Analisi
potenza_alpha = calc.estrai_alpha(raw_pulito)
print(f"📊 Potenza Alpha Rilevata: {potenza_alpha:.2e}")

# 4. Archivio (Percorsi Assoluti)
print("📂 Salvataggio dati e grafici...")
timestamp = datetime.now().strftime('%Y%m%d_%H%M')
nome_grafico = f"grafico_{nome_segnale}_{timestamp}.png"
percorso_grafico = os.path.join(REPORTS_DIR, nome_grafico)

# Salviamo i risultati tecnici nel CSV
dati_report = createfile.salva_risultati(
    potenza_alpha, 
    fmin=param.F_MIN, 
    fmax=param.F_MAX, 
    durata=param.DURATION,
    nome_paziente=nome_segnale  # Usiamo il nome del file come nome paziente
)

# 5. Grafica (Salvataggio immagine)
graphics.genera_grafici(raw, raw_pulito, save_path=percorso_grafico)

# 6. Report HTML FINALE (Per aprire con il Browser)
nome_report = f"REPORT_{nome_segnale}_{timestamp}.html"
percorso_report = os.path.join(REPORTS_DIR, nome_report)
createfile.genera_report_html(dati_report, percorso_grafico, percorso_report)

print(f"\n✅ ANALISI COMPLETATA!")
print(f"📍 Il tuo report è qui: {REPORTS_DIR}")
print(f"🌐 Fai DOPPIO CLIC sul file '{nome_report}' per vederlo con Chrome o Edge.")
