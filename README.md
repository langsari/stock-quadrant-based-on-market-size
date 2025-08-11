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


3. เกณฑ์ (Criteria)
 -Market Size (Y-axis)
    1.Large Cap: Market Cap > 100,000 ล้านบาท
    2.Mid Cap: 30,000–100,000 ล้านบาท
    3.Small Cap: < 30,000 ล้านบาท (สามารถปรับเกณฑ์ตามตลาดไทยได้)
 -Investment Style (X-axis)
    1.Growth Stock: EPS Growth > 15% (หรือใช้ Revenue Growth, ROE สูง)
    2.Value Stock: P/E ต่ำกว่าเฉลี่ยกลุ่ม และ Dividend Yield สูง (อาจใช้การจัดอันดับ percentile แทนค่า fixed number)


4. ข้อมูลและตัวแปรที่ใช้
 -ตัวแปรดิบ (Raw variables)
    1.Market Cap
    2.P/E Ratio
    3.P/BV Ratio
    4.Dividend Yield (%)
    5.EPS Growth (%)
    6.Sector / Industry
    7.Volume, Turnover
 -ตัวแปรอนุพันธ์ (Derived variables)
    1.Market Size Category
    2.Style Category (Value / Growth)
    3.Quadrant (1–4)


5. Output / Deployment
 -Heatmap Quadrant
    1.X-axis = Investment Style (Value → Growth)
    2.Y-axis = Market Size (Small → Large)
    3.จุด (dot) = หุ้นแต่ละตัว
    4.สี = Sector
    5.ขนาดจุด = Market Cap
 -Descriptive Table
    1.ตารางสรุปว่ามีหุ้นกี่บริษัทในแต่ละ Quadrant
    2.แยกเป็นหมวดอุตสาหกรรม (Industry) และสรุปค่าเฉลี่ยตัวชี้วัด
 -หมวดหมู่ใน SET
    1.ดูจำนวนหุ้นในแต่ละ Sector (เช่น AGRI, FOOD, FIN, PROP, etc.)
    2.แสดงผ่าน Horizontal Bar Chart


6. การแบ่ง “ฝั่ง” ใน Heatmap
 -Quadrant 1: Large-Cap Growth
 -Quadrant 2: Large-Cap Value
 -Quadrant 3: Small-Cap Growth
 -Quadrant 4: Small-Cap Value


7. การประยุกต์ใช้
 -ช่วยนักลงทุนเลือกหุ้นให้หลากหลาย
 -วิเคราะห์การกระจายความเสี่ยงของพอร์ต
 -ดูเทรนด์ตลาดว่ากระจุกตัวในฝั่งใด
   
