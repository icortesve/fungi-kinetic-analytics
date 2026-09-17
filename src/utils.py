import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

def modelo_logistico(t, K, mu, N0):
    """Modelo de crecimiento sigmoideo (Logístico)."""
    return K / (1 + ((K - N0) / N0) * np.exp(-mu * t))

def ajustar_cinetica(df):
    """Ajusta los datos experimentales al modelo logístico y retorna los parámetros."""
    # Normalizar nombres de columnas por seguridad
    df_clean = df.copy()
    df_clean.columns = [str(c).strip().lower() for c in df_clean.columns]
    
    col_t = next((c for c in df_clean.columns if 'tiem' in c or 'time' in c or c == 't'), None)
    col_b = next((c for c in df_clean.columns if 'bio' in c or 'mass' in c or 'x' in c), None)
    
    if not col_t or not col_b:
        return None

    t_vals = df_clean[col_t].values
    b_vals = df_clean[col_b].values
    
    k_init = max(b_vals)
    n0_init = min(b_vals)
    
    try:
        popt, _ = curve_fit(
            modelo_logistico, 
            t_vals, 
            b_vals, 
            p0=[k_init, 0.1, n0_init],
            bounds=(0, [np.inf, 1.0, np.inf])
        )
        K, mu, N0 = popt
        predicciones = modelo_logistico(t_vals, *popt)
        r2 = r2_score(b_vals, predicciones)
        rmse = np.sqrt(np.mean((b_vals - predicciones)**2))
        
        return {
            'mu': round(mu, 4),
            'K': round(K, 4),
            'N0': round(N0, 4),
            'R2': round(r2, 4),
            'RMSE': round(rmse, 4)
        }
    except Exception:
        return None