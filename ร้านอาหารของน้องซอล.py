import streamlit as st
from datetime import date

st.set_page_config(
    page_title="ร้านอาหารตามสั่งของน้องชอล",
    page_icon="🍳",
    layout="centered"
)

# ข้อมูลเมนู

MENU = {
    "กะเพราหมูสับ": 40,
    "กะเพราหมูกรอบ": 50,
    "หมูปิ้งโบราณ": 5,
    "ซาลาเปาไส้หมู": 25,
    "ข้าวหมูหวาน": 40,
    "ข้าวหมูกระเทียม": 40,
    "ข้าวขาหมู": 45,
    "ข้าวหมูแดง": 40,
}

st.title("🍳 ร้านอาหารตามสั่งของน้องชอล")
st.caption("เลือกเมนู ระบุจำนวน แล้วระบบคำนวณส่วนลดและราคาสุทธิให้อัตโนมัติ")

st.divider()

# เลือกวันที่

selected_date = st.date_input(
    "วันที่สั่งอาหาร",
    value=date.today(),
    format="DD/MM/YYYY"
)


# เลือกเมนูและจำนวน

st.subheader("🛒 รายการอาหาร")

quantities = {}

for item, price in MENU.items():
    col1, col2, col3 = st.columns([4, 2, 2])

    with col1:
        st.write(f"**{item}**")
        st.caption(f"{price} บาท")

    with col2:
        quantities[item] = st.number_input(
            "จำนวน",
            min_value=0,
            max_value=99,
            value=0,
            step=1,
            key=f"qty_{item}"
        )

    with col3:
        subtotal = price * quantities[item]
        st.write(f"**{subtotal:,} บาท**")

st.divider()


# คำนวณราคา

total = sum(MENU[item] * quantities[item] for item in MENU)

# ส่วนลด
discount = 0
discount_text = "ไม่มีส่วนลด"

# วันอังคาร ลด 20% (ใช้สิทธิ์นี้ก่อน)
if selected_date.weekday() == 1 and total > 0:
    discount = total * 0.20
    discount_text = "ส่วนลดวันอังคาร 20%"
# ซื้อครบ 200 ลด 10%
elif total >= 200:
    discount = total * 0.10
    discount_text = "ซื้อครบ 200 บาท ลด 10%"

net_total = total - discount

st.subheader("💰 สรุปยอด")

col1, col2 = st.columns(2)

with col1:
    st.metric("รวมราคา", f"{total:,.2f} บาท")

with col2:
    st.metric("ส่วนลด", f"{discount:,.2f} บาท")

st.info(discount_text)

st.success(f"### ราคาสุทธิ {net_total:,.2f} บาท")


# แสดงรายการที่เลือก

selected_items = [
    (item, quantities[item], MENU[item] * quantities[item])
    for item in MENU
    if quantities[item] > 0
]

if selected_items:
    st.subheader("📋 รายการที่สั่ง")

    for item, qty, subtotal in selected_items:
        st.write(f"- {item} × {qty} = **{subtotal:,} บาท**")
else:
    st.warning("ยังไม่ได้เลือกเมนู")


# ปุ่มยืนยัน

if st.button("✅ ยืนยันการสั่งซื้อ", use_container_width=True):
    if total == 0:
        st.error("กรุณาเลือกอาหารอย่างน้อย 1 รายการ")
    else:
        st.balloons()
        st.success(f"สั่งซื้อสำเร็จ! ยอดชำระ {net_total:,.2f} บาท")
