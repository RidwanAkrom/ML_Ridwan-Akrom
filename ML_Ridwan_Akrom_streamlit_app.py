
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit Title
st.title("Case Study Machine Learning GDGoC Sriwijaya University 2024/2025")

st.write("Nama: Ridwan Akrom")
st.write("Jurusan: Sistem Komputer 2022")

# Data Wrangling
st.subheader("1.Data Wrangling")
st.subheader("Dataset yang Digunakan")
st.write("Dataset yang digunakan dalam kasus ini adalah 'StudentPerformanceFactors.csv'.")
df = pd.read_csv("StudentPerformanceFactors.csv")
st.write(df)

st.subheader("Deskripsi Dataset")
st.write("""Kumpulan data ini memberikan gambaran komprehensif tentang berbagai faktor yang memengaruhi kinerja siswa dalam ujian. Ini
        mencakup informasi tentang kebiasaan belajar, kehadiran, keterlibatan orang tua, dan aspek lain yang memengaruhi keberhasilan akademik.""")
st.write("Berikut adalah deskripsi dari setiap kolom dalam dataset tersebut: ")
st.write("- Hours_Studied: Jumlah jam yang dihabiskan untuk belajar per minggu.")
st.write("- Attendance: Jumlah Persentase kehadiran siswa di kelas.")
st.write("- Parental_Involvement: Tingkat keterlibatan orang tua dalam pendidikan siswa (Low, Medium, High).")
st.write("- Access_to_Resources: Ketersediaan sumber daya pendidikan (Low, Medium, High).")
st.write("- Extracurricular_Activities: Partisipasi dalam kegiatan ekstrakurikuler (Yes, No).")
st.write("- Sleep_Hours: Jumlah rata-rata jam tidur per malam.")
st.write("- Previous_Scores: Skor dari ujian sebelumnya.")
st.write("- Motivation_Level: Tingkat motivasi siswa (Low, Medium, High).")
st.write("- Internet_Access: Ketersediaan akses internet (Yes, No).")
st.write("- Tutoring_Sessions: Jumlah sesi bimbingan belajar yang dihadiri per bulan.")
st.write("- Family_Income: Tingkat pendapatan keluarga (Low, Medium, High).")
st.write("- Teacher_Quality: Kualitas guru (Low, Medium, High).")
st.write("- School_Type: Jenis sekolah yang dihadiri (Public, Private).")
st.write("- Peer_Influence: Pengaruh teman sebaya terhadap prestasi akademik (Positive Neutral, Negative).")
st.write("- Physical_Activity: Jumlah rata-rata jam aktivitas fisik per minggu.")
st.write("- Learning_Disabilities: Adanya ketidakmampuan belajar (Yes, No).")
st.write("- Parental_Education_Level: Tingkat pendidikan tertinggi orang tua (High School, College, Postgraduate).")
st.write("- Distance_from_Home: Jarak dari rumah ke sekolah (Near, Moderate, Far).")
st.write("- Gender: Jenis kelamin siswa (Male, Female).")
st.write("- Exam_Score: Nilai ujian akhir.")

st.write(df.describe())
st.write(df.dtypes)
st.write("Dataset memiliki",df.shape[0],"baris dan",df.shape[1],"kolom.")
st.write("Dataset ini memiliki atribut 20 kolom data dan 6607 baris data. 7 kolom diantaranya bertipe data numerik dan 13 kolom bertipe data kategorikal.") 

st.subheader("2. Data Availability Checking")
st.write(df.isnull().sum())
st.write("Dataset ini memiliki", df.isnull().sum().sum(), "missing value. Diantaranya missing value terdapat pada kolom 'Teacher_Quality', 'Distance_from_Home', dan 'Parental_Education_Level'. Sehingga perlu dilakukan tindakan lebih lanjut dengan menghapus missing value tersebut")
df.dropna(inplace=True)
st.write(df.isnull().sum())
st.write("Setelah dilakukan pengapusan pada missing value, dilakukan pengecekan ulang dan tidak ada lagi missing value.")
st.write("Selain itu, dataset ini juga memiliki",df.duplicated().sum(),"duplicate value. Sehingga tidak perlu dilakukan tindak lanjut dengan menghapus duplicate value tersebut.")

