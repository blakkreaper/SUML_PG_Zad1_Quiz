import streamlit as st

# Tytuł aplikacji
st.title('Prosty Quiz')

# Pytania i odpowiedzi
q_and_a = {
    "Stolica Polski to:": ("Warszawa", ["Kraków", "Gdańsk", "Wrocław"]),
    "Największa planeta w Układzie Słonecznym to:": ("Jowisz", ["Mars", "Ziemia", "Saturn"]),
    "Ile nóg ma pająk?": ("8", ["4", "6", "10"]),
    "Stolica Francji to:": ("Paryż", ["Londyn", "Berlin", "Madryt"]),
    "Kto napisał 'Lalkę'?": ("Bolesław Prus", ["Adam Mickiewicz", "Juliusz Słowacki", "Henryk Sienkiewicz"]),
    "Najdłuższa rzeka w Polsce to:": ("Wisła", ["Dunaj", "Odra", "Warta"]),
    "Który pierwiastek chemiczny ma symbol Fe?": ("Żelazo", ["Złoto", "Srebro", "Miedź"]),
    "W którym roku człowiek pierwszy raz postawił nogę na Księżycu?": ("1969", ["1959", "1979", "1989"]),
    "Największy ocean na Ziemi to:": ("Ocean Spokojny", ["Ocean Atlantycki", "Ocean Indyjski", "Ocean Arktyczny"])
}

# Przechowywanie odpowiedzi użytkownika
user_answers = {}
for q, a in q_and_a.items():
    options = [a[0]] + a[1]
    answer = st.radio(q, options, index=None, key=q)  # Ustawienie index na None
    user_answers[q] = answer

# Przycisk sprawdzający odpowiedzi
if st.button('Sprawdź'):
    if None in user_answers.values():
        st.error("Proszę odpowiedzieć na wszystkie pytania.")
    else:
        points = sum(user_answers[q] == q_and_a[q][0] for q in q_and_a)
        total_questions = len(q_and_a)
        score_percentage = (points / total_questions) * 100

        # Wyświetlanie wyniku
        st.write(f"Twój wynik to: {points} punkt(ów) na {total_questions} możliwe, co stanowi {score_percentage:.2f}%.")
