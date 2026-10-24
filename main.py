
import pandas as pd
# pyrefly: ignore[missing-import]
import streamlit as st
# pyrefly: ignore[missing-import]
import google.generativeai as genai
from function import *

st.title("HELLO POTENTAL DIRECTORS")
st.header("Hệ thống phân tích dữ liệu bán hàng và đề xuất giải pháp tối ưu")

upload_file = st.file_uploader (
    label = "Chọn file dữ liệu cần phân tích [xlsx]",
    type = ["xlsx"],
    help = "Xin vui lòng nhập đúng định dạng file"
)
if upload_file is not None:
    st.success("Tải dữ liệu thành công !")

    df = load_excel(upload_file)
    if df is not None:
        df_sorted = df_sorted_product(df)
        fig = bieudo_cot(df_sorted)
        st.pyplot(fig)

        st.subheader("🤖 AI Phân Tích & Gợi Ý Nhập Hàng")
        # Tạo nút bấm để tránh việc API bị gọi liên tục mỗi khi giao diện reload
        if st.button("Phân tích dữ liệu ngay", type="primary"):
            with st.spinner("AI đang phân tích luồng dữ liệu, xin chờ trong vài phút..."):
                ai_insight = chatbot_recomment(df_sorted.head(10))
                
                # Hiển thị kết quả trong một khung thông báo nổi bật
                st.info(ai_insight)
    else:
        st.error("Quá trình tải lên bị lỗi")
else:
    st.error("Vui lòng tải lên file excel để phân tích")