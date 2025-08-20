# 📊 Stock Quadrant Based on Market Size

A stock quadrant model for classifying equities by **market capitalization** and **investment style**, helping to build and analyze diversified portfolios.

---

* ใช้เกณฑ์ **FTSE (FTSE Russell / FTSE GEIS)** สำหรับ Market Size
* ใช้เกณฑ์ **Peter Lynch** สำหรับ Investment Style
* วางเป็น **Data Science Life Cycle** แบบมองภาพรวม ครอบทุกขั้นตอน
* ปรับ **Heatmap เป็น 5×5** (แกนละ 5 ระดับ)

---

# Stock Quadrant (FTSE Size × Peter Lynch Style) — 5×5

## 1) แนวคิด (Concept)

สร้างแดชบอร์ด/โมเดล “Stock Quadrant” ของหุ้นในตลาดไทย โดย

* **แกน Y (5 ระดับ):** Market Size ตาม **มาตรฐาน FTSE GEIS** (Large/Mid/Small/Micro) แปลงเป็นสเกล 1–5
* **แกน X (5 ระดับ):** Investment Style ตาม **Peter Lynch** (Slow Growers, Stalwarts, Fast Growers, Cyclicals, Turnarounds/Asset Plays) แปลงเป็นสเกล 1–5
  ได้ **Heatmap 5×5** เพื่อช่วยวิเคราะห์การกระจายตัวและสร้างพอร์ตแบบ Diversified

> อิงเกณฑ์ขนาดจาก FTSE GEIS ซึ่งแบ่งขนาดด้วยการ **จัดอันดับตามมาร์เก็ตแคปแบบถ่วงด้วย free float** และใช้ **เปอร์เซ็นไทล์/บัฟเฟอร์โซน** สำหรับ Large/Mid/Small/Micro (เช่น ใช้จุดแบ่งราว 70%–90% ของมูลค่ารวม และ micro นอกท็อป \~98% พร้อมเกณฑ์มูลค่าลงทุนขั้นต่ำ) ตามเอกสารกติกา FTSE GEIS ล่าสุด. ([LSEG][1], [Bursa Malaysia][2])

---

## 2) Data Science Life Cycle (ภาพรวม ครอบทุกขั้นตอน)

### A. Business Understanding

* เป้าหมาย: จัดหุ้นไทยลง **Heatmap 5×5** = **FTSE Size (Y)** × **Peter Lynch Style (X)**
* คำถามหลัก:

  1. หุ้นไทยกระจุกในช่องไหนของ 5×5 มากที่สุด?
  2. แต่ละ **Sector/Industry** กระจายยังไง?
  3. ใช้เพื่อออกแบบ **allocation** ของพอร์ตแบบกระจายความเสี่ยง

### B. Data Collection

* แหล่ง: SET/SETTRADE (ราคา, จำนวนหุ้น, Sector, ปัจจัยพื้นฐาน), งบการเงินรายปี/ไตรมาส
* ตัวแปรดิบ: Market Cap (free-float ถ้ามี), P/E, P/BV, Dividend Yield, EPS Growth, Revenue Growth, ROE, เลเวอเรจ, ความผันผวนกำไร/ยอดขาย, Sector/Industry, Volume/Turnover
* หมายเหตุ FTSE: ใช้ **full market cap เพื่อจัดอันดับ** + **investable/free-float market cap** เพื่อ inclusion/exclusion และ **บัฟเฟอร์โซน** (กติกาอยู่ใน Section 7). ([LSEG][1])

### C. Data Preparation

* ทำความสะอาด: missing/outlier, ความถี่ข้อมูล (ไตรมาส/ปี), ปรับฐานตัวเลข
* สร้างฟีเจอร์:

  * **FTSE Size Percentile**: จัดอันดับตาม **full market cap** ในจักรวาลหุ้นไทย → คำนวณเปอร์เซ็นไทล์
  * **Peter Lynch Signals**: EPS/Revenue CAGR, ความผันผวนยอดขาย/กำไร (σ), PEG, Dividend Yield, Leverage, Asset/Book Value growth, วัฏจักรอุตสาหกรรม ฯลฯ
* แม็ปเป็น **5 ระดับ** (รายละเอียดด้านล่าง)

### D. Data Analysis / Descriptive Analytics

* ตารางสรุปจำนวนบริษัทในแต่ละช่องของ 5×5
* สรุปตาม Sector/Industry, ค่าเฉลี่ยตัวชี้วัดในแต่ละช่อง
* แผนภูมิแท่งสรุป **จำนวนหุ้นต่อ Sector** และ **สัดส่วนต่อช่อง**

### E. Modeling / Classification

