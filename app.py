import streamlit as st

st.set_page_config(page_title="حاسبة المهندس", page_icon="🏗️")
st.title("🏗️ حاسبة المهندس")
st.write("احسب كميات الحديد والخرسانة والطوب")

col1, col2 = st.columns(2)
with col1:
    length = st.number_input("الطول (م)", value=10.0)
with col2:
    width = st.number_input("العرض (م)", value=10.0)

thickness = st.selectbox("سمك السقف (سم)", [12, 15, 20, 25], index=1)
area = length * width
concrete = area * (thickness/100)
steel = concrete * 90
blocks = int(area * 8)

if st.button("احسب", type="primary"):
    st.success(f"المساحة: {area:.1f} م²")
    st.info(f"الخرسانة: {concrete:.2f} م³")
    st.info(f"الحديد: {steel:.0f} كجم")
    st.info(f"الطوب تقريبا: {blocks} طوبة")
