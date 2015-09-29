# -*- coding: utf-8 -*-

demo_users = {
    '72C918A84D785B9F@lmu.de': {  # Alexander Loechel
        'email': 'Alexander.Loechel@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Alexander Loechel',
            'location': 'Martiusstr. 4; München',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/l/loechel_alexander/index.html',
        },
        'roles': ('Member', 'Manager', 'cms-admins', 'in_sp_supportteam', 'in_members')
    },
    '5B4187806EA6E3B0@lmu.de': {  # Katharine Linges
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Katharine Linges',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/l/linges_katharine/index.html',
        },
        'roles': ('Member', 'in_sp_supportteam', 'in_members')
    },
    '5B9282DB46605F33@lmu.de': {  # Katrin Gröschel
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Katrin Gröschel',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/g/groeschel_katrin/index.html',
        },
        'roles': ('Member', 'in_sp_supportteam', 'in_members')
    },
    '3ABBA66EEABFBA4A@lmu.de': {  # Christoph Zehetleitner
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Christoph Zehetleitner',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/z/zehetleitner_christoph/index.html',
        },
        'roles': ('Member', 'in_sp_supportteam', 'in_members')
    },
    'D3A7AFBDCBCDFAEF@lmu.de': {  # Stephanie Brady
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Stephanie Brady',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/b/brady_stephanie/index.html',
        },
        'roles': ('Member', 'in_members')
    },
    '1AFCC515C117A98D@lmu.de': {  # Simon.Kirner
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Simon Kirner',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/k/kirner_simon/index.html',
        },
        'roles': ('Member', 'in_members')
    },
    '3624AAC8BBF0A28E@lmu.de': {  # Seyhan Karabulut
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Seyhan Karabulut',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/k/karabulut_seyhan/index.html',
        },
        'roles': ('Member', 'in_members')
    },
    'AEA7ED2EEFDD4E7A@lmu.de': {  # Elmar Thalhammer
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Elmar Thalhammer',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/t/thalhammer_elmar/index.html',
        },
        'roles': ('Member', 'in_members')
    },
    'D1D7CEAFBBABCDAC@lmu.de': {  # Jan Ingenhaag
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Jan Ingenhaag',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/i/ingenhaag_jan/index.html',
        },
        'roles': ('Member', 'in_members')
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
        'author': '1AFCC515C117A98D@lmu.de',  # 'Simon.Kirner',
        'date': '2014/10/02 16:09:00.000000 GMT+2'
    },
    'wer-hat-erfahrungen-mit-online-anwendungen-fuer-die-reisekosten-administration': {
        'title': u'Wer hat Erfahrungen mit Online-Anwendungen für die Reisekosten-Administration?',
        'description': '',
        'text': u"""<p>Ich leite ein Projekt zur Optimierung des Geschäftsprozesses von Reisekosten und arbeite derzeit an einem Konzept zur Digitalisierung von deren Beantragung.
        Hat jemand Erfahrungen mit Online-Buchungs-Tools und kann diese einbringen?</p>""",
        'path': '/blog-mit',
        'author': 'D3A7AFBDCBCDFAEF@lmu.de',  # 'Brady',
        'date': '2014/10/02 15:32:00.000000 GMT+2'
    },
    'organisationsentwicklung-an-der-universitaet-lund': {
        'title': u'Organisationsentwicklung an der Universität Lund',
        'description': '',
        'text': u"""<p>Im Rahmen eines Mitarbeiteraustauschs war ich letzte Woche an der LERU-Uni in Lund / Schweden.
        Es ist sehr erhellend, wie dort die Verwaltung aufgebaut ist und wie sie derzeit ihre Administration optimieren.
        Einige Maßnahmen sind ähnlich wie in ZUV 2015…</p>""",
        'path': '/blog-mit',
        'author': 'D3A7AFBDCBCDFAEF@lmu.de',  # 'Brady',
        'date': '2014/10/02 13:09:00.000000 GMT+2'
    },
    'mitreden-bei-blog-mit': {
        'title': u'Mitreden bei "Blog Mit!',
        'description': '',
        'text': u"""<p>Der ZUV-Mitarbeiterblog „Blog Mit!“ bietet Raum für Ihre Anliegen:
        Beschäftigt Sie ein Thema aus Ihrer täglichen Arbeit, das Sie mit einem größeren Kollegenkreis diskutieren wollen?
        Möchten Sie Ihr Erfahrungswissen mit anderen teilen oder bringt Sie das Know-how von anderen Kolleginnen und Kollegen bei Ihrer Fragestellung weiter?
        Wollen Sie den anderen das schönste Foto vom letzten Betriebsausflug oder vom Firmenlauf zeigen?</p>
        <p>Dann laden wir Sie herzlich ein, in „Blog Mit!“ Beiträge zu verfassen oder zu kommentieren – selbstverständlich während Ihrer Arbeitszeit.
        Die Themen unserer täglichen Arbeit  sollen dabei im Mittelpunkt stehen, unsere Projekte, Prozesse, Fragestellungen und Dienstleistungen, aber auch das, was das tägliche Zusammenarbeiten noch ausmacht.</p>
        <p>„Blog Mit!“ soll zum offenen und transparenten Austausch von Informationen und Meinungen innerhalb der ZUV beitragen und die Kolleginnen und Kollegen über die Hierarchieebenen hinweg besser vernetzen.
        Alle Beiträge können deshalb von den Mitarbeitern der ZUV kommentiert werden.</p>
        <p>Um eine faire und respektvolle Kommunikationskultur sicherzustellen, erscheinen alle Beiträge und Kommentare mit dem Namen des Verfassers.
        Darüber hinaus haben wir  einige Regeln und Tipps zusammengestellt, die den Umgang mit dem Mitarbeiter-Blog erleichtern. </p>
        <p>Wir freuen uns auf Ihre Beiträge und Kommentare!</p>""",
        'path': '/blog-mit',
        'author': '72C918A84D785B9F@lmu.de',  # 'Linges',
        'date': '2014/10/02 13:09:00.000000 GMT+2'
    },
    'mitarbeiterfotos-im-zuv-intranet': {
        'title': u'Mitarbeiterfotos im ZUV-Intranet',
        'description': '',
        'text': u"""<p>Da das ZUV-Intranet nicht nur als reine Informationsplattform für ZUV-Mitarbeiter, sondern auch zur Vernetzung untereinander gedacht ist, halte ich es für sehr sinnvoll, wenn alle Mitarbeiter auf ihrer Personenprofilseite ein Foto von sich platzieren.
        Ich gebe zu, dass das Thema "Gesichter merken und wieder erkennen" nicht zu meinen herausragendsten Fähigkeiten zählt.
        Es passiert mir immer wieder, dass ich eine Kollegin oder einen Kollegen auf dem Gang begegne und nicht auf Anhieb weiss um wen es sich dabei handelt.
        Entsprechend aufbereitete Personenprofilseiten im ZUV-Intranet würden mir enorm helfen.
        Wenn man dann noch neben einem freundlichen "Guten Tag Herr Müller" im richtigen Moment ein zusätzliches "Ach übrigens, alles Gute zum Geburtstag" anbringen kann, dann steht einer engeren Vernetzung der einzelnen ZUV-Mitarbeiter nichts mehr im Weg.</p>""",
        'path': '/blog-mit',
        'author': '3ABBA66EEABFBA4A@lmu.de',  # 'Christoph Zehetleitner',
        'date': '2015/19/16 16:10:00.000000 GMT+2'
    },
    'erholung-garantiert': {
        'title': u'Erholung garantiert',
        'description': '',
        'text': u"""<p>Der Alte Südliche Friedhof lädt zu jeder Jahreszeit zu einem Spaziergang in der Mittagspause ein (Thalkirchner Str. 17).</p>""",
        'path': '/blog-mit',
        'author': '3624AAC8BBF0A28E@lmu.de',  # 'Seyhan Karabulut'
        'date': '2015/09/15 16:03:00.000000 GMT+2'
    },
    'wo-einem-die-lmu-ueberall-begegnet': {
        'title': u'Wo einem die LMU überall begegnet ...',
        'description': '',
        'text': u"""<p>Am 5. Juni war es wieder soweit:
        Der Stichtag für die Hörsaalanträge für das Wintersemester 2015/16 stand auf dem Programm; alle bis zu diesem Tag eingegangen Hörsaalanträge sind als ein Block an die Kolleginnen und Kollegen von der Zentralen Hörsaalverwaltung übermittelt worden und werden gleichrangig behandelt.
        Die Anzahl der Anträge steigt dabei kontinuierlich - diesmal waren es 8.147 Raumanträge, die für zentral verwaltete Hörsäle gestellt wurden.
        Wenn man sich diese beeindruckende Zahl einmal vor Augen führt, ist es erstaunlich, dass die Bearbeitung dieses Berges von Anträgen gerade einmal sechs bis acht Wochen dauern wird.</p>
         <p>In diesem Zusammenhang bin ich immer wieder erstaunt, über wie viele Gebäude und vor allem Räume die LMU verfügt; fast im ganzen Stadtgebiet und auch darüber hinaus stößt man auf sie.
         Als ich letztes Jahr auf den Wendelstein gestiegen bin, kam ich kurz vor dem Gipfel an einem LMU-Schild vorbei.
         Überrascht war ich ob des weithin sichtbaren Observatoriums zwar nicht, aber schmunzeln musste ich trotzdem kurz: Selbst auf über 1.800 Metern sagt die LMU noch kurz "Hallo"...</p>
         <p>Bei LSF-Schulungen (in denen es i. d. R. auch um Raumbuchungen geht) komme ich auch gerne an den Arbeitsplatz unserer Kunden, so dass ich schon zu "Außenstellen" wie z. B. dem Biozentrum in Martinsried reisen durfte.
         Auch wenn man normalerweise überall gut mit den öffentlichen Verkehrsmitteln hinkommt, habe ich diesen Außentermin zum Anlass genommen, um die Kooperation mit DriveNow zu testen (auch weil der Campus in Martinsried kürzlich zum Geschäftsgebiet hinzugefügt worden war).
         Um es kurz zu machen: Es war erfreulich unkompliziert, das Auto anzumieten; und Spaß hat die Fahrt bei schönem Wetter in einem schönen Mini Cabrio darüber hinaus auch noch gemacht.
         Ich könnte mir vorstellen, dass dieses Angebot auch für andere Kolleginnen und Kollegen interessant ist, die es auch mal in die "Randgebiete" der LMU verschlägt.</p>""",
        'path': '/blog-mit',
        'image': '',
        'image_caption': u'',
        'author': 'AEA7ED2EEFDD4E7A@lmu.de',  # 'Elmar Thalhammer'
        'date': '2015/09/15 07:37:00.000000 GMT+2'
    },
    'b2run-morgen-gehts-los': {
        'title': u"B2Run - Morgen geht's los",
        'description': '',
        'text': u"""<p>Morgen geht's los- die LMU läuft wieder beim B2Run! Das T-Shirt: Ich würde mal sagen: GRÜN! Wer ist noch dabei?</p>""",
        'path': '/blog-mit',
        'author': '5B9282DB46605F33@lmu.de',  # "Katrin Gröschel'
        'date': '2015/09/10 13:29:00.000000 GMT+2'
    },
}

