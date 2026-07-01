import streamlit as st

# Tiêu đề
st.title("🏠 Tính Tiền Phòng Trọ - Nhóm 2")

st.write("### Nhập thông tin")

# Tiền phòng
A = st.number_input("Nhập số tiền phòng (đồng)", min_value=0.0, step=1000.0)

# Điện
st.subheader("⚡ Tiền điện")
a = st.number_input("Số điện đầu tháng", min_value=0.0, step=1.0)
b = st.number_input("Số điện cuối tháng", min_value=0.0, step=1.0)
c = st.number_input("Đơn giá 1 số điện (đồng)", min_value=0.0, step=100.0)

# Nước
st.subheader("💧 Tiền nước")
x = st.number_input("Số nước đầu tháng", min_value=0.0, step=1.0)
y = st.number_input("Số nước cuối tháng", min_value=0.0, step=1.0)
z = st.number_input("Đơn giá 1 số nước (đồng)", min_value=0.0, step=100.0)

# Wifi
E = st.number_input("Tiền Wifi (đồng)", min_value=0.0, step=1000.0)

# Nút tính
if st.button("💰 Tính tiền phòng"):

    # Kiểm tra dữ liệu
    if b < a:
        st.error("❌ Số điện cuối tháng phải lớn hơn hoặc bằng số đầu tháng!")
    elif y < x:
        st.error("❌ Số nước cuối tháng phải lớn hơn hoặc bằng số đầu tháng!")
    else:
        B = (b - a) * c
        C = (y - x) * z
        D = A + B + C + E

        st.success("✅ Tính thành công!")

        st.write("### Chi tiết")
        st.write(f"🏠 Tiền phòng: **{A:,.0f} đồng**")
        st.write(f"⚡ Tiền điện: **{B:,.0f} đồng**")
        st.write(f"💧 Tiền nước: **{C:,.0f} đồng**")
        st.write(f"📶 Tiền Wifi: **{E:,.0f} đồng**")

        st.markdown("---")
        st.metric("💵 Tổng tiền phải thanh toán", f"{D:,.0f} đồng")
