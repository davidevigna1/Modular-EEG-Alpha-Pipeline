import pandas as pd
from datetime import datetime
import os

# Calcolo percorsi assoluti per evitare problemi di CWD
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
NOME_FILE = "report_neuro_analisi.csv"

def salva_risultati(valore_alpha, fmin=None, fmax=None, durata=None, nome_paziente="Paziente Ignoto"):
    """Crea la cartella 'reports' (percorso assoluto) e salva il file CSV"""
    
    percorso_completo = os.path.join(REPORTS_DIR, NOME_FILE)

    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)
        print(f"📁 Cartella '{REPORTS_DIR}' verificata/creata.")

    nuovo_dato = {
        "Data_Ora": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Paziente": [nome_paziente],
        "F_Min (Hz)": [fmin],
        "F_Max (Hz)": [fmax],
        "Durata (s)": [durata],
        "Indice_Alpha": [valore_alpha],
        "Qualita": ["Segnale Filtrato"]
    }
    df = pd.DataFrame(nuovo_dato)
    
    if not os.path.isfile(percorso_completo):
        df.to_csv(percorso_completo, index=False, sep=';')
    else:
        df.to_csv(percorso_completo, mode='a', header=False, index=False, sep=';')
        
    print(f"✅ Risultato salvato in: {percorso_completo}")
    
    # Restituiamo il dizionario semplificato (senza liste) per il report
    return {k: v[0] for k, v in nuovo_dato.items()}

def genera_report_html(dati, percorso_immagine, output_path):
    """Genera un report HTML elegante con dati e immagine incorporata"""
    html_content = f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <title>Report Analisi Neuro-Biotech</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; color: #333; margin: 0; padding: 20px; }}
            .container {{ max-width: 900px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
            .metadata {{ display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 30px; background: #ecf0f1; padding: 15px; border-radius: 5px; }}
            .item {{ flex: 1; min-width: 200px; }}
            .label {{ font-weight: bold; color: #7f8c8d; display: block; font-size: 0.9em; }}
            .value {{ font-size: 1.1em; color: #2c3e50; }}
            .result {{ text-align: center; margin: 40px 0; padding: 20px; background: #e8f4fd; border-left: 5px solid #3498db; }}
            .result .val {{ font-size: 2.5em; font-weight: bold; color: #3498db; }}
            .viz {{ text-align: center; margin-top: 30px; }}
            img {{ max-width: 100%; border-radius: 5px; box-shadow: 0 4px 8px rgba(0,0,0,0.2); }}
            footer {{ margin-top: 50px; font-size: 0.8em; color: #95a5a6; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧠 Report Analisi Neuro-Biotech</h1>
            
            <div class="metadata">
                <div class="item"><span class="label">Data Ora</span><span class="value">{dati['Data_Ora']}</span></div>
                <div class="item"><span class="label">Paziente</span><span class="value">{dati['Paziente']}</span></div>
                <div class="item"><span class="label">Filtro</span><span class="value">{dati['F_Min (Hz)']} - {dati['F_Max (Hz)']} Hz</span></div>
                <div class="item"><span class="label">Durata</span><span class="value">{dati['Durata (s)']} secondi</span></div>
            </div>

            <div class="result">
                <span class="label">Potenza Alpha Rilevata</span>
                <div class="val">{dati['Indice_Alpha']:.2e}</div>
                <span class="value">Stato: <strong>{dati['Qualita']}</strong></span>
            </div>

            <div class="viz">
                <h2>📈 Visualizzazione Segnale</h2>
                <img src="{os.path.basename(percorso_immagine)}" alt="Grafico Analisi">
            </div>

            <footer>Analisi generata automaticamente dal Sistema Neuro-Biotech Monitor</footer>
        </div>
    </body>
    </html>
    """
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"🌐 Smart Report HTML generato con successo: {output_path}")

if __name__ == "__main__":
    salva_risultati(0.000045, fmin=1.0, fmax=45.0, durata=5)
