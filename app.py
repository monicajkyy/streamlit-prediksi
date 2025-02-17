import pickle
import streamlit as st
import numpy as np
import sklearn 

# Load model yang sudah disimpan
model = pickle.load(open('prd.sav', 'rb'))

# Judul Aplikasi
st.title('Prediksi Produksi Jagung')

# Input dari pengguna
luas_lahan = st.text_input('Masukkan Luas Lahan (ha)')
luas_panen = st.text_input('Masukkan Luas Panen (ha)')
produktivitas = st.text_input('Masukkan Produktivitas (kw/ha)')

# Tombol Prediksi
if st.button('Prediksi Produksi'):
    try:
        # Konversi input ke float
        luas_lahan = float(luas_lahan)
        luas_panen = float(luas_panen)
        produktivitas = float(produktivitas)

        # Membentuk array input untuk model
        input_data = np.array([[luas_lahan, luas_panen, produktivitas]])

        # Melakukan prediksi produksi
        prediksi_produksi = model.predict(input_data)[0]

        # Menampilkan hasil prediksi
        st.success(f'Prediksi Produksi Jagung: {prediksi_produksi:.2f} kw')

    except ValueError:
        st.error('Harap masukkan angka yang valid!')

