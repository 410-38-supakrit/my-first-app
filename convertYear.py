import streamlit as st
st.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็ร ค.ศ.")

a=st.number_input("กรอกปี พ.ศ. ที่ต้องการแปลง",value=2569)
b=a-543
st.header(f"ปี ค.ศ. คือ : {b}")
