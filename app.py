ax.set_title('Biểu đồ điểm tổng kết 10 sinh viên', fontsize=14, fontweight='bold')
ax.set_xlabel('Họ và tên', fontsize=11)
ax.set_ylabel('Điểm tổng kết', fontsize=11)
plt.xticks(rotation=30, ha='right')
plt.ylim(0, 10)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, f'{yval}', ha='center', va='bottom', fontsize=9)

st.pyplot(fig)

# 5. Thông tin người tạo (chữ nhỏ ở cuối trang)
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: small;'>Người tạo: Nguyễn Tiến Nam - MSSV: [Điền MSSV của bạn]</p>", unsafe_allow_html=True)