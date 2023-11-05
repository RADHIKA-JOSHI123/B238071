import streamlit as st
import cv2
import numpy as np

# Define image transformation functions
def rotate_image(image, angle):
    rows, cols, _ = image.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, M, (cols, rows))
    return rotated_image

def resize_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
    return resized_image

def blur_image(image, kernel_size):
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return blurred_image

def grayscale_conversion(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayscale_image = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2BGR)
    return grayscale_image

# Streamlit UI
st.title("Image Transformation App")
image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if image is not None:
    image = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_COLOR)

    # Display original image
    st.image(image, channels="BGR", use_column_width=True, caption="Original Image")

    # Choose transformation method
    method = st.selectbox("Select Transformation Method", ["Rotate", "Resize", "Blur", "Grayscale"])

    if method == "Rotate":
        angle = st.slider("Select Rotation Angle", -180, 180, 0)
        transformed_image = rotate_image(image, angle)

    elif method == "Resize":
        scale_percent = st.slider("Select Resize Scale (%)", 10, 200, 100)
        transformed_image = resize_image(image, scale_percent)

    elif method == "Blur":
        kernel_size = st.slider("Select Kernel Size", 1, 11, 3)
        transformed_image = blur_image(image, kernel_size)

    elif method == "Grayscale":
        transformed_image = grayscale_conversion(image)

    # Display transformed image
    st.image(transformed_image, channels="BGR", use_column_width=True, caption="Transformed Image")
