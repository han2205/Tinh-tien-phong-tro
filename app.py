import streamlit as st

st.set_page_config(page_title="Tính tiền phòng trọ", page_icon="🏠")

st.title("🏠 Ứng dụng tính tiền phòng trọ - Nhóm 2")

# Nhập tiền phòng
tien_phong = st.number_input("Nhập số tiền phòng (đồng)", min_value=0.0, value=2000000.0)

st.subheader("⚡ Tiền điện")
dien_dau = st.number_input("Số điện đầu tháng", min_value=0.0, value=1500.0)
dien_cuoi = st.number_input("Số điện cuối tháng", min_value=0.0, value=1600.0)
gia_dien = st.number_input("Đơn giá 1 số điện (đồng)", min_value=0.0, value=3400.0)

st.subheader("💧 Tiền nước")
nuoc_dau = st.number_input("Số nước đầu tháng", min_value=0.0, value=200.0)
nuoc_cuoi = st.number_input("Số nước cuối tháng", min_value=0.0, value=250.0)
gia_nuoc = st.number_input("Đơn giá 1 số nước (đồng)", min_value=0.0, value=12000.0)

st.subheader("📶 Chi phí khác")
wifi = st.number_input("Tiền WiFi (đồng)", min_value=0.0, value=100000.0)

# Nút tính toán
if st.button("💰 Tính tiền phòng"):
    tien_dien = (dien_cuoi - dien_dau) * gia_dien
    tien_nuoc = (nuoc_cuoi - nuoc_dau) * gia_nuoc
    tong_tien = tien_phong + tien_dien + tien_nuoc + wifi

    st.success("### Kết quả tính toán")

    st.write(f"**Tiền phòng:** {tien_phong:,.0f} đồng")
    st.write(f"**Tiền điện:** {tien_dien:,.0f} đồng")
    st.write(f"**Tiền nước:** {tien_nuoc:,.0f} đồng")
    st.write(f"**Tiền WiFi:** {wifi:,.0f} đồng")

    st.markdown("---")
    st.metric("💵 Tổng tiền phải thanh toán", f"{tong_tien:,.0f} đồng")
