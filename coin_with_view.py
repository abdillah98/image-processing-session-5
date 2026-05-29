import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Coin Counter App")

uploaded_file = st.file_uploader(
    "Upload Gambar",
    type=['jpg', 'png', 'jpeg']
)

if uploaded_file is not None:

    # =========================
    # Load gambar
    # =========================
    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    img = cv2.imdecode(file_bytes, 1)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    st.subheader("Gambar Asli")
    st.image(img_rgb)

    # =========================
    # Grayscale
    # =========================
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # =========================
    # Blur
    # =========================
    blur = cv2.GaussianBlur(gray, (9,9), 0)

    # =========================
    # Threshold
    # =========================
    _, thresh = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    st.subheader("Threshold")
    st.image(thresh)

    # =========================
    # Morphology
    # =========================
    kernel = np.ones((3,3), np.uint8)

    morph = cv2.morphologyEx(
        thresh,
        cv2.MORPH_OPEN,
        kernel,
        iterations=2
    )

    # =========================
    # Contour Detection
    # =========================
    contours, _ = cv2.findContours(
        morph,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    count = 0

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area > 500:

            count += 1

            x, y, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(
                img_rgb,
                (x, y),
                (x+w, y+h),
                (255, 0, 0),
                2
            )

    # =========================
    # Hasil
    # =========================
    st.subheader("Hasil Deteksi")
    st.image(img_rgb)

    st.success(f"Jumlah Koin Terdeteksi: {count}")