st.subheader("3. Descriptive Statistics")
st.write(df.describe())
st.write("""
         - Rata-rata waktu belajar adalah 19.98 jam per minggu, dengan rentang 1-44 jam. 
         dengan mayoritas siswa belajar antara 16-24 jam")
         - Rata-rata kehadiran siswa mencapai 80% dengan rentang 60% -100%, menunjukkan kehadiran siswa yang konsisten.")
         - Durasi rata-rata tidur siswa adalah 7 jam per malam, dengan rentang 4-10 jam")
         - Nilai rata-rata ujian sebelumnya adalah 75,07, dengan rentang 50-100. mayoritas siswa memiliki nilai 63-88.")
         - Sedangkan untuk Nilai ujian memiliki rata-rata 67,25 dengan rentang 55-101. Sebagian 
         besar nilai siswa berada diantara 65-69.")
         - Dalam kolom 'Exam_Score', ditemukan data yang tidak normal atau anomaly. Terdapat nilai ujian yang 
         melebihi batas, yakni 101. Hal ini bisa terjadi karena beberapa alasan, seperti human error ataupun kesalahan penghitungan. """)


st.subheader("4. Exploratory Data Analysis")
st.subheader("Korelasi antara kolom Family_Income dan Teacher_Quality")

df_2dhist = pd.DataFrame({
    x_label: grp['Family_Income'].value_counts()
    for x_label, grp in df.groupby('Teacher_Quality')
})

plt.figure(figsize=(8, 8))
sns.heatmap(df_2dhist, cmap='viridis', annot=True, fmt=".1f")
plt.xlabel('Teacher_Quality')
plt.ylabel('Family_Income')

# Tampilkan heatmap di Streamlit
st.pyplot(plt)
#Dewskrip dari heatmap
st.write("""Guru dengan kualitas Medium mendominasi distribusi untuk semua tingkat 
        pendapatan keluarga, menunjukkan bahwa kualitas ini paling umum diterima siswa, terlepas dari status ekonomi mereka.""")
st.write("""
        Siswa dari keluarga berpendapatan tinggi memiliki kemungkinan lebih rendah untuk mendapatkan 
        guru dengan kualitas Low, sementara siswa dari keluarga berpendapatan rendah lebih sering menerima guru 
        High daripada kategori lainnya. Hal ini mungkin terjadi pada sekolah prestisius ataupun sekolah unggulan/favorit yang 
        didukung dengan adanya beasiswa ataupun program pendidikan khusus.
""")

st.subheader("Korelasi antara kolom Parental_Education_Level dan Parental_Involvement")
df_2dhist = pd.DataFrame({
    x_label: grp['Parental_Involvement'].value_counts()
    for x_label, grp in df.groupby('Parental_Education_Level')
})

plt.figure(figsize=(8, 8))
sns.heatmap(df_2dhist, cmap='viridis', annot=True, fmt=".1f")
plt.xlabel('Parental_Education_Level')
plt.ylabel('Parental_Involvement')

# Tampilkan heatmap di Streamlit
st.pyplot(plt)  

#Deskripsi heatmap diatas
st.write("""
       Orang tua dengan pendidikan *High School* cenderung paling aktif berpartisipasi dalam 
         keterlibatan kategori *Medium*. Hal ini bisa mengindikasikan bahwa orang tua dengan pendidikan 
         menengah mungkin memiliki lebih banyak waktu atau prioritas untuk terlibat dalam pendidikan anak mereka 
         dibandingkan orang tua dengan pendidikan *Postgraduate* yang mungkin lebih sibuk dengan pekerjaan atau 
         tanggung jawab lainnya. Tingkat pendidikan orang tua juga turut menentukan kesibukan mereka terhadap 
         pekerjaan dan prioritas lainnya, serta memengaruhi kesadaran mereka terhadap pentingnya memberikan dukungan 
         kepada siswa dalam proses pembelajaran.
""")

