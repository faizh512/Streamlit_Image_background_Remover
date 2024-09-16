import streamlit as st
from rembg import remove
from PIL import Image
import io
st.set_page_config(layout="wide", page_title="Image Backdround Remover")
st.sidebar.header("Background Remover")
img = st.sidebar.file_uploader("Upload the image", type=["jpg", "jpeg", "png"])
Max_IMAGE_size=5*1024*1024
if img is not None:
    if img.size>Max_IMAGE_size:
        st.warning("size Too Large")
    # Create two columns
    else:
            col1, col2 = st.columns(2)


            # Load the image using PIL
            image = Image.open(img)
            
            # Remove the background
            output_image = remove(image)
            
            # Display the original and processed images side by side
            with col1:
                st.image(image, caption="Original Image")
            with col2:
                st.image(output_image, caption="Processed Image")
            
            # Save the output image to bytes for download
            img_byte_arr = io.BytesIO()
            output_image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            
            #Provide download button in the sidebar
            st.sidebar.download_button("Download Image", data=img_byte_arr, file_name="output_image.png", mime="image/png")
            # processed_image=output_image.tobytes()
            # st.sidebar.download_button("Download Image")
else:
    st.write("Please upload an image to remove the background.")
