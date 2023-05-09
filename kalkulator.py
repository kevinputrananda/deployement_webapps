import streamlit as st

def main():
    st.sidebar.title("Menu")
    options = ["Penetapan Konsentrasi NaOH", "Penetapan Konsentrasi HCl", "Penetapan Konsentrasi KMnO₄", "Penetapan Konsentrasi Tio", "Penetapan Konsentrasi EDTA", "Penetapan Kadar Asam Asetat dalam Cuka Makanan", "Penetapan Kadar Besi dalam Sampel Garam"]
    choice = st.sidebar.selectbox("Select an option", options)
    
    if choice == "Penetapan Konsentrasi NaOH":
        st.title("Perhitungan Konsentrasi NaOH")
        st.header('Identitas Penguji')
        nama = st.text_input('Nama Penguji')
        nim = st.text_input('NIM')
        instansi = st.text_input('Instansi')
        tanggal = st.date_input('Tanggal')

        st.header('Perhitungan')

        bobot = st.number_input('Masukkan Nilai Bobot (mg)',format="%.4f")
        faktor = st.number_input('Masukkan Nilai Faktor Pengali')
        volume = st.number_input('Masukkan Nilai Volume (mL)')
        BE = st.number_input('Masukkan Nilai BE')

        tombol = st.button('Hitung Konsentrasi')

        if tombol:
            nilai_konsentrasi = bobot/(faktor*volume*BE)
            st.success(f'Nilai konsentrasi adalah {nilai_konsentrasi} N')
            st.success(f'Nama : {nama}')
            st.success(f'NIM : {nim}')
            st.success(f'Instansi : {instansi}')
            st.success(f'Tanggal : {tanggal}')
                       
    
    elif choice == "Penetapan Konsentrasi HCl":
        st.title("Perhitungan Konsentrasi HCl")
        st.header('Identitas Penguji')
        nama = st.text_input('Nama Penguji')
        nim = st.text_input('NIM')
        instansi = st.text_input('Instansi')
        tanggal = st.date_input('Tanggal')

        st.header('Perhitungan')

        bobot = st.number_input('Masukkan Nilai Bobot (mg)',format="%.4f")
        faktor = st.number_input('Masukkan Nilai Faktor Pengali')
        volume = st.number_input('Masukkan Nilai Volume (mL)')
        BE = st.number_input('Masukkan Nilai BE')

        tombol = st.button('Hitung Konsentrasi')

        if tombol:
            nilai_konsentrasi = bobot/(faktor*volume*BE)
            st.success(f'Nilai konsentrasi adalah {nilai_konsentrasi} N')
            st.success(f'Nama : {nama}')
            st.success(f'NIM : {nim}')
            st.success(f'Instansi : {instansi}')
            st.success(f'Tanggal : {tanggal}')
            
    elif choice == "Penetapan Konsentrasi KMnO₄":
        st.title("Perhitungan Konsentrasi KMnO₄")
        st.header('Identitas Penguji')
        nama = st.text_input('Nama Penguji')
        nim = st.text_input('NIM')
        instansi = st.text_input('Instansi')
        tanggal = st.date_input('Tanggal')

        st.header('Perhitungan')

        bobot = st.number_input('Masukkan Nilai Bobot (mg)',format="%.4f")
        faktor = st.number_input('Masukkan Nilai Faktor Pengali')
        volume = st.number_input('Masukkan Nilai Volume (mL)')
        BE = st.number_input('Masukkan Nilai BE')

        tombol = st.button('Hitung Konsentrasi')

        if tombol:
            nilai_konsentrasi = bobot/(faktor*volume*BE)
            st.success(f'Nilai konsentrasi adalah {nilai_konsentrasi} N')
            st.success(f'Nama : {nama}')
            st.success(f'NIM : {nim}')
            st.success(f'Instansi : {instansi}')
            st.success(f'Tanggal : {tanggal}')
            
    elif choice == "Penetapan Konsentrasi Tio":
        st.title("Perhitungan Konsentrasi Tio")
        st.header('Identitas Penguji')
        nama = st.text_input('Nama Penguji')
        nim = st.text_input('NIM')
        instansi = st.text_input('Instansi')
        tanggal = st.date_input('Tanggal')

        st.header('Perhitungan')

        bobot = st.number_input('Masukkan Nilai Bobot (mg)',format="%.4f")
        volume = st.number_input('Masukkan Nilai Volume (mL)')
        BE = st.number_input('Masukkan Nilai BE')

        tombol = st.button('Hitung Konsentrasi')

        if tombol:
            nilai_konsentrasi = bobot/(volume*BE)
            st.success(f'Nilai konsentrasi adalah {nilai_konsentrasi} N')
            st.success(f'Nama : {nama}')
            st.success(f'NIM : {nim}')
            st.success(f'Instansi : {instansi}')
            st.success(f'Tanggal : {tanggal}')
            
    elif choice == "Penetapan Konsentrasi EDTA":
        st.title("Perhitungan Konsentrasi EDTA")
        st.header('Identitas Penguji')
        nama = st.text_input('Nama Penguji')
        nim = st.text_input('NIM')
        instansi = st.text_input('Instansi')
        tanggal = st.date_input('Tanggal')

        st.header('Perhitungan')

        bobot = st.number_input('Masukkan Nilai Bobot (mg)',format="%.4f")
        faktor = st.number_input('Masukkan Nilai Faktor Pengali')
        volume = st.number_input('Masukkan Nilai Volume (mL)')
        BE = st.number_input('Masukkan Nilai BE')

        tombol = st.button('Hitung Konsentrasi')

        if tombol:
            nilai_konsentrasi = bobot/(faktor*volume*BE)
            st.success(f'Nilai konsentrasi adalah {nilai_konsentrasi} M')
            st.success(f'Nama : {nama}')
            st.success(f'NIM : {nim}')
            st.success(f'Instansi : {instansi}')
            st.success(f'Tanggal : {tanggal}')
            
    elif choice == "Penetapan Kadar Asam Asetat dalam Cuka Makanan":
        st.title("Penetapan Kadar Asam Asetat dalam Cuka Makanan")
        st.header('Identitas Penguji')
        nama = st.text_input('Nama Penguji')
        nim = st.text_input('NIM')
        instansi = st.text_input('Instansi')
        tanggal = st.date_input('Tanggal')

        st.header('Perhitungan')

        konsentrasi = st.number_input('Masukkan Nilai Konsentrasi (mg)',format="%.4f")
        vn = st.number_input('Masukkan Nilai Volume Titran (mL)')
        vt = st.number_input('Masukkan Nilai Volume Titrat (mL)')
        BE = st.number_input('Masukkan Nilai BE')
        fp = st.number_input('Masukkan Faktor Pengali')

        tombol = st.button('Hitung Kadar')

        if tombol:
            nilai_kadar = (vn*konsentrasi*BE)/vt/1000*fp*100
            st.success(f'Nilai kadar adalah {nilai_kadar} %(b/v)')
            st.success(f'Nama : {nama}')
            st.success(f'NIM : {nim}')
            st.success(f'Instansi : {instansi}')
            st.success(f'Tanggal : {tanggal}')
            
    elif choice == "Penetapan Kadar Besi dalam Sampel Garam":
        st.title("Penetapan Kadar Besi dalam Sampel Garam Secara Permanganometri")
        st.header('Identitas Penguji')
        nama = st.text_input('Nama Penguji')
        nim = st.text_input('NIM')
        instansi = st.text_input('Instansi')
        tanggal = st.date_input('Tanggal')

        st.header('Perhitungan')

        vn = st.number_input('Masukkan Nilai Volume Titran (mL)')
        konsentrasi = st.number_input('Masukkan Nilai Konsentrasi (mg)',format="%.4f")
        vc = st.number_input('Masukkan Nilai Volume Contoh (mL)')
        BE = st.number_input('Masukkan Nilai BE')
        
        tombol = st.button('Hitung Kadar')

        if tombol:
            nilai_kadar = (vn*konsentrasi*BE)/vc/1000*100
            st.success(f'Nilai kadar Na₂CO₃ adalah {nilai_kadar} %(b/v)')
            st.success(f'Nama : {nama}')
            st.success(f'NIM : {nim}')
            st.success(f'Instansi : {instansi}')
            st.success(f'Tanggal : {tanggal}')
            
    else:
        st.title("Welcome to Settings Page!")
        st.write("Here you can update your application settings.")

if __name__ == "__main__":
    main()
