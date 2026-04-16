import streamlit as st
import pandas as pd
from datetime import datetime

# ตั้งค่าหน้าจอ
st.set_page_config(page_title="GLO Negative News Monitor", layout="wide")

st.title("ระบบเฝ้าระวังข่าวสารเชิงลบ: สำนักงานสลากกินแบ่งรัฐบาล")
st.markdown("---")

# แถบด้านข้าง
st.sidebar.header("🔍 การตั้งค่า")
keywords = st.sidebar.text_input("Keywords เชิงลบ", "หวยแพง, ทุจริต, ร้องเรียน")
if st.sidebar.button("เริ่มการ Scan ข่าว"):
    st.sidebar.success("กำลังตรวจสอบข้อมูลล่าสุด...")

# ส่วน Dashboard
col1, col2, col3 = st.columns(3)
col1.metric("ข่าวเชิงลบวันนี้", "12", "3")
col2.metric("ระดับความเสี่ยง", "High")
col3.metric("แหล่งข่าวหลัก", "Social Media")

# ตารางข้อมูลจำลอง
data = {
    "วันที่": [datetime.now().strftime("%d/%m/%Y")] * 3,
    "หัวข้อข่าว": ["พบสลากเกินราคาในหลายพื้นที่", "ร้องเรียนระบบจองสลากล่ม", "ข่าวปลอมเรื่องเลขล็อก"],
    "ระดับความเสี่ยง": ["🔴 สูง", "🟡 กลาง", "🔴 สูง"]
}
st.table(pd.DataFrame(data))

st.info("💡 นี่คือหน้าตาจำลอง (Mock-up) ของระบบตรวจสอบข่าวสาร")
