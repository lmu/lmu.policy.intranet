# -*- coding: utf-8 -*-

demo_users = {
    'Brady': {
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Stephanie Brady',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/b/brady_stephanie/index.html',
        },
        'roles': ('Member', 'in_members')
    },
    'Simon.Kirner': {
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Simon Kirner',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/k/kirner_simon/index.html',
        },
        'roles': ('Member', 'in_members')
    },
    'Alexander.Loechel': {
        'email': 'Alexander.Loechel@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Alexander Loechel',
            'location': 'Martiusstr. 4; München',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/l/loechel_alexander/index.html',
        },
        'roles': ('Member', 'Manager', 'cms-admins', 'in_sp_supportteam', 'in_members')
    },
    'Katharine.Linges': {
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Katharine Linges',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/l/linges_katharine/index.html',
        },
        'roles': ('Member', 'in_sp_supportteam', 'in_members')
    },
    'Katrin.Groeschel': {
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Katrin Gröschel',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/g/groeschel_katrin/index.html',
        },
        'roles': ('Member', 'in_sp_supportteam', 'in_members')
    }
}


demo_blog_entries = {
    'verloren-und-gewonnen-am-aktionstag-gesundheit': {
        'title': u'Verloren und gewonnen am Aktionstag Gesundheit',
        'description': '',
        'text': u"""<p>Leider hat es für mein Team nicht für einen Sieg im Riesenkicker gereicht – dennoch war aus meiner Sicht der Aktionstag Gesundheit ein voller Erfolg:
        Am Ende waren alle Gewinner.</p>
        <p>Ich muss gestehen, dass ich mich nicht ohne Skepsis zum Aktionstag Gesundheit angemeldet habe.
        Skeptisch insofern, weil als Ziel des Aktionstages die Stärkung der Gemeinschaft unter Kolleginnen und Kolleginnen angegeben war.
        Ein recht hohes Ziel für einen Tag voller auf den ersten Blick skurril anmutender Spiele wie Riesenkicker oder Wischmopphockey.
        Ich habe allerdings unterschätzt, welch positive Wirkung es haben kann, mit Kollegen an eine Stange „gefesselt“ zu sein.
        Vor allem das menschliche Riesenkicker als Highlight des Tages war Anstifter zu guten Gesprächen und vor allem viel gemeinsamen Lachens.
        Am Rande sei erwähnt, dass der Ehrgeiz dann doch den ein oder anderen auf spielerische Weise gepackt hat.
        Tja, dummerweise hat es am Ende für mein Team „Walter Frosch Gedächtnisgruppe“ nicht für den Pokal gereicht – wir mussten uns knapp geschlagen geben, trotz größerer Spielanteile.</p>
        <p>Aber sei es dem Team „Internationale Härte“ gegönnt, den Pokal zu haben.
        Vielleicht gibt es ja irgendwann wieder einen Aktionstag Gesundheit und ein Rückspiel.
        Denn gewonnen oder nicht, ich hatte den Eindruck, dass am Ende jeder jeden ein wenig mehr kannte und schätzte.
        So dass am Ende des Tages alle als Gewinner einer – wie eben anfangs erwähnt – Gemeinschaft waren.</p>
        <p>Ich freue mich auf nächstes Jahr und werde wieder am Start sein.</p>""",
        'path': '/blog-mit',
        'image': 'demo-content/Aktionstag Gesundheit 006.jpg',
        'image_caption': u'Aktionstag Gesundheit - Riesen-Kicker',
        'author': 'Simon.Kirner',
        'modification_date': '2014/10/02 16:09:00.000000 GMT+2'
    },
    'wer-hat-erfahrungen-mit-online-anwendungen-fuer-die-reisekosten-administration': {
        'title': u'Wer hat Erfahrungen mit Online-Anwendungen für die Reisekosten-Administration?',
        'description': '',
        'text': u"""<p>Ich leite ein Projekt zur Optimierung des Geschäftsprozesses von Reisekosten und arbeite derzeit an einem Konzept zur Digitalisierung von deren Beantragung.
        Hat jemand Erfahrungen mit Online-Buchungs-Tools und kann diese einbringen?</p>""",
        'path': '/blog-mit',
        'image': '',
        'image_caption': u'',
        'author': 'Brady',
        'modification_date': '2014/10/02 15:32:00.000000 GMT+2'
    },
    'organisationsentwicklung-an-der-universitaet-lund': {
        'title': u'Organisationsentwicklung an der Universität Lund',
        'description': '',
        'text': u"""<p>Im Rahmen eines Mitarbeiteraustauschs war ich letzte Woche an der LERU-Uni in Lund / Schweden.
        Es ist sehr erhellend, wie dort die Verwaltung aufgebaut ist und wie sie derzeit ihre Administration optimieren.
        Einige Maßnahmen sind ähnlich wie in ZUV 2015…</p>""",
        'path': '/blog-mit',
        'image': 'demo-content/lunds-universitets-huvudbyggnad.jpg',
        'image_caption': u'Universität Lund',
        'author': 'Brady',
        'modification_date': '2014/10/02 13:09:00.000000 GMT+2'
    },
}

