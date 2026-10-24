# 📊 RECOMMEND STRATEGY SERVICES
> **Hệ thống phân tích dữ liệu bán hàng & đề xuất chiến lược tối ưu bằng Generative AI**  
> *Final Project - Khóa học Python GD1-CS.DATA17 | Cybersoft Academy*

---

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-Generative%20AI-orange.svg?logo=google&logoColor=white)](https://ai.google.dev/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 1. Giới thiệu tổng quan

Trong kỷ nguyên bán lẻ hiện đại, việc theo dõi doanh số và đưa ra quyết định nhập hàng thủ công thường tiêu tốn nhiều thời gian và dễ bỏ sót các cơ hội kinh doanh.

**Recommend Strategy Services** là giải pháp phần mềm web tương tác được phát triển nhằm hỗ trợ các cấp quản lý, chủ doanh nghiệp và giám đốc bán lẻ (**Retail Directors / Store Managers**):
- Tự động hóa quá trình tiếp nhận và tiền xử lý báo cáo doanh thu từ file Excel thô.
- Tổng hợp và xếp hạng các danh mục sản phẩm có tốc độ tiêu thụ cao nhất.
- Trực quan hóa dữ liệu bán hàng qua biểu đồ trực quan, rõ ràng.
- Ứng dụng **Generative AI (Google Gemini)** đóng vai trò một chuyên gia phân tích bán lẻ để tự động đề xuất chiến lược tối ưu giá, kiểm soát tồn kho và gợi ý kế hoạch nhập hàng.

---

## 🚀 2. Tính năng nổi bật

- 📁 **Tải lên & Kiểm tra dữ liệu (File Ingestion & Validation):**
  - Tải lên file Excel (`.xlsx`) nhanh chóng qua giao diện kéo-thả trực quan của Streamlit.
  - Tự động chuẩn hóa tiêu đề các cột dữ liệu (loại bỏ khoảng trắng thừa), cơ chế `try-catch` bắt lỗi file hỏng/sai định dạng.

- 📈 **Tổng hợp & Phân loại thông minh (Data Aggregation & Ranking):**
  - Nhóm dữ liệu theo ngành hàng / danh mục (`Category`).
  - Thống kê tổng số lượng sản phẩm bán ra (`Units Sold`), giá bán trung bình (`Retail Price`), tồn kho đầu kỳ (`Opening Stock`).
  - Sắp xếp và trích xuất danh sách các sản phẩm bán chạy nhất (Best-selling products).

- 📊 **Trực quan hóa dữ liệu (Interactive Visualization):**
  - Tự động dựng biểu đồ cột sắc nét (Matplotlib Bar Chart) thể hiện trực tiếp thứ hạng số lượng bán của các danh mục sản phẩm.

- 🤖 **Trợ lý AI Đề xuất Chiến lược (GenAI Strategy Advisor):**
  - Sử dụng mô hình **Google Gemini (`gemini-3.8-flash`)** phân tích dữ liệu Top 10 sản phẩm bán chạy nhất.
  - Tự động đánh giá tương quan giữa giá bán và tốc độ bán hàng.
  - Nhận diện các phân khúc sản phẩm có biên độ giá cao và thấp.
  - Đưa ra **3 đề xuất chiến lược cụ thể** giúp cải thiện doanh số và tối ưu vòng quay hàng tồn kho.
  - Phản hồi bằng tiếng Việt ngắn gọn, súc tích và dễ áp dụng vào thực tế.

---

## 🔄 3. Quy trình hoạt động (Data & AI Pipeline)

```mermaid
flowchart TD
    A[Người dùng tải file Excel (.xlsx)] --> B[Hàm load_excel: Đọc & làm sạch dữ liệu]
    B --> C[Hàm df_sorted_product: GroupBy Category & Tính tổng Units Sold, Retail Price, Stock]
    C --> D[Hàm bieudo_cot: Vẽ biểu đồ cột Matplotlib hiển thị Top sản phẩm]
    D --> E[Chuyển đổi Top 10 sản phẩm sang định dạng Markdown Data]
    E --> F[Prompt Engineering gửi đến Google Gemini AI Model]
    F --> G[Gemini phân tích giá, phân khúc & đưa ra 3 đề xuất chiến lược]
    G --> H[Hiển thị kết quả & Insight lên giao diện Streamlit Dashboard]
```

---

## 🗂️ 4. Cấu trúc thư mục dự án

```text
recommend_strategy-services/
├── .streamlit/
│   ├── secrets.toml.example     # File mẫu hướng dẫn cấu hình API Key
│   └── secrets.toml             # File chứa API Key thực tế (được bảo mật trong .gitignore)
├── .gitignore                   # Cấu hình bỏ qua các file nhạy cảm, cache và môi trường ảo
├── function.py                  # Module logic: Đọc Excel, xử lý dữ liệu, vẽ chart, gọi Gemini API
├── main.py                      # Giao diện chính Streamlit Dashboard
├── plan.docx                    # Bản kế hoạch chi tiết các giai đoạn phát triển dự án
├── requirements.txt             # Danh sách các thư viện cần thiết
├── revenue_data.xlsx            # File dữ liệu mẫu phục vụ kiểm thử và demo
└── README.md                    # Tài liệu hướng dẫn sử dụng và giới thiệu dự án
```

---

## 📑 5. Cấu trúc dữ liệu mẫu (`revenue_data.xlsx`)

Hệ thống được thiết kế để xử lý dữ liệu bán hàng với các trường thông tin chuẩn:

| Cột dữ liệu | Ý nghĩa |
| :--- | :--- |
| `Product ID` | Mã định danh sản phẩm |
| `Product Name` | Tên sản phẩm |
| `Category` | Danh mục / Nhóm ngành hàng |
| `Supplier Name` | Nhà cung cấp |
| `Unit Cost` | Giá vốn sản phẩm |
| `Retail Price` | Giá bán lẻ niêm yết |
| `Opening Stock` | Số lượng tồn kho đầu kỳ |
| `Units Sold` | Số lượng sản phẩm đã bán |
| `Closing Stock` | Số lượng tồn kho cuối kỳ |
| `Reorder Point` | Điểm đặt hàng lại (ngưỡng cảnh báo tồn kho tối thiểu) |
| `Stock Status` | Trạng thái tồn kho (*In Stock*, *Low Stock*,...) |

---

## 🛠️ 6. Hướng dẫn cài đặt & Khởi chạy

### Bước 1: Clone kho lưu trữ về máy
```bash
git clone https://github.com/quantm10627/recommend_strategy-services.git
cd recommend_strategy-services
```

### Bước 2: Thiết lập môi trường ảo (Khuyến nghị)
- **Trên Windows:**
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```
- **Trên macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### Bước 3: Cài đặt các thư viện phụ thuộc
```bash
pip install -r requirements.txt
```

### Bước 4: Cấu hình Google Gemini API Key
1. Truy cập [Google AI Studio](https://aistudio.google.com/) để tạo một API Key miễn phí.
2. Sao chép file `.streamlit/secrets.toml.example` thành `.streamlit/secrets.toml`:
   - **Trên Windows (PowerShell):**
     ```powershell
     Copy-Item .streamlit/secrets.toml.example .streamlit/secrets.toml
     ```
   - **Trên Linux / macOS:**
     ```bash
     cp .streamlit/secrets.toml.example .streamlit/secrets.toml
     ```
3. Mở file `.streamlit/secrets.toml` và dán API key của bạn:
   ```toml
   API_key = "AIzaSy..."
   ```

### Bước 5: Khởi chạy ứng dụng Streamlit
```bash
streamlit run main.py
```
Sau khi chạy lệnh, trình duyệt sẽ tự động mở giao diện tại địa chỉ: `http://localhost:8501`.

---

## 💡 7. Hướng dẫn sử dụng
1. Tại màn hình chính, nhấn vào nút **"Browse files"** hoặc kéo thả file `revenue_data.xlsx` vào khu vực tải file.
2. Hệ thống sẽ ngay lập tức:
   - Hiển thị thông báo tải dữ liệu thành công.
   - Hiển thị biểu đồ cột trực quan về các danh mục có lượng hàng bán chạy nhất.
3. Nhấn nút **"Phân tích dữ liệu ngay"** trong mục **"🤖 AI Phân Tích & Gợi Ý Nhập Hàng"**.
4. Chờ vài giây để trợ lý AI Gemini phân tích và đọc các khuyến nghị chiến lược được hiển thị nổi bật trong khung thông báo.

---

## 🎯 8. Kế hoạch phát triển tiếp theo (Roadmap)
Dựa trên tài liệu thiết kế dự án [`plan.docx`](plan.docx):
- [x] **Giai đoạn 1**: Thiết kế template dữ liệu chuẩn và thiết lập môi trường dự án.
- [x] **Giai đoạn 2**: Xây dựng Data Pipeline với Pandas & OpenPyXL.
- [x] **Giai đoạn 3**: Trực quan hóa dữ liệu bán hàng với Matplotlib & Streamlit.
- [x] **Giai đoạn 4**: Tích hợp AI Gemini đề xuất chiến lược kinh doanh và gợi ý nhập hàng.
- [ ] **Giai đoạn 5**:
  - Áp dụng phân tích chuyên sâu **ABC Analysis** (Phân loại nhóm A chiếm 80% doanh thu, nhóm B chiếm 15%, nhóm C chiếm 5%).
  - Bổ sung công thức tính tự động số lượng cần nhập dựa trên tốc độ tiêu thụ trung bình ngày và số ngày dự trữ an toàn.
  - Đóng gói Docker và triển khai trực tuyến trên Streamlit Community Cloud.

---

## 👥 Tác giả
- **Tác giả:** Minh Quân ([@quantm10627](https://github.com/quantm10627))
- **Dự án:** Final Project môn Lập trình Python (GD1-CS.DATA17)
- **Đơn vị đào tạo:** Cybersoft Academy
