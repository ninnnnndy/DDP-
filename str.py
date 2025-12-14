import streamlit as st

# halaman utama
st.title('Aplikasi Perhitungan Luas Bangun Datar')
st.title('Buatan Anak SI')

menu = st.sidebar.selectbox('Pilih Aplikasi', ['Luas Persegi', 'Luas Segitiga', 'Luas Lingkaran', 'Luas Persegi Panjang', 'Luas Jajar Genjang'])

if menu == 'Luas Persegi':
    st.write('Ini halaman untuk menghitung luas persegi')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi.jpg', caption='rumus persegi')
    sisi = st.number_input('Masukkan sisi', min_value=0)
    if st.button('Hitung'):
        luas = sisi * sisi
        st.success(f'Luas persegi adalah {luas}')

elif menu == 'Luas Segitiga':
    st.write('Ini halaman untuk menghitung luas segitiga')
    st.image('https://idschool.net/wp-content/uploads/2018/03/Rumus-Luas-Segitiga.png')
    def segitiga (alas, tinggi):
        return 0.5 * alas * tinggi
    
    alas = st.number_input('Masukkan alas', min_value=0)
    tinggi = st.number_input('Masukkan tinggi', min_value=0)

    if st.button('Hitung'):
        hasil = segitiga (alas, tinggi)
        st.success(f'Luas segitiga adalah {hasil}')

elif menu == 'Luas Lingkaran':
    st.write('Ini halaman untuk menghitung luas lingkaran')
    st.image('https://mamatematika.wordpress.com/wp-content/uploads/2016/11/38.png')

    def lingkaran(jari_jari):
        return 22/7 * jari_jari * jari_jari

    jari_jari = st.number_input('Masukkan jari-jari', min_value= 0)

    if st.button('Hitung'):
        hasil = lingkaran(jari_jari)
        st.success(f'Luas lingkaran adalah {hasil}')

elif menu == 'Luas Persegi Panjang':
    st.write('Ini halaman untuk menghitung luas persegi panjang')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwwt-1oZfAbXo9CzBW6Hc7RdVFl0DJoTgxWQ&s')

    def persegi_panjang(panjang, lebar):
        return panjang * lebar
    
    panjang = st.number_input('Masukkan panjang', min_value= 0)
    lebar = st.number_input('Masukkan lebar', min_value= 0)

    if st.button('Hitung'):
        hasil = persegi_panjang(panjang, lebar)
        st.success(f'Luas persegi panjanng adalah {hasil}')

elif menu == 'Luas Jajar Genjang':
    st.write('Ini halaman untuk menghitung luas jajar genjang')
    st.image('https://i.pinimg.com/1200x/7e/11/16/7e1116b65eab976c92e9592d2f903cbf.jpg')

def jajar_genjang(alas, tinggi):
          return alas * tinggi
alas = st.number_input('Masukkan alas', min_value= 0)
tinggi = st.number_input('Masukkan tinggi', min_value= 0)
if st.button('Hitung'):
    hasil = jajar_genjang(alas, tinggi)
st.success(f'luas jajar genjang adalah {hasil}')
