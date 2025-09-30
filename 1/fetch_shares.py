"""
fetch_shares.py

สคริปต์นี้ช่วยดึงข้อมูลจำนวนหุ้นจดทะเบียน (shares_outstanding)
จาก Market Cap และราคาหุ้น (last) ถ้ามีคอลัมน์ market_cap อยู่แล้ว
ก็จะสร้างคอลัมน์ shares_outstanding ให้อัตโนมัติ
"""

import pandas as pd
import numpy as np
import os

# -----------------------------
# 1) โหลดไฟล์ CSV
# -----------------------------
def load_csv(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"ไม่พบไฟล์: {path}")
    df = pd.read_csv(path)
    return df

# -----------------------------
# 2) คำนวณ shares_outstanding
# -----------------------------
def add_shares_outstanding(df: pd.DataFrame,
                           market_cap_col: str = "market_cap",
                           price_col: str = "last") -> pd.DataFrame:
    df = df.copy()

    if market_cap_col in df.columns and price_col in df.columns:
        # คำนวณ shares_outstanding = market_cap / last
        df["shares_outstanding"] = np.where(
            (df[price_col] > 0) & (~df[market_cap_col].isna()),
            df[market_cap_col] / df[price_col],
            np.nan
        )
    else:
        print("⚠️ ไม่มี market_cap หรือ last ใน DataFrame จึงไม่สามารถคำนวณ shares_outstanding ได้")

    return df

# -----------------------------
# 3) main function
# -----------------------------
def main():
    input_csv = "stock_financials.csv"   # ไฟล์ต้นฉบับ
    output_csv = "stock_financials_with_shares.csv"  # ไฟล์ใหม่

    df = load_csv(input_csv)
    df_new = add_shares_outstanding(df)

    df_new.to_csv(output_csv, index=False)
    print(f"✅ บันทึกไฟล์ใหม่เรียบร้อย: {output_csv}")

if __name__ == "__main__":
    main()
แสห
