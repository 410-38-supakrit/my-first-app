import streamlit as st
st.markdown("# : red[🏋️  คำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็คสุขภาพเบื้องต้น")
w = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
h_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):", min_value=1.0, value=1.0)
if st.button("คำนวณค่า BMI 🎯 "):
  h_m = h_cm/100
  bmi = w / (h_m ** 2)
  st.write("---")
  st.header(f"ค่า BMI ของคุณคือ : **{bmi:.2f}**")
if bmi < 18.5:
  st.warning("⚠️ คุณมีน้ำหนักน้อยกว่าเกนฑ์ (ผอม)")
elif 18.5 <= bmi < 23.0:
  st.success("🎉 คุณมีน้ำหนักอยู่ในเกนฑ์ปกติ (สุขภาพดี)")
elif 23.0 <= bmi < 25.0:
  st.info("💡 คุณเริ่มมีน้ำหนักเกินเกนฑ์ (ท้วม)")
else:
  st.error("🚨 คุณอยู่ในเกนฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย")
st.dvider()
st.write("นายศุภกฤต บุญแก่น เลขที่ 38 ม.4/10")
