import streamlit as st
import datetime
import matplotlib.pyplot as plt

# Banner laterale con descrizione e categorie di voto
st.sidebar.title("Info su SagraAdvisor")
st.sidebar.markdown(
    """
    **SagraAdvisor** nasce per giudicare le sagre con rigore e ironia.

    Non siamo Food Bloggers. Solo verità e patatine fritte.

    **Criteri di valutazione (1-10):**
    1. **Parcheggio**: se non trovi posto, è un disastro.
    2. **Menù**: varietà o qualità? Meglio entrambe.
    3. **Special**: il piatto che domina la sagra.
    4. **Rabosello**: la base. Se manca, serata rovinata.
    5. **Frittella**: se c'è, si giudica.
    6. **Intrattenimento**: dai brucamela ai balli in acciaio.
    7. **Location**: atmosfera e contesto.
    8. **Prezzo**: Cracco? No grazie. Deve essere accessibile.
    9. **Pesca di Beneficenza**: sempre una sorpresa.
    10. **Verdetto Finale**: la media o l'impressione generale.
    """
)

# Base URL GitHub per le immagini
github_base_url = "https://raw.githubusercontent.com/battistg/sagra_advisor/main/"

sagre = {
    "2025-05-16": [
        {
            "nome": "Sagra di San Isidoro di Schiavon (VI)",
            "menu_foto": [github_base_url + "IMG_0266.jpeg"],
            "piatti_foto": [
                github_base_url + "IMG_0267.jpeg",
                github_base_url + "IMG_0270.jpeg",
                github_base_url + "IMG_0271.jpeg"
            ],
            "menu": {
                "Gnocchi burro salvia": "6,00€",
                "Gnocchi ragù": "6,50€",
                "Gnocchi ragù d'anatra": "7,50€",
                "Frittura mista di pesce con polenta e patatine fritte": "15,00€",
                "Porzione patatine fritte": "3,50€",
                "Grigliata mista (costine, salsiccia, galletto)": "13,00€",
                "Costine e salsiccia (con patatine o fagioli)": "10,50€",
                "Salsicce (con patatine o fagioli)": "9,00€",
                "Galletto allo spiedo (con patatine o fagioli)": "9,00€",
                "Pizze varie": "5,50€ - 7,50€",
                "Birre (33cl)": "3,50€ - 4,00€",
                "Birra metro (10 birre)": "32,00€ - 36,00€",
                "Bicchiere di vino": "1,50€",
                "Caraffe di vino": "6,00€ - 9,00€",
                "Spritz, Gin Tonic, Caffè": "1,30€ - 3,00€"
            },
            "recensione": "Specialità frittura di pesce. Sagra ben organizzata con qualche alto e basso tra cibo, location e intrattenimento.",
            "voti": {
                "Frittella": 8.5,
                "Intrattenimento": 5.5,
                "Pesca di Beneficenza": 9.0,
                "Rabosello": 0.0,
                "Location": 7.0
            }
        }
    ]
}

st.title("Sagra Advisor 🐷")
st.markdown("Benvenuto su **Sagra Advisor**! Seleziona una data per vedere le sagre disponibili.")

# Selettore di data
data_scelta = st.date_input("Scegli una data", datetime.date.today())
data_str = data_scelta.strftime("%Y-%m-%d")

# Visualizza sagre se presenti
if data_str in sagre:
    st.subheader(f"Sagre il {data_scelta.strftime('%d %B %Y')}")
    for sagra in sagre[data_str]:
        with st.expander(sagra["nome"]):
            st.markdown("### Foto del menu")
            for foto in sagra["menu_foto"]:
                st.image(foto, use_container_width=True)

            st.markdown("### Foto dei piatti")
            for foto in sagra["piatti_foto"]:
                st.image(foto, use_container_width=True)

            st.markdown("### Menu e Prezzi")
            for piatto, prezzo in sagra["menu"].items():
                st.write(f"- **{piatto}**: {prezzo}")

            st.markdown("### Recensione Generale")
            st.info(sagra["recensione"])

            st.markdown("### Voti per Categoria")
            for categoria, voto in sagra["voti"].items():
                st.write(f"- **{categoria}**: {voto}/10")

            # Riepilogo voti con media e grafico
            st.markdown("### Riepilogo voti")
            categorie = list(sagra["voti"].keys())
            punteggi = list(sagra["voti"].values())
            media = sum(punteggi) / len(punteggi)
            st.success(f"**Media dei voti**: {media:.1f}/10")

            # Grafico a barre
            fig, ax = plt.subplots()
            ax.barh(categorie, punteggi, color='skyblue')
            ax.set_xlim(0, 10)
            ax.set_xlabel("Punteggio")
            ax.set_title("Valutazione per categoria")
            st.pyplot(fig)
else:
    st.warning("Nessuna sagra trovata per questa data.")
