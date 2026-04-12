import streamlit as st
import requests
from PIL import Image
import os
import json

if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="AI Medical System", layout="wide")

# =========================
# STYLE
# =========================
st.markdown("""
<style>
.big-title {
    font-size: 40px;
    font-weight: bold;
    color: #00FFAA;
}
.image-card {
    text-align: center;
}
.label-normal {
    color: #00FFAA;
    font-weight: bold;
}
.label-pneumonia {
    color: red;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown('<div class="big-title">🧠 AI Medical Image Analysis</div>', unsafe_allow_html=True)
st.write("### Detect Pneumonia from Chest X-rays")

# =========================
# UPLOAD
# =========================
uploaded_file = st.file_uploader(
    "Upload X-ray Image",
    type=["jpg", "png"],
    key=st.session_state.uploader_key
)

col1, col2 = st.columns([1, 1])

# =========================
# SHOW IMAGE
# =========================
if uploaded_file:
    image = Image.open(uploaded_file)
    col1.image(image, caption="Uploaded Image", width=300)

    if st.button("🔍 Analyze Image"):

        with st.spinner("Analyzing..."):
            response = requests.post(
                "http://127.0.0.1:5000/predict",
                files={"image": ("image.jpg", uploaded_file.getvalue(), "image/jpeg")}
            )

            result = response.json()

        if "error" in result:
            st.error(result["error"])

        else:
            st.success("Analysis Complete")

            with col2:
                if result["prediction"] == "PNEUMONIA DETECTED":
                    st.error(f"⚠️ {result['prediction']}")
                else:
                    st.success(f"✅ {result['prediction']}")

                st.metric("Confidence", f"{result['confidence']*100:.2f}%")
                st.write(f"📁 {result['image_saved_as']}")

# =========================
# IMAGE GALLERY WITH LABELS
# =========================
st.write("---")
st.write("## 📂 Analyzed Images")

history_file = "outputs/history.json"

if not os.path.exists(history_file):
    st.write("No images yet")
else:
    with open(history_file, "r") as f:
        history = json.load(f)

    if len(history) == 0:
        st.write("No images yet")
    else:
        cols = st.columns(6)  # ✅ 6 images per row

        for i, item in enumerate(reversed(history)):
            img_path = os.path.join("outputs", item["image"])

            if os.path.exists(img_path):
                with cols[i % 6]:

                    st.image(img_path, width=800)

                    # LABEL
                    if item["result"] == "PNEUMONIA DETECTED":
                        st.markdown(
                            f'<div class="label-pneumonia">⚠️ {item["result"]}</div>',
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            f'<div class="label-normal">✅ {item["result"]}</div>',
                            unsafe_allow_html=True
                        )

                    st.write(f"{item['confidence']*100:.2f}%")
