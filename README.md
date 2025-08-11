# stock-quadrant-based-on-market-size
A stock quadrant model for classifying equities by market capitalization and investment style, helping to build and analyze diversified portfolios.

1. แนวคิดโครงการ
สร้างโมเดล/แดชบอร์ด “Stock Quadrant” สำหรับจัดกลุ่มหุ้นในตลาด SET ตาม Market Capitalization (ขนาดบริษัท) และ Investment Style (เช่น Growth, Value)
เพื่อช่วยนักลงทุนมองเห็นภาพรวมและสร้างพอร์ตที่หลากหลาย (Diversified Portfolio)


2. Data Science Life Cycle
เราสามารถอิงขั้นตอนหลัก 6 ขั้น ดังนี้

ขั้นตอน	รายละเอียด
1. Business Understanding	กำหนดเป้าหมาย: ต้องการแบ่งหุ้นในตลาด SET ออกเป็น 4 Quadrant ตาม Market Size และ Investment Style
2. Data Collection	ดึงข้อมูลจาก SETTRADE API / เว็บไซต์ SETTRADE เกี่ยวกับ Market Cap, P/E, P/BV, Dividend Yield, EPS Growth เป็นต้น
3. Data Preparation	ทำความสะอาดข้อมูล (จัดการ missing value, แปลงประเภทข้อมูล), สร้างตัวแปรใหม่ (เช่น แบ่ง market cap เป็น Small, Mid, Large)
4. Data Analysis / Descriptive Analytics	วิเคราะห์จำนวนหุ้นในแต่ละหมวดหมู่, ค่าเฉลี่ย Market Cap, ค่าเฉลี่ย P/E เป็นต้น
5. Modeling / Classification	จัดกลุ่มเป็น Quadrant โดยใช้เกณฑ์ที่ตั้งไว้ เช่น
• แกน X: Investment Style (Value vs Growth)
• แกน Y: Market Cap (Small vs Large)
ได้ 4 Quadrant เช่น Small-Growth, Small-Value, Large-Growth, Large-Value
6. Deployment	แสดงผลผ่าน Heatmap / Dashboard (เช่น Power BI, Tableau, Plotly) เพื่อให้ผู้ใช้ดูได้ว่า หุ้นในหมวดใดอยู่ตรงไหนของ Quadrant (ไม่จำเป็นต้องเป็น API)
