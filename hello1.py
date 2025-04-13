import streamlit as st
import pandas as pd

st.title("🧹 Qualité des Données - Streamlit")

# 1. Upload de fichier
uploaded_file = st.file_uploader("📂 Importer un fichier CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Aperçu des données")
    st.dataframe(df)

    # 2. Valeurs manquantes
    st.subheader("🔍 Valeurs manquantes")
    missing = df.isnull().sum()
    st.write(missing[missing > 0])

    # 3. Détection de doublons
    st.subheader("🟠 Doublons")
    duplicates = df[df.duplicated()]
    if not duplicates.empty:
        st.warning(f"{len(duplicates)} doublons trouvés.")
        st.dataframe(duplicates)
    else:
        st.success("Aucun doublon trouvé.")

    # 4. Statistiques générales
    st.subheader("📈 Statistiques")
    st.write(df.describe())

    # 5. Option de nettoyage
    if st.button("🧼 Supprimer les doublons"):
        df = df.drop_duplicates()
        st.success("Doublons supprimés.")
        st.dataframe(df)

else:
    st.info("Veuillez importer un fichier CSV pour commencer.")
