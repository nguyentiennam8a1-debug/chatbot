import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Cấu hình giao diện trang web
st.set_page_config(page_title="QUẢN LÝ ĐIỂM SINH VIÊN", layout="wide")

# Tiêu đề ứng dụng
st.markdown(
    "<h1 style='text-align: center; color: #1f77b4;'>QUẢN LÝ ĐIỂM SINH VIÊN</h1>",
    unsafe_allow_html=True,
)
st.write("---")

# Dữ liệu mẫu chuẩn theo tài liệu của bạn
data = {
    "Họ và tên": [
        "An",
        "Bình",
        "Chi",
        "Dũng",
        "Hà",
        "Lan",
        "Minh",
        "Nam",
        "Phúc",
        "Trang",
    ],
    "Điểm chuyên cần": [8.5, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.5, 9.0, 8.0],
    "Điểm giữa kỳ": [7.0, 8.0, 6.5, 8.5, 7.0, 7.5, 8.0, 6.5, 9.0, 8.5],
    "Điểm cuối kỳ": [8.0, 8.5, 7.0, 9.0, 7.5, 8.0, 8.5, 7.0, 8.5, 9.0],
}

df = pd.DataFrame(data)

# Yêu cầu 2: Tính điểm tổng kết
df["Tong_ket"] = (
    0.2 * df["Điểm chuyên cần"]
    + 0.3 * df["Điểm giữa kỳ"]
    + 0.5 * df["Điểm cuối kỳ"]
).round(2)


# Yêu cầu 3: Xếp loại sinh viên
def xep_loai(diem):
  if diem >= 8.5:
    return "Giỏi"
  elif diem >= 7.0:
    return "Khá"
  elif diem >= 5.0:
    return "Trung bình"
  else:
    return "Yếu"


df["Xêp_loai"] = df["Tong_ket"].apply(xep_loai)

# 1. Hiển thị bảng điểm chi tiết
st.subheader("📋 Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df, use_container_width=True)

# Yêu cầu 4: Thống kê cơ bản
st.subheader("📊 Thống kê chung của lớp")
col1, col2, col3, col4 = st.columns(4)

diem_tb_lop = df["Tong_ket"].mean()
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = (df["Tong_ket"] >= 5.0).sum()

with col1:
  st.metric(label="Điểm TB của lớp", value=f"{diem_tb_lop:.2f}")
with col2:
  st.metric(
      label="Điểm cao nhất",
      value=f"{sv_max['Tong_ket']}",
      delta=sv_max["Họ và tên"],
  )
with col3:
  st.metric(
      label="Điểm thấp nhất",
      value=f"{sv_min['Tong_ket']}",
      delta=sv_min["Họ và tên"],
      delta_color="inverse",
  )
with col4:
  st.metric(label="Số sinh viên đạt (>=5.0)", value=f"{so_sv_dat}/10")

st.write("---")

# Tra cứu thông tin từng sinh viên bằng Selectbox
st.subheader("🔍 Tra cứu thông tin sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên cần xem:", df["Họ và tên"])

student_info = df[df["Họ và tên"] == selected_student].iloc[0]
    0
]  # Lọc đúng sinh viên

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Chuyên cần", student_info["Điểm chuyên cần"])
c2.metric("Giữa kỳ", student_info["Điểm giữa kỳ"])
c3.metric("Cuối kỳ", student_info["Điểm cuối kỳ"])
c4.metric("Tổng kết", student_info["Tong_ket"])
c5.metric("Xếp loại", student_info["Xêp_loai"])

st.write("---")
# Yêu cầu 5: Biểu đồ cột ngang (plt.barh) y hệt tài liệu
st.subheader("📈 Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(df["Họ và tên"], df["Tong_ket"], color="#4A90E2")

ax.set_title(
    "Biểu đồ điểm tổng kết của 10 sinh viên", fontsize=14, fontweight="bold"
)
ax.set_xlabel("Điểm tổng kết", fontsize=12)
ax.set_ylabel("Tên sinh viên", fontsize=12)
ax.set_xlim(0, 10)

for i, v in enumerate(df["Tong_ket"]):
  ax.text(v + 0.1, i, f"{v:.2f}", va="center", fontsize=10, fontweight="bold")

plt.tight_layout()
st.pyplot(fig)

# Thông tin người tạo (MSSV)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: small;'>Người"
    " tạo:Nguyễn Tiến Nam - MSSV: 068208010484</p>",
    unsafe_allow_html=True,
)

# Yêu cầu 5: Biểu đồ cột ngang (plt.barh) y hệt tài liệu
