# ------------------------------------------------------------------------------
# Version: 20.12.2024
# ------------------------------------------------------------------------------


# Define prompts --------------------------------------------------------------
SYSTEM_PROMPT = """
    Du bist ein erfahrener Fachjournalist.
    Deine Spezialität ist das Schreiben von Fachartikeln auf Basis von Originaldokumenten,
    wie zum Beispiel: Pressemitteilungen, Produktbroschüren, wissenschaftliche Arbeiten,
    Social Media Posts, Blog-Posts, etc.
    Die Ausgabe erfolgt immer in unformatiertem Text und besteht ausschliesslich aus dem Text.

    Wenn der Prompt #ENG enthält, wird die Ausgabe in englischer Sprache erfolgen.
    Wenn der Prompt #FRA enthält, wird die Ausgabe in französischer Sprache erfolgen.
    Wenn der Prompt #DEU enthält, wird die Ausgabe in deutscher Sprache erfolgen.
    """

PROMPTS = {
    "Fachartikel": """
        Schreibe einen Fachartikel, der die beigefügten Dokumente strukturiert zusammenfasst.
        Beginne mit einem inhaltlichen Überblick und fasse die wichtigsten Punkte zusammen.
        """,
    "Blogbeitrag": """
        Schreibe einen Blogbeitrag, der die beigefügten Dokumente zusammenfasst und die wesentlichen Punkte hervorhebt.
        """,
    "Social Media Post": """
        Schreibe einen Social Media Post, der Leser dazu ermutigt, den beigefügten Artikel zu lesen.
        Beschreibe das Thema und die wichtigsten Punkte des Dokuments.
        """,
    "Schlagworte": """
        Generiere mindestens 5 Schlagworte.
        """,
    "Pressemitteilung": """
        Pressemitteilungen sind ein zentrales Instrument der Unternehmenskommunikation, das darauf abzielt,
        Aufmerksamkeit in der Öffentlichkeit zu erzeugen und die Wahrnehmung von Unternehmen,
        Produkten oder Dienstleistungen positiv zu beeinflussen.
        Sie richten sich primär an Journalistinnen und Journalisten, die als Multiplikatoren fungieren
        und die Themen in die redaktionelle Berichterstattung einbringen können.

        Eine Pressemitteilung unterscheidet sich von anderen Textformaten durch ihren sachlich-neutralen Stil
        und die Beantwortung der wichtigsten W-Fragen: Wer, was, wann, wo, wie und warum.
        Sie sollte ein zentrales Thema fokussieren und in einer klaren, lebendigen Sprache verfasst sein,
        ohne Superlative oder Wertungen.

        Der Aufbau einer Pressemitteilung umfasst eine prägnante Headline, die das Interesse weckt,
        einen Teaser, der die wichtigsten Informationen zusammenfasst,
        und weitere Absätze, die zusätzliche Details und Zitate enthalten.
        Am Ende stehen ein Boilerplate mit Unternehmensinformationen und der Pressekontakt.

        Insgesamt sollte eine Pressemitteilung klar, präzise und relevant für die Zielgruppe sein,
        um erfolgreich in der Medienlandschaft wahrgenommen zu werden.

        Schreibe eine Pressemitteilung entsprechend dieser Vorgaben.
        """,
    "Karteikarten": """
        Deine Aufgabe ist es, Karteikarten zu erstellen, die dabei helfen, die wichigsten Informationen
        aus den beigefügten Dokumenten zu lernen und zu behalten.
        Die Karteikarten bestehen jeweils aus einer Frage und einer Antwort.
        Das Ausgabeformat ist wie folgt:
        [
        {Frage: [Frage], Antwort: [Antwort]},
        {Frage: [Frage], Antwort: [Antwort]},
        ...
        ]
        """,
    }

# Def functions --------------------------------------------------------------
def get_system_prompt():
    return SYSTEM_PROMPT

def get_prompt_names():
    return list(PROMPTS.keys())

def get_prompt_by_name(name):
    if name in PROMPTS:
        return PROMPTS[name]
    return None

def get_prompt_by_index(index):
    prompts_list = list(PROMPTS.values())
    return prompts_list[index]