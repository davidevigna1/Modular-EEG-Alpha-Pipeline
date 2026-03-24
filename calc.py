import mne
import param

def pulizia_segnale(raw):
    """Applica filtri Notch e Passa-Banda"""
    raw_p = raw.copy()
    raw_p.notch_filter(param.NOTCH_FREQ, verbose=False)
    raw_p.filter(param.F_MIN, param.F_MAX, verbose=False)
    return raw_p

def estrai_alpha(raw):
    """Calcola la potenza media del ritmo Alpha"""
    psd = raw.compute_psd(fmin=param.ALPHA_RANGE[0], fmax=param.ALPHA_RANGE[1], verbose=False)
    return psd.get_data().mean()