* **แกน Y (FTSE Size Score: 1–5)**

  * ใช้เปอร์เซ็นไทล์ขนาดตาม FTSE GEIS (ภายในประเทศ/ภูมิภาค) + แนวคิดบัฟเฟอร์โซน
  * ตัวอย่าง mapping (ปรับได้ให้สอดคล้องจักรวาลหุ้นไทย):

    * **Score 5 (Mega/Large Top)**: ≤ \~70% ของมูลค่ารวม (Large core)
    * **Score 4 (Large/Mid Edge)**: \~70–80%
    * **Score 3 (Mid)**: \~80–90%
    * **Score 2 (Small)**: \~90–98%
    * **Score 1 (Micro/Below)**: > \~98% และผ่านเกณฑ์ investable cap ของ FTSE
  * อ้างอิงกติกา FTSE GEIS สำหรับหลักการแบ่ง Large/Mid/Small/Micro และ micro-cut (เช่น นอกท็อป \~98% + min investable cap) และ **buffer** \~68/72/86/92% สำหรับความต่อเนื่องของสมาชิกภาพ. ([LSEG][1], [Bursa Malaysia][2])
* **แกน X (Peter Lynch Style Score: 1–5)**

  * อิงการจัดหมวด **6 ประเภทของ Peter Lynch** แล้วทำให้เป็นสเกล 5 ระดับที่ใช้งานได้ในข้อมูลเชิงปริมาณ: Slow Growers, Stalwarts, Fast Growers, Cyclicals, Turnarounds, Asset Plays. ([Hapi][3], [Old School Value][4], [Value Investor Academy][5])
  * เสนอการแม็ปเชิงกติกา (ปรับ threshold ตามตลาดไทย):

    * **Score 1 – Slow Growers/High Yield**: EPS/Revenue CAGR 0–5%, Dividend Yield สูง, P/E ต่ำ–ปานกลาง
    * **Score 2 – Stalwarts**: EPS CAGR \~5–12%, ROE เสถียร, เบต้าต่ำ–ปานกลาง
    * **Score 3 – Cyclicals / Asset Plays (กลาง)**: ความผันผวนกำไร/ยอดขายสูง, ขึ้นกับวัฏจักร, หรือมีส่วนต่าง “ทรัพย์สินซ่อนเร้น” (P/BV < 1–1.2 พร้อมหลักฐานสินทรัพย์)
    * **Score 4 – Turnarounds (กำลังฟื้น)**: EPS ล่าสุดกลับมาเป็นบวก, หนี้ลดลง, กระแสเงินสดดีขึ้น
    * **Score 5 – Fast Growers**: EPS/Revenue CAGR > 15–20%, PEG \~≤ 1.5, ROE สูง
  * กรณีหุ้นเข้าได้หลายประเภท ให้กติกาจัดลำดับความสำคัญ: **Fast Grower > Turnaround > Cyclical/Asset > Stalwart > Slow** (หรือใช้คะแนนถ่วงน้ำหนัก)

### F. Deployment

* แดชบอร์ด (Power BI/Plotly/Streamlit)
* **Heatmap 5×5**:

  * แกน X = **Peter Lynch Style (1–5)**
  * แกน Y = **FTSE Size (1–5)**
  * จุด = หุ้น, สี = Sector/Industry, ขนาดจุด = Market Cap
* ตารางสรุป, Bar Chart จำแนก Sector, ฟิลเตอร์ตาม **Sector/Industry, Size Band, Style Band**

---

## 3) นิยามสเกล 5×5 (พร้อมเกณฑ์ใช้งานได้จริง)

### แกน Y — FTSE Size Score (ตาม FTSE GEIS)

> ขั้นตอนจริงให้คำนวณจากจักรวาลหุ้นไทย แล้วจัดอันดับตาม **full market cap** (เปอร์เซ็นไทล์)
> ใช้ **buffer zone** ตามคู่มือ FTSE เมื่ออัปเดตเป็นรอบ (เพื่อลด turnover)

* **5 = Mega/Large Top**: ≤\~70%
* **4 = Large/Mid Edge**: \~70–80%
* **3 = Mid**: \~80–90%
* **2 = Small**: \~90–98%
* **1 = Micro**: >\~98% (และผ่าน investable cap ขั้นต่ำของ FTSE)
  อ้างอิงกติกา FTSE GEIS (Section 7) และคำอธิบายสัดส่วนโดยสรุป \~70/20/10 สำหรับ Large/Mid/(Small+Micro). ([LSEG][1], [Bursa Malaysia][2])

### แกน X — Peter Lynch Style Score (เชิงปริมาณ)

คำนวณสัญญาณต่อไปนี้ (ย้อนหลัง 3–5 ปี):

* EPS CAGR, Revenue CAGR, **σ(EPS/Revenue YoY)** (ความผันผวน), ROE, PEG = (P/E)/EPS Growth, Dividend Yield, Leverage (D/E), P/BV, กระแสเงินสด

> กติกาย่อ (ตัวอย่าง threshold ที่ปรับได้):

