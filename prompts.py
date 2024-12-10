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