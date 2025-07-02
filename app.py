import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

st.set_page_config(page_title="Image Generator", layout="centered")

@st.cache_resource
def load_pipeline():
    # Ganti dtype float32 untuk CPU, hilangkan use_auth_token jika tidak perlu
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32,
    )
    pipe.enable_attention_slicing()  # hemat RAM, penting di CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe.to(device)
    return pipe

pipe = load_pipeline()

st.title("🎨 Image Generator AI")
prompt = st.text_input("Masukkan prompt (dalam Bahasa Indonesia/Inggris):", "sebuah kota futuristik di atas awan")

if st.button("Generate"):
    with st.spinner("Membuat gambar..."):
        image = pipe(prompt, height=256, width=256).images[0]  # resolusi lebih kecil untuk CPU
        st.image(image, caption="Hasil dari prompt", use_column_width=True)
        image.save("assets/samples/generated_image.png")