* **1 = Slow Growers/High Yield:** EPS CAGR 0–5%, DivYield สูง, P/E ต่ำ–กลาง
* **2 = Stalwarts:** EPS CAGR 5–12%, ROE สม่ำเสมอ, เบต้าต่ำ–กลาง
* **3 = Cyclicals/Asset Plays:** σ(EPS) สูง, หรือ P/BV ต่ำพร้อมทรัพย์สินรองรับ
* **4 = Turnarounds:** EPS พลิกบวก, หนี้/ดอกเบี้ยจ่ายลดลง, OCF ดีขึ้น
* **5 = Fast Growers:** EPS/Revenue CAGR > 15–20%, ROE สูง, PEG ≤ 1.5
  อ้างอิงกรอบหมวด 6 แบบของ Peter Lynch. ([Hapi][3], [Old School Value][4], [Value Investor Academy][5])

---

## 4) Output ที่ต้องมี

1. **Heatmap 5×5** (X: Lynch Style 1–5, Y: FTSE Size 1–5)
2. **Descriptive Table**: จำนวนบริษัทในแต่ละช่อง + ค่าเฉลี่ยตัวชี้วัดหลัก
3. **Sector View**: แถบสรุปจำนวนหุ้นต่อ Sector/Industry + สัดส่วนแต่ละช่อง
4. **Filters**: ปี, Sector, Size Band, Style Band, เกณฑ์คุณภาพ (ROE, Leverage, Liquidity)

---

## 5) เกณฑ์ข้อมูล/ตัวแปรที่ใช้ (สรุป)

* **FTSE Size:** full market cap → คำนวณ percentile ภายในจักรวาลไทย (ใช้อ้างอิง FTSE GEIS) + เงื่อนไข micro/investable cap + buffer เมื่อรีวิวรอบถัดไป. ([LSEG][1])
* **Lynch Style:** สัญญาณการเติบโต/เสถียรภาพ/วัฏจักร/การฟื้นตัว/ทรัพย์สิน (ตามด้านบน)

---

## 6) หมายเหตุด้านระเบียบวิธี (Methodology Notes)

* **ทำไมใช้ FTSE GEIS:** เป็นมาตรฐานสากลสำหรับการแบ่ง Large/Mid/Small/Micro ด้วยวิธี percentile ตาม region/country และใช้ **buffer** ลดการสลับกลุ่มเวลารีบาลานซ์. ([LSEG][1])
* **Peter Lynch กับ “สไตล์”:** Lynch เน้น “ประเภทบริษัท” มากกว่าแฟคเตอร์เชิงเดี่ยว (P/E หรือ Growth อย่างเดียว) จึงเหมาะที่จะทำเป็น **สเกลองค์รวม 1–5** ที่ดูหลายสัญญาณพร้อมกัน. ([Hapi][3], [Old School Value][4])

---

## 7) แผนการทำงานย่อ (Checklist)

* [ ] นิยามจักรวาลหุ้นไทย + ดึงข้อมูลราค/งบ/ปัจจัยพื้นฐาน
* [ ] คำนวณ **FTSE Size Percentile** + กำหนด Score 1–5
* [ ] คำนวณสัญญาณ **Lynch Style** + กำหนด Score 1–5
* [ ] เรนเดอร์ **Heatmap 5×5** + ตาราง/กราฟสรุป
* [ ] เพิ่มฟิลเตอร์/อินเตอร์แอคทีฟ + เอกสารวิธีคำนวณ

---

### แหล่งอ้างอิงหลัก

* **FTSE GEIS Ground Rules (v13.5, Jul 2025)** — วิธีแบ่งขนาด, micro cut, buffer zones. ([LSEG][1])
* **สรุปสัดส่วน size แถบ 70/20/10 (ประเทศ/ภูมิภาค)** — เอกสาร regional role/สไลด์. ([Bursa Malaysia][2])
* **Peter Lynch’s 6 Categories** — บทความ/เช็กลิสต์อธิบายหมวด Slow/Stalwart/Fast/Cyclical/Turnaround/Asset Play. ([Hapi][3], [Old School Value][4], [Value Investor Academy][5])

---


[1]: https://www.lseg.com/content/dam/ftse-russell/en_us/documents/ground-rules/ftse-global-equity-index-series-ground-rules.pdf "FTSE Global Equity Index Series Ground Rules"
[2]: https://www.bursamalaysia.com/sites/5bb54be15f36ca0af339077a/content_entry6545042539fba2073dff6c40/66b1b632e6414a5076a39de4/files/Malaysia_s_role_in_FTSE_GEIS_Jul2024.pdf?1722939579=&utm_source=chatgpt.com "Malaysia's Role in FTSE GEIS"
[3]: https://hapi.trade/en/blog/types-of-stocks-peter-lynch?utm_source=chatgpt.com "What are the types of stocks according to Peter Lynch?"
[4]: https://www.oldschoolvalue.com/investment-tools/peter-lynchs-final-investment-checklist/?utm_source=chatgpt.com "Peter Lynch's Final Investment Checklist"
[5]: https://valueinvestoracademy.com/peter-lynchs-6-types-of-companies-you-need-to-know/?utm_source=chatgpt.com "Peter Lynch's 6 Types of Companies You Need to Know"

---



