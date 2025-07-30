import streamlit as st
from paddleocr import PaddleOCR
from gtts import gTTS
from googletrans import Translator
import json
import os
from PIL import Image
import tempfile

# Tạo thư mục output nếu chưa có
os.makedirs("res_output", exist_ok=True)

# Khởi tạo OCR
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)

translator = Translator()

st.title("OCR Hóa đơn + Chuyển văn bản thành giọng nói")

# Upload ảnh
uploaded_file = st.file_uploader("Tải lên ảnh hóa đơn (.jpg/.png)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Hiển thị ảnh gốc
    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh hóa đơn đã tải lên", use_container_width=True)

    # Lưu ảnh tạm để PaddleOCR xử lý
    tmp_img_path = os.path.join(tempfile.gettempdir(), "uploaded_image.jpg")
    image.save(tmp_img_path)

    # Chạy OCR
    result = ocr.predict(tmp_img_path)

    # Lưu kết quả
    json_path = "res_output/res_full.json"
    img_path = "res_output/res_full.jpg"
    for res in result:
        res.save_to_json(json_path)
        res.save_to_img(img_path)

    # **Hiển thị ảnh kết quả OCR ngay dưới ảnh gốc**
    if os.path.exists(img_path):
        st.image(img_path, caption="Ảnh kết quả OCR", use_container_width=True)

    # Đọc lại file JSON
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    rec_texts = data.get("rec_texts", [])
    all_text = ". ".join(rec_texts)

    # Hiển thị văn bản OCR
    st.subheader("Văn bản nhận diện được:")
    for line in rec_texts:
        st.markdown(f"- {line}")

    if all_text.strip():
        # Âm thanh tiếng gốc
        mp3_path = "res_output/res_full_audio.mp3"
        tts = gTTS(text=all_text, lang="en")
        tts.save(mp3_path)
        st.audio(mp3_path, format="audio/mp3")

        # Dịch và đọc tiếng Việt
        if st.button("Dịch sang tiếng Việt & đọc"):
            translated_text = translator.translate(all_text, dest="vi").text
            st.subheader("Bản dịch tiếng Việt:")
            st.write(translated_text)

            vi_mp3_path = "res_output/res_full_audio_vi.mp3"
            tts_vi = gTTS(text=translated_text, lang="vi")
            tts_vi.save(vi_mp3_path)
            st.success("Đã tạo audio tiếng Việt!")
            st.audio(vi_mp3_path, format="audio/mp3")
    else:
        st.warning("Không có nội dung để chuyển thành giọng nói.")

