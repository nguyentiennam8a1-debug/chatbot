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
