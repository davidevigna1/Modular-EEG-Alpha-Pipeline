import matplotlib.pyplot as plt
import param
import os

def genera_grafici(raw_dirty, raw_clean, save_path=None):
    """Confronta il prima e il dopo il filtraggio e opzionalmente salva su file"""
    sfreq = raw_dirty.info['sfreq']
    stop = int(param.DURATION * sfreq)
    
    times = raw_dirty.times[:stop]
    data_dirty = raw_dirty.get_data(picks=0, stop=stop) # Prendiamo il primo canale
    data_clean = raw_clean.get_data(picks=0, stop=stop) # Prendiamo il primo canale
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    
    # Segnale originale
    ax1.plot(times, data_dirty[0], color='red', linewidth=0.8, label="Canale 1")
    ax1.set_title("Segnale Originale (Sporco)")
    ax1.set_ylabel("Ampiezza (V)")
    ax1.legend()
    
    # Segnale filtrato
    ax2.plot(times, data_clean[0], color='green', linewidth=1, label="Canale 1")
    ax2.set_title("Segnale Elaborato (Pulito)")
    ax2.set_ylabel("Ampiezza (V)")
    ax2.set_xlabel("Tempo (s)")
    ax2.legend()
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
        print(f"🖼️ Grafico salvato come immagine in: {save_path}")
        
    plt.show()
