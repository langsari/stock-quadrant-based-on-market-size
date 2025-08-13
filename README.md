# 📊 Stock Quadrant Based on Market Size

A stock quadrant model for classifying equities by **market capitalization** and **investment style**, helping to build and analyze diversified portfolios.

---

## 1. แนวคิดโครงการ
สร้างโมเดล/แดชบอร์ด **"Stock Quadrant"** สำหรับจัดกลุ่มหุ้นในตลาด SET ตาม  
- **Market Capitalization** (ขนาดบริษัท)  
- **Investment Style** (เช่น Growth, Value)  

เพื่อช่วยให้นักลงทุนมองเห็นภาพรวมและสร้างพอร์ตการลงทุนที่หลากหลาย (**Diversified Portfolio**)

---

## 2. Data Science Life Cycle
| ขั้นตอน | รายละเอียด |
|---------|-------------|
| **1. Business Understanding** | กำหนดเป้าหมาย: ต้องการแบ่งหุ้นในตลาด SET ออกเป็น 4 Quadrant ตาม Market Size และ Investment Style |
| **2. Data Collection** | ดึงข้อมูลจาก **SETTRADE API / เว็บไซต์ SETTRADE** เช่น Market Cap, P/E, P/BV, Dividend Yield, EPS Growth |
| **3. Data Preparation** | ทำความสะอาดข้อมูล (missing value, type casting) และสร้างตัวแปรใหม่ เช่น Market Size Category |
| **4. Data Analysis / Descriptive Analytics** | วิเคราะห์จำนวนหุ้นในแต่ละหมวดหมู่, ค่าเฉลี่ย Market Cap, ค่าเฉลี่ย P/E |
| **5. Modeling / Classification** | จัดกลุ่มเป็น Quadrant:<br>• แกน X = Investment Style (Value vs Growth)<br>• แกน Y = Market Cap (Small vs Large) |
| **6. Deployment** | แสดงผลผ่าน Heatmap / Dashboard (Power BI, Tableau, Plotly) |

---

## 3. เกณฑ์การจัดกลุ่ม (Criteria)

### **Market Size (Y-axis)**
1. **Large Cap**: Market Cap > 100,000 ล้านบาท  
2. **Mid Cap**: 30,000 – 100,000 ล้านบาท  
3. **Small Cap**: < 30,000 ล้านบาท  
*(สามารถปรับเกณฑ์ตามตลาดไทยได้)*

### **Investment Style (X-axis)**
1. **Growth Stock**: EPS Growth > 15% (หรือใช้ Revenue Growth, ROE สูง)  
2. **Value Stock**: P/E ต่ำกว่าเฉลี่ยกลุ่ม และ Dividend Yield สูง  
*(อาจใช้การจัดอันดับ percentile แทนค่า fixed number)*

---

## 4. ข้อมูลและตัวแปรที่ใช้

### **ตัวแปรดิบ (Raw Variables)**
- Market Cap
- P/E Ratio
- P/BV Ratio
- Dividend Yield (%)
- EPS Growth (%)
- Sector / Industry
- Volume, Turnover

### **ตัวแปรอนุพันธ์ (Derived Variables)**
- Market Size Category
- Style Category (Value / Growth)
- Quadrant (1–4)

---

## 5. Output / Deployment

### **Heatmap Quadrant**
- X-axis = Investment Style (Value → Growth)  
- Y-axis = Market Size (Small → Large)  
- จุด (dot) = หุ้นแต่ละตัว  
- สี = Sector  
- ขนาดจุด = Market Cap  

### **Descriptive Table**
- จำนวนหุ้นในแต่ละ Quadrant  
- แยกตามหมวดอุตสาหกรรม (Industry) พร้อมสรุปค่าเฉลี่ยตัวชี้วัด  

### **หมวดหมู่ใน SET**
- จำนวนหุ้นในแต่ละ Sector (เช่น AGRI, FOOD, FIN, PROP)  
- แสดงผ่าน **Horizontal Bar Chart**

---

## 6. การแบ่ง “ฝั่ง” ใน Heatmap
- **Quadrant 1**: Large-Cap Growth  
- **Quadrant 2**: Large-Cap Value  
- **Quadrant 3**: Small-Cap Growth  
- **Quadrant 4**: Small-Cap Value  

---

## 7. การประยุกต์ใช้
- ช่วยนักลงทุนเลือกหุ้นให้หลากหลาย  
- วิเคราะห์การกระจายความเสี่ยงของพอร์ต  
- ดูเทรนด์ตลาดว่ากระจุกตัวในฝั่งใด  

---

## 🚀 Tools & Libraries (Suggested)
- **Data Collection**: Python (Requests, BeautifulSoup, yfinance, API)
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly, Power BI, Tableau
- **Deployment**: Streamlit, Dash, Power BI Service

---

## 📌 Author
Project by: *[Your Name]*  
Data Science Student | Financial Data Enthusiast  