empty_blog_entrys = {
    '': {
        'title': u'',
        'description': '',
        'text': u"""""",
        'path': '/blog-mit',
        'image': '',
        'image_caption': u'',
        'author': '',
        'date': '2014/10/02 13:09:00.000000 GMT+2'
    },
}

demo_polls = {
    'und-sie-bewegt-sich-doch': {
        'poll_type': 'Agree Disagree Poll',
        'path': '/umfragen',
        'title': 'Und sie bewegt sich doch, die ZUV.',
        'description': '',
        'author': '5B4187806EA6E3B0@lmu.de',  # 'Katharine.Linges',
        'date': '2014/10/02 12:43:00.000000 GMT+2',
        'state': 'open',
    },
    'wie-gut-hilft-ihnen-unser-service-portal-bei-der-arbeit': {
        'poll_type': 'Star Poll',
        'path': '/umfragen',
        'title': 'Wie gut hilft Ihnen unser Service-Portal bei der Arbeit?',
        'description': 'Seien Sie ehrlich, nur so können wir besser werden.',
        'author': '5B4187806EA6E3B0@lmu.de',  # 'Katharine.Linges',
        'date': '2014/10/02 12:43:00.000000 GMT+2',
        'state': 'open',
    }
}

demo_pinnwand_entries = {
    '115qm-wohnung-in-schwabing': {
        'category': 'Biete',
        'title': u'115pm Wohung in Schwabing',
        'text': u'<p>3-Zimmer Wohnung inmitten des lebhaften Kunst- und Pinakothekenviertels zu vermieten...</p>',
        'path': '/pinnwand',
        'author': '1AFCC515C117A98D@lmu.de',  # 'Simon.Kirner',
        'date': '2014/10/02 12:43:00.000000 GMT+2'
    },
    'fahrgemeinschaft-von-altdorf-bei-landshut-in-die-leo3': {
        'category': 'Suche',
        'title': u'Fahrgemeinschaft von Altdorf bei Landshut in die Leo3',
        'text': u'<p>Ich fahre regelmäßig Montag bis Donnerstag morgens nach München und mittags zurück. Wer hat die gleiche Strecke?</p>',
        'path': '/pinnwand',
        'author': 'D3A7AFBDCBCDFAEF@lmu.de',  # 'Brady',
        'date': '2014/10/02 13:32:00.000000 GMT+2'
    },
    'tolles-sofa': {
        'category': 'Biete',
        'title': u'Tolles Sofa!',
        'text': u'<p>Das Sofa muss raus. Jetzt für 150€ abzugeben.</p>',
        'path': '/pinnwand',
        'author': '1AFCC515C117A98D@lmu.de',  # 'Simon.Kirner',
        'date': '2014/10/02 14:27:00.000000 GMT+2'
    },
    'damenfahrrad': {
        'category': 'Suche',
        'title': u'Damenfahrrad',
        'text': u'''<p>Liebe Kolleginnen und Kollegen,</p>
        <p>ich bin auf der Suche nach einem gut erhaltenen Damenfahrrad, möglichst 28 Zoll.
        Falls jemand einen Tipp hat oder noch ein gebrauchtes Rad im Keller stehen hat, würde ich mich über eine E-Mail sehr freuen!</p>''',
        'path': '/pinnwand',
        'author': '5B4187806EA6E3B0@lmu.de',  # 'Katharine.Linges',
        'date': '2014/10/03 14:27:00.000000 GMT+2'
    },
    'rollcontainer-gebraucht-aber-gut-in-schuss': {
        'category': 'Biete',
        'title': u'Rollcontainer - gebraucht, aber gut in Schuss',
        'description': '',
        'text': u"""<p>Verkaufe einen Rollcontainer mit 3 Schubladen, oben hat er eine kleine Macke (siehe Foto).</p>
        <p>Maße:<br />Tiefe: 41 cm<br />Höhe:57 cm<br />Breite: 41 cm</p>
        <p>5 Euro VB</p>""",
        'path': '/pinnwand',
        'author': '72C918A84D785B9F@lmu.de',  # 'Katrin.Groeschel',
        'date': '2014/10/02 13:09:00.000000 GMT+2'
    },
}

