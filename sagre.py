import streamlit as st
import datetime

# Inserisci il tuo username GitHub qui
github_base_url = "https://github.com/battistg/sagra_advisor/edit/main"

sagre = {
    "2025-05-16": [
        {
            "nome": "Sagra di San Isidoro di Schiavon (VI)",
            "menu_foto": [github_base_url + "IMG_0273.jpeg"],
            "piatti_foto": [
                github_base_url + "IMG_0266.jpeg",
                github_base_url + "IMG_0267.jpeg",
                github_base_url + "IMG_0268.jpeg"
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
                "Frittella": "8.5/10 - Ottima, poco unta e ben zuccherata. Prezzo 4€ un po’ alto.",
                "Intrattenimento": "5.5/10 - Brucamela ok, autoscontro assente, cover band ok, pista da ballo male.",
                "Pesca di Beneficenza": "9/10 - Ricca di premi seri, molto curata.",
                "Rabosello": "0/10 - Totalmente assente, delusione.",
                "Location": "7/10 - Ordinata ma senza cestini. Cimitero vicino poco coinvolgente."
            }
        }
    ]
}

st.title("Sagra Advisor")
st.markdown("Benvenuto su **SagraAdvisor**! Seleziona una data per vedere le sagre disponibili.")

# Selettore di data
data_scelta = st.date_input("Scegli una data", datetime.date.today())
data_str = data_scelta.strftime("%Y-%m-%d")

# Verifica presenza di sagre in quella data
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
                st.write(f"- **{categoria}**: {voto}")
else:
    st.warning("Nessuna sagra trovata per questa data.")
