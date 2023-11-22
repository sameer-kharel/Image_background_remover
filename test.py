import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

def remove_background(input_image):
    inp = Image.open(input_image)
    output = remove(inp, alpha=True)
    return output

def main():
    st.set_page_config(page_title="Background Removal App", layout="centered")
    st.title("Background Removal App")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True, width=300)

        if st.button("Remove Background", key="remove_button"):
            with st.spinner("Removing background..."):
                output_image = remove_background(uploaded_file)
                st.image(output_image, caption="Image with Background Removed", use_column_width=True)

                buffered_output = BytesIO()
                output_image.save(buffered_output, format="PNG")

                if st.download_button("Download Processed Image", buffered_output.getvalue(), key="download_button", file_name="processed_image.png"):
                    st.success("Image downloaded successfully!")

if __name__ == "__main__":
    main()