st.subheader("5. Data Visualization")
st.subheader("Visualisasi hubungan kolom Motivation_Level dan Peer_Influence terhadap Exam_Score")
sns.catplot(data=df, x="Motivation_Level", y="Exam_Score", hue='Peer_Influence',kind="box")

# Tampilan plot di Streamlit
st.pyplot(plt)

#Deskripsi plot diatas
st.write("""
        Berdasarkan visualisasi boxplot, Peer Influence tampaknya memiliki pengaruh kecil terhadap performa ujian 
         siswa. Siswa yang berada di bawah pengaruh positif cenderung memiliki skor ujian yang sedikit lebih tinggi 
         dibandingkan siswa dengan pengaruh netral atau negatif. Hal ini terlihat dari pergeseran nilai median yang 
         lebih tinggi pada kategori Positive Peer Influence. Meskipun demikian, perbedaannya tidak terlalu signifikan, 
         mengindikasikan bahwa faktor lain mungkin lebih berperan dalam menentukan skor ujian siswa.
         """)

st.write("""
        Selain itu, tingkat motivasi (Motivation Level) tampaknya tidak memiliki pengaruh yang signifikan terhadap 
         performa ujian. Hal ini ditunjukkan oleh nilai median skor ujian yang relatif konsisten di semua tingkat 
         motivasi, baik Low, Medium, maupun High. Sebaran data pada setiap kategori motivasi juga menunjukkan distribusi 
         yang serupa, dengan adanya outlier di semua kategori.
         """)


st.subheader("Visualisasi hubungan kolom Internet_Access dan Access_to_Resources terhadap Exam_Score")
sns.catplot(data=df, x="Internet_Access", y="Exam_Score", hue='Access_to_Resources',kind="box")

# Tampilan plot di Streamlit
st.pyplot(plt)

#Deskripsi plot diatas
st.write("""
        Visualisasi ini menunjukkan bahwa siswa yang memiliki akses internet cenderung memiliki skor ujian lebih 
         tinggi dibandingkan yang tanpa akses internet. Akses ke sumber daya pendidikan (Access_to_Resources) juga berpengaruh 
         signifikan, di mana peserta dengan akses sumber daya pendidikan tinggi ("High") memiliki skor ujian lebih baik, sementara yang 
         dengan akses rendah ("Low") memiliki skor lebih rendah. Selain itu, kelompok dengan akses sumber daya pendidikan tinggi pada "Yes" 
         memiliki distribusi skor yang lebih lebar, dengan banyaknya outlier yang menunjukkan variasi skor yang besar. Secara 
         keseluruhan, akses internet dan sumber daya yang memadai dapat meningkatkan skor ujian.
         """)

st.subheader("6. Conclusion")
st.write("""
       Dataset ini memberikan wawasan penting tentang berbagai faktor yang memengaruhi kinerja akademik siswa, termasuk kebiasaan 
         belajar, akses sumber daya, keterlibatan orang tua, dan kualitas pendidikan. Berdasarkan analisis, ditemukan bahwa akses 
         internet dan sumber daya pendidikan berkontribusi signifikan terhadap skor ujian. Faktor-faktor seperti kualitas guru, tingkat 
         pendidikan orang tua, dan pengaruh teman sebaya juga memengaruhi hasil siswa, meskipun pengaruhnya tidak selalu konsisten.
        """)
st.write("""
        Dalam bagian descriptive statistics menunjukkan adanya anomali data, seperti skor ujian di atas 100, yang memerlukan pemeriksaan lebih 
         lanjut. Sementara itu, tidak adanya nilai duplikat dan penanganan missing value memastikan bahwa dataset ini siap untuk analisis lebih 
         mendalam. Secara keseluruhan, kombinasi antara sumber daya pendidikan yang memadai, kualitas guru yang baik, dan keterlibatan orang tua
         menjadi faktor utama yang mendukung keberhasilan akademik siswa.
         """)