"""
SET Stock Classification Pipeline (ปรับปรุง)

ในเวอร์ชันนี้ เปลี่ยนจากการใช้ **FFMC (Free-Float Market Cap)** เป็นการใช้ **EPS × Market Cap** แทน สำหรับการจัดกลุ่มขนาด (FTSE GEIS Size)

สูตร:
    EPS × Market Cap = EPS ล่าสุด × (ราคาหุ้นล่าสุด × จำนวนหุ้นจดทะเบียน)

โดย:
- ถ้ามีคอลัมน์ `market_cap` อยู่แล้ว → ใช้ `eps × market_cap`
- ถ้าไม่มี → ใช้ `eps × last × shares_outstanding`

ผลลัพธ์นี้จะถูกนำไปจัดอันดับเพื่อแบ่งเป็น 4 กลุ่ม: Large / Mid / Small / Micro
"""

from typing import Optional, Tuple
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os

# -----------------------------
# 1) Business understanding & data collection
# -----------------------------

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv("D:\Document\DSA\DSA 3\DSA3_1-2568\Data Mining\stock_financials.csv")
    return df

# -----------------------------
# 2) Data preparation & feature engineering
# -----------------------------

def compute_eps_x_mcap(df: pd.DataFrame, price_col: str = 'last') -> pd.Series:
    """คำนวณ EPS × Market Cap.
    - ถ้ามีคอลัมน์ `market_cap` ใช้: eps × market_cap
    - ถ้าไม่มี ใช้: eps × last × shares_outstanding
    """
    eps = pd.to_numeric(df.get('eps', pd.Series(np.nan, index=df.index)), errors='coerce')

    if 'market_cap' in df.columns:
        return eps * df['market_cap']

    if 'shares_outstanding' in df.columns:
        return eps * df[price_col] * df['shares_outstanding']

    raise ValueError('ต้องมี market_cap หรือ shares_outstanding สำหรับคำนวณ EPS × Market Cap')


def prepare_features(df: pd.DataFrame, eps_year_cols: list, years: int = 3) -> pd.DataFrame:
    df = df.copy()
    df['eps_x_mcap'] = compute_eps_x_mcap(df)
    df['pe'] = pd.to_numeric(df.get('pe', pd.Series(np.nan, index=df.index)), errors='coerce')
    df['pbv'] = pd.to_numeric(df.get('pbv', pd.Series(np.nan, index=df.index)), errors='coerce')
    df['percent_yield'] = pd.to_numeric(df.get('percent_yield', pd.Series(np.nan, index=df.index)), errors='coerce')
    return df

# -----------------------------
# 3) Unit test helpers + EDA
# -----------------------------

def run_unit_tests():
    data = {
        'symbol': ['T1'],
        'eps': [2.0],
        'last': [10.0],
        'shares_outstanding': [1e6],
        'market_cap': [1e7],
    }
    df_test = pd.DataFrame(data)
    df_test['eps_x_mcap'] = compute_eps_x_mcap(df_test)

    # eps_x_mcap = 2 × 1e7 = 2e7
    assert np.isclose(df_test.loc[0, 'eps_x_mcap'], 2e7), f"คำนวณผิด {df_test.loc[0,'eps_x_mcap']}"
    print('Unit tests passed')


def eda_summary(df: pd.DataFrame) -> pd.DataFrame:
    num = df.select_dtypes(include=[np.number])
    summary = num.describe().T
    return summary

# -----------------------------
# 4) Classification: FTSE (size) + Peter Lynch style
# -----------------------------

def classify_ftse_size(df: pd.DataFrame, col: str = 'eps_x_mcap') -> pd.Series:
    sizes = pd.qcut(df[col].rank(method='first', na_option='bottom'), q=4, labels=['Large', 'Mid', 'Small', 'Micro'])
    return sizes

# (Peter Lynch classification คงเดิม)

