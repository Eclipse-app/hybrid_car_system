import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(layout="wide", page_title="Hybrid Car System")

# ---------- Sidebar ----------
st.sidebar.title("🚗 Gibrid avtomobillar")
page = st.sidebar.radio("Bo‘lim", [
    "Kirish",
    "Parallel Hybrid",
    "Series Hybrid",
    "Series-Parallel Hybrid",
    "Plug-in Hybrid",
    "Mild Hybrid",
    "Video qo‘llanma"
])

# ---------- Dizayn ----------
st.markdown("""
<style>
.block {
    padding:30px;
    border-radius:20px;
    background:linear-gradient(135deg,#0A66C2,#00c6ff);
    color:white;
    box-shadow:0px 8px 25px rgba(0,0,0,0.3);
}
.card {
    padding:20px;
    border-radius:15px;
    background:white;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# Kirish
# =====================================================
if page == "Kirish":
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.title("Gibrid avtomobil tizimlari")
    st.write("""
Gibrid avtomobil — bu ichki yonuv dvigateli (ICE) va elektr motor kombinatsiyasida ishlovchi transport vositasi.  
Ularning asosiy maqsadi:
- Yoqilg‘i sarfini kamaytirish
- CO₂ chiqindilarini kamaytirish
- Energiya samaradorligini oshirish
- Shahar sharoitida jim va ekologik harakat
""")
    st.markdown('</div>', unsafe_allow_html=True)

    st.subheader("Gibrid avtomobil turlari")

    col1, col2, col3 = st.columns(3)

    col1.markdown("**Parallel Hybrid**  \nDvigatel va motor birga ishlaydi")
    col2.markdown("**Series Hybrid**  \nHarakat faqat elektr orqali")
    col3.markdown("**Series-Parallel**  \nEng samarali kombinatsiya")

    col1, col2, col3 = st.columns(3)
    col1.markdown("**Plug-in Hybrid**  \nTashqi zaryadlanadi")
    col2.markdown("**Mild Hybrid**  \nYordamchi tizim")
    col3.markdown("**Full Hybrid**  \nElektrda mustaqil harakatlana oladi")

    st.progress(80)
    st.info("Zamonaviy avtomobillarning asosiy yo‘nalishi — gibrid va elektr texnologiyalar.")

# =====================================================
# Parallel Hybrid
# =====================================================
elif page == "Parallel Hybrid":
    st.header("Parallel Hybrid tizimi")

    col1, col2 = st.columns([1,2])
    img = Image.open("models/images/parallel.png")
    col1.image(img)

    col2.markdown("""
### Ishlash prinsipi
- ICE va elektr motor birgalikda g‘ildirakni aylantiradi
- Past tezlikda motor
- Tezlanishda ikkala manba ishlaydi
- Tormozda energiya qayta tiklanadi (regeneratsiya)
""")

    with st.expander("Texnik xususiyatlar"):
        st.write("""
- Samaradorlik: 30–40% yoqilg‘i tejaladi
- Qo‘llaniladi: Toyota Camry Hybrid, Honda Insight
- Afzallik: oddiy va ishonchli tizim
""")

    st.subheader("Energiya taqsimoti")
    st.bar_chart({"Engine":[60], "Motor":[40]})

# =====================================================
# Series Hybrid
# =====================================================
elif page == "Series Hybrid":
    st.header("Series Hybrid tizimi")

    col1, col2 = st.columns([1,2])
    img = Image.open("models/images/series.png")
    col1.image(img)

    col2.markdown("""
### Ishlash prinsipi
- Dvigatel g‘ildirakni aylantirmaydi
- ICE → Generator → Batareya
- Harakat faqat elektr motor orqali
""")

    with st.expander("Afzalliklari"):
        st.write("""
- Shahar sharoitida juda samarali
- Mexanik uzatma yo‘q
- Kam shovqin
""")

    st.bar_chart({"Generator":[50], "Battery":[30], "Motor":[20]})

# =====================================================
# Series-Parallel Hybrid
# =====================================================
elif page == "Series-Parallel Hybrid":
    st.header("Series-Parallel Hybrid (Eng samarali tizim)")

    col1, col2 = st.columns([1,2])
    img = Image.open("models/images/series_parallel.png")
    col1.image(img)

    mode = st.selectbox("Rejimni tanlang", ["Electric Mode", "Series Mode", "Parallel Mode"])

    if mode == "Electric Mode":
        st.success("Past tezlikda faqat elektr motor ishlaydi")
    elif mode == "Series Mode":
        st.info("ICE generator sifatida ishlaydi")
    else:
        st.warning("ICE + Motor birga ishlaydi")

    with st.expander("Qayerda ishlatiladi?"):
        st.write("""
- Toyota Prius
- Lexus Hybrid seriyasi
- Eng optimal yoqilg‘i samaradorligi
""")

# =====================================================
# Plug-in Hybrid
# =====================================================
elif page == "Plug-in Hybrid":
    st.header("Plug-in Hybrid")

    col1, col2 = st.columns([1,2])
    img = Image.open("models/images/plugin.png")
    col1.image(img)

    col2.markdown("""
### Xususiyatlari
- Tashqi elektrdan zaryadlanadi
- 40–100 km faqat elektr rejimi
- Katta batareya (10–20 kWh)
""")

    distance = st.slider("Elektr rejimi masofasi (km)", 20, 100, 60)
    st.write(f"Elektr rejimi: {distance} km")

# =====================================================
# Mild Hybrid
# =====================================================
elif page == "Mild Hybrid":
    st.header("Mild Hybrid")

    col1, col2 = st.columns([1,2])
    img = Image.open("models/images/mild.png")
    col1.image(img)

    col2.markdown("""
### Xususiyatlari
- 48V tizim
- Elektr motor faqat yordam beradi
- Mustaqil harakatlana olmaydi
- 10–15% yoqilg‘i tejaladi
""")

    st.progress(15)

# =====================================================

# =====================================================
# Video qo‘llanma
# =====================================================
elif page == "Video qo‘llanma":
    st.header("Gibrid avtomobillar haqida video")
    st.video("https://www.youtube.com/watch?v=SHRrhyGYbb8")

    st.info("Video: Hybrid tizimlarning ishlash prinsipi va taqqoslanishi.")