demo_polls = {
    'und-sie-bewegt-sich-doch': {
        'poll_type': 'Agree Disagree Poll',
        'path': '/umfragen',
        'title': 'Und sie bewegt sich doch, die ZUV.',
        'description': '',
        'author': 'Katharine.Linges',
        'modification_date': '2014/10/02 12:43:00.000000 GMT+2',
        'state': 'open',
    },
    'wie-gut-hilft-ihnen-unser-service-portal-bei-der-arbeit': {
        'poll_type': 'Star Poll',
        'path': '/umfragen',
        'title': 'Wie gut hilft Ihnen unser Service-Portal bei der Arbeit?',
        'description': 'Seien Sie ehrlich, nur so können wir besser werden.',
        'author': 'Katharine.Linges',
        'modification_date': '2014/10/02 12:43:00.000000 GMT+2',
        'state': 'open',
    }
}

demo_pinnwand_entries = {
    '115qm-wohnung-in-schwabing': {
        'category': 'Biete',
        'title': u'115pm Wohung in Schwabing',
        'text': u'<p>3-Zimmer Wohnung inmitten des lebhaften Kunst- und Pinakothekenviertels zu vermieten...</p>',
        'path': '/pinnwand',
        'image': 'demo-content/wohung-schwabingen.jpg',
        'image_caption': '',
        'author': 'Simon.Kirner',
        'modification_date': '2014/10/02 12:43:00.000000 GMT+2'
    },
    'fahrgemeinschaft-von-altdorf-bei-landshut-in-die-leo3': {
        'category': 'Suche',
        'title': u'Fahrgemeinschaft von Altdorf bei Landshut in die Leo3',
        'text': u'<p>Ich fahre regelmäßig Montag bis Donnerstag morgens nach München und mittags zurück. Wer hat die gleiche Strecke?</p>',
        'path': '/pinnwand',
        'image': '',
        'image_caption': '',
        'author': 'Brady',
        'modification_date': '2014/10/02 13:32:00.000000 GMT+2'
    },
    'tolles-sofa': {
        'category': 'Biete',
        'title': u'Tolles Sofa!',
        'text': u'<p>Das Sofa muss raus. Jetzt für 150€ abzugeben.</p>',
        'path': '/pinnwand',
        'image': 'demo-content/sofa.jpg',
        'image_caption': '',
        'author': 'Simon.Kirner',
        'modification_date': '2014/10/02 14:27:00.000000 GMT+2'
    },
    'damenfahrrad': {
        'category': 'Suche',
        'title': u'Damenfahrrad',
        'text': u'''<p>Liebe Kolleginnen und Kollegen,</p>
        <p>ich bin auf der Suche nach einem gut erhaltenen Damenfahrrad, möglichst 28 Zoll.
        Falls jemand einen Tipp hat oder noch ein gebrauchtes Rad im Keller stehen hat, würde ich mich über eine E-Mail sehr freuen!</p>''',
        'path': '/pinnwand',
        'image': '',
        'image_caption': '',
        'author': 'Katharine.Linges',
        'modification_date': '2014/10/03 14:27:00.000000 GMT+2'
    },
    'rollcontainer-gebraucht-aber-gut-in-schuss': {
        'category': 'Biete',
        'title': u'Rollcontainer - gebraucht, aber gut in Schuss',
        'description': '',
        'text': u"""<p>Verkaufe einen Rollcontainer mit 3 Schubladen, oben hat er eine kleine Macke (siehe Foto).</p>
<p>Maße:<br />Tiefe: 41 cm<br />Höhe:57 cm<br />Breite: 41 cm</p>
<p>5 Euro VB</p>""",
        'path': '/pinnwand',
        'image': 'demo-content/Rollcontainer.jpg',
        'image_caption': u'Rollcontainer',
        'author': 'Katrin.Groeschel',
        'modification_date': '2014/10/02 13:09:00.000000 GMT+2'
    },
}