def classify_peter_lynch(df: pd.DataFrame) -> pd.Series:
    labels = []
    for _, r in df.iterrows():
        eps_cagr = r.get('eps_cagr', np.nan)
        pe = r.get('pe', np.nan)
        pbv = r.get('pbv', np.nan)
        yld = r.get('percent_yield', np.nan)
        label = 'Cyclicals'
        try:
            if not np.isnan(eps_cagr) and eps_cagr > 0.20 and not np.isnan(pe) and pe > 20:
                label = 'Fast Growers'
            elif not np.isnan(eps_cagr) and 0.08 <= eps_cagr <= 0.20 and (not np.isnan(pbv) and pbv > 1.0):
                label = 'Stalwarts'
            elif (not np.isnan(eps_cagr) and eps_cagr < 0.08) and (not np.isnan(yld) and yld >= 0.03):
                label = 'Slow Growers'
            elif (not np.isnan(pbv) and pbv < 0.8) and (np.isnan(pe) or pe < 10):
                label = 'Asset Plays'
            elif (not np.isnan(eps_cagr) and eps_cagr < 0) and (not np.isnan(pe) and pe > 0):
                label = 'Turnarounds'
            else:
                label = 'Cyclicals'
        except Exception:
            label = 'Cyclicals'
        labels.append(label)
    return pd.Series(labels, index=df.index)

# -----------------------------
# 5) Deployment: Heatmap 4x6 Dashboard
# -----------------------------

def build_heatmap(df: pd.DataFrame, size_col: str = 'ftse_size', style_col: str = 'lynch_style',
                  value_col: str = 'last', out_html: str = 'heatmap_4x6.html') -> str:
    size_order = ['Large', 'Mid', 'Small', 'Micro']
    style_order = ['Slow Growers', 'Stalwarts', 'Fast Growers', 'Cyclicals', 'Turnarounds', 'Asset Plays']
    pivot_table = pd.pivot_table(df, values=value_col, index=size_col, columns=style_col, aggfunc='mean')
    pivot_table = pivot_table.reindex(index=size_order, columns=style_order)
    z = pivot_table.values
    fig = go.Figure(data=go.Heatmap(
        z=z,
        x=style_order,
        y=size_order,
        hoverongaps=False,
        colorbar=dict(title=value_col)
    ))
    annotations = []
    for i, row in enumerate(size_order):
        for j, col in enumerate(style_order):
            val = pivot_table.loc[row, col]
            txt = f"{val:,.2f}" if not pd.isna(val) else "-"
            annotations.append(dict(x=col, y=row, text=txt, showarrow=False, font=dict(color='black')))
    fig.update_layout(
        title=f"Heatmap: {value_col} by FTSE Size x Peter Lynch Style",
        xaxis_title="Peter Lynch Style",
        yaxis_title="FTSE GEIS Size",
        annotations=annotations
    )
    fig.write_html(out_html, include_plotlyjs='cdn')
    return os.path.abspath(out_html)

# -----------------------------
# Example main flow
# -----------------------------

def main(csv_path: str):
    df = load_data(csv_path)
    eps_cols = sorted([c for c in df.columns if c.startswith('eps_')])
    df_feat = prepare_features(df, eps_cols, years=3)
    df_feat['ftse_size'] = classify_ftse_size(df_feat, col='eps_x_mcap')
    df_feat['lynch_style'] = classify_peter_lynch(df_feat)
    out_csv = 'classified_stocks.csv'
    df_feat.to_csv(out_csv, index=False)
    summary = eda_summary(df_feat)
    summary.to_csv('eda_summary.csv')
    heatmap_path = build_heatmap(df_feat, value_col='last')
    print('Saved classified stocks to', out_csv)
    print('Saved EDA summary to eda_summary.csv')
    print('Saved heatmap to', heatmap_path)

if __name__ == '__main__':
    default_csv = 'stock_financials.csv'
    if os.path.exists(default_csv):
        try:
            run_unit_tests()
        except AssertionError as e:
            print('Unit tests failed:', e)
        main(default_csv)
    else:
        print(f'กรุณาวางไฟล์ CSV ชื่อ {default_csv} ในโฟลเดอร์ทำงาน หรือเรียก main(csv_path) เอง')