demo_files_images = {
    # Blog Files and Images
    'wald.jpg': {
        'title': u'Der alte Südfriedhof',
        'description': u'Der alte Südfriedhof',
        'src': 'demo-content/blog/erholung-garantiert/wald.jpg',
        'target': '/blog-mit/erholung-garantiert',
        'type': 'Image',
        'author': '3624AAC8BBF0A28E@lmu.de',  # 'Seyhan Karabulut'
    },
    'b2run.jpg': {
        'title': u'B2Run Laufschirt',
        'description': u'Das B2Run Laufshirt 2015',
        'src': 'demo-content/blog/b2run/laufshirt.jpg',
        'target': '/blog-mit/b2run-morgen-gehts-los',
        'type': 'Image',
        'author': '72C918A84D785B9F@lmu.de',  # 'Katrin.Groeschel',
    },
    'uni-lund.jpg': {
        'title': u'Universität Lund',
        'description': u'Universität Lund',
        'src': 'demo-content/blog/organisationsentwicklung-an-der-universitaet-lund/lunds-universitets-huvudbyggnad.jpg',
        'target': '/blog-mit/organisationsentwicklung-an-der-universitaet-lund',
        'type': 'Image',
        'author': 'D3A7AFBDCBCDFAEF@lmu.de',  # 'Brady',
    },
    'berg.jpg': {
        'title': u'Wo einem die LMU überall begegnet',
        'description': u'Wo einem die LMU überall begegnet',
        'src': 'demo-content/blog/wo-einem-die-lmu-ueberall-begegnet/berg.jpg',
        'target': '/blog-mit/wo-einem-die-lmu-ueberall-begegnet',
        'type': 'Image',
        'author': 'AEA7ED2EEFDD4E7A@lmu.de',  # 'Elmar Thalhammer'
    },
    'wanderung.jpg': {
        'title': u'Wo einem die LMU überall begegnet',
        'description': u'Wo einem die LMU überall begegnet',
        'src': 'demo-content/blog/wo-einem-die-lmu-ueberall-begegnet/wanderung.jpg',
        'target': '/blog-mit/wo-einem-die-lmu-ueberall-begegnet',
        'type': 'Image',
        'author': 'AEA7ED2EEFDD4E7A@lmu.de',  # 'Elmar Thalhammer'
    },
    'gipfel.jpg': {
        'title': u'Wo einem die LMU überall begegnet',
        'description': u'Wo einem die LMU überall begegnet',
        'src': 'demo-content/blog/wo-einem-die-lmu-ueberall-begegnet/gipfel.jpg',
        'target': '/blog-mit/wo-einem-die-lmu-ueberall-begegnet',
        'type': 'Image',
        'author': 'AEA7ED2EEFDD4E7A@lmu.de',  # 'Elmar Thalhammer'
    },
    'aktionstag-gesundheit.jpg': {
        'title': u'Verloren und gewonnen am Aktionstag Gesundheit',
        'description': u'Verloren und gewonnen am Aktionstag Gesundheit',
        'src': 'demo-content/blog/verloren-und-gewonnen/aktionstag-gesundheit.jpg',
        'target': 'blog-mit/verloren-und-gewonnen-am-aktionstag-gesundheit',
        'type': 'Image',
        'author': 'D1D7CEAFBBABCDAC@lmu.de',  # Jan Ingenhaag
    },
    # Pinnwand Files and Images
    'rollcontainer.jpg': {
        'title': u'Rollcontainer',
        'description': u'Rollcontainer',
        'src': 'demo-content/pinnwand/rollcontainer-gebraucht-aber-gut-in-schuss/rollcontainer.jpg',
        'target': '/pinnwand/rollcontainer-gebraucht-aber-gut-in-schuss',
        'type': 'Image',
        'author': '72C918A84D785B9F@lmu.de',  # 'Katrin.Groeschel',
    },
    'sofa.jpg': {
        'title': u'Sofa',
        'description': u'Tolles Sofa',
        'src': 'demo-content/pinnwand/tolles-sofa/sofa.jpg',
        'target': '/pinnwand/tolles-sofa/rollcontainer-gebraucht-aber-gut-in-schuss',
        'type': 'Image',
        'author': '72C918A84D785B9F@lmu.de',  # 'Katrin.Groeschel',
    },
}
