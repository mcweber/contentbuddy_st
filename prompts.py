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

FACHARTIKEL = """
Schreibe einen Fachartikel, der die beigefügten Dokumente strukturiert zusammenfasst.
Beginne mit einem inhaltlichen Überblick und fasse die wichtigsten Punkte zusammen.
"""

BLOGBEITRAG = """
Schreibe einen Blogbeitrag, der die beigefügten Dokumente zusammenfasst und die wesentlichen Punkte hervorhebt.
"""

SOCIAL_MEDIA_POST = """
Schreibe einen Social Media Post, der Leser dazu ermutigt, den beigefügten Artikel zu lesen.
Beschreibe das Thema und die wichtigsten Punkte des Dokuments.
"""

SCHLAGWORTE = """
Generiere mindestens 5 Schlagworte.
"""

PRESSEMITTEILUNG = """
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
"""
