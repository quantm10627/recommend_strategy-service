import openpyxl
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import google.generativeai as genai 

# 1. Hàm nhận dữ liệu file excel từ streamlit
def load_excel (upload_file):
    # Nhận file excel và trả về dataframe kèm xử lý lỗi vặt.\
    try :
        df = pd.read_excel (upload_file) #Sử dụng thư viện openpyxl để truy xuất file excel
        df.columns = df.columns.str.strip()
        return df
    except:
        st.error("Đã xảy ra lỗi, vui lòng nhập lại")
        return None

# 2. Hàm sắp xếp trả về df chứa top loại sản phẩm bán chạy nhất
def df_sorted_product (df):
    if df is None:
        return None
    product_by_sold = df.groupby("Category").agg({
        'Units Sold': 'sum',
        'Retail Price': 'mean',
        'Opening Stock': 'sum'
    })
    # .reset_index() phải đặt ở đây để chuyển 'Category' từ Index thành Cột của DataFrame
    df_result = product_by_sold.sort_values(by='Units Sold', ascending = False).reset_index()
    return df_result

# 3. Hàm vẽ biểu đồ trực quan hóa số lượng sản phẩm bán được của top 10 sản phẩm bán chạy nhất.
# Gom nhóm các sản phẩm -> vẽ biểu đồ
def bieudo_cot (df_sorted):
    if df_sorted is None:
        return None
    # Nếu Category đang là Index thì tự động reset_index thành cột để tránh lỗi KeyError
    if "Category" not in df_sorted.columns:
        df_sorted = df_sorted.reset_index()
        
    fig, ax = plt.subplots(figsize = (20,10))
    ax.bar(df_sorted["Category"], df_sorted["Units Sold"], color ="blue")
    ax.set_title("Biểu đồ top các loại sản phẩm bán chạy nhất")
    ax.set_xlabel("Loại sản phẩm")
    ax.set_ylabel("Số lượng sản phẩm đã bán")
    ax.tick_params(axis='x', rotation=30)
    plt.tight_layout()
    return fig

# 4. Chatbot
genai.configure (api_key = st.secrets["API_key"])
model = genai.GenerativeModel('gemini-3.8-flash')
def chatbot_recomment (df_topproduct):
    data_chatbot = df_topproduct.to_markdown(index = False)

    prompt = f"""
    Bạn là chuyên gia phân tích dữ liệu bán lẻ.

    Hãy phân tích dữ liệu 10 sản phẩm sau:

    {data_chatbot}

    Yêu cầu:
    1. Nhận xét về giá bán sản phẩm.
    2. Xác định sản phẩm có giá cao và thấp.
    3. Đưa ra 3 đề xuất cải thiện kinh doanh.
    4. Trình bày bằng tiếng Việt.
    5. Trả lời ngắn gọn, dễ hiểu.
    """

    response = model.generate_content(prompt)
    return response.text
