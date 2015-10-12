# -*- coding: utf-8 -*-

required_groups = {
    'ZUV-Intranet-Members': {
        'roles': ['Member'],
        'title': 'ZUV-Intranet-Members (Virtual Group)',
        'description': 'Virtual Group for Users of the ZUV-Intranet comming from Shibboleth via "cn=ZUV-Intranet-Members,ou=..."'
    },
    'ZUV-Intranet-Blog': {
        'roles': ['Member'],
        'title': 'ZUV-Intranet-Members (Virtual Group)',
        'description': 'Virtual Group for Users of the ZUV-Intranet comming from Shibboleth via "cn=ZUV-Intranet-Members,ou=..."'
    },
    'ZUV-Intranet-Pinnwand': {
        'roles': ['Member'],
        'title': 'ZUV-Intranet-Members (Virtual Group)',
        'description': 'Virtual Group for Users of the ZUV-Intranet comming from Shibboleth via "cn=ZUV-Intranet-Members,ou=..."'
    }
}

base_content = {
    'blog-mit': {
        'title': 'Blog mit!',
        'description': 'Mitarbeiten. Mitreden. Mitmachen.',
        'text': """
        <h2>Willkommen zum Mitarbeiter Blog der ZUV!</h2>
        <p>Ziel von Blog MIT, dem Mitarbeiter-Blog im ZUV-Intranet, ist der interne Austausch und die Vernetzung aller Mitarbeiterinnen und Mitarbeiter der ZUV über die Hierarchieebenen hinweg.
        Wir laden Sie herzlich ein, zu aktuellen Themen unserer täglichen Arbeit, zu Projekten, Prozessen, Fragestellungen und Dienstleistungen der ZUV Beiträge zu verfassen und zu kommentieren.
        Alle Beiträge und Kommentare werden mit dem Namen des Verfassers veröffentlicht, um eine faire und respektvolle Kommunikationskultur sicherzustellen. Darüber hinaus haben wir Ihnen im Folgenden einige Regeln und Tipps zusammengestellt, die den Umgang mit dem Mitarbeiter-Blog erleichtern.
        Wir freuen uns über Ihre Beiträge und Kommentare.</p>
        <h3>Tipps und Tricks</h3>
        <ul>
            <li>Wählen Sie einen aussagekräftigen Titel für Ihren Beitrag.
            Gut formulierte Überschriften machen neugierig und geben einen klaren Hinweis zum Inhalt des Beitrags.</li>
            <li>Falls Sie Ihrem Beitrag ein Bild beifügen möchten, verwenden Sie stets hochwertiges Bildmaterial und achten Sie auf einen Bezug zum Beitrag.</li>
            <li>Ihr Blog-Beitrag wird von vielen Kolleginnen und Kollegen gelesen. Achten Sie deshalb auf Rechtschreibung und drücken Sie erst auf „Senden“ wenn Sie sich sicher sind, dass Sie Ihren Beitrag so veröffentlichen möchten.</li>
        </ul>
        <h3>Blog-Verhaltensregeln</h3>
        <ul>
            <li>Im Mitarbeiter-Blog behandeln wir andere Nutzer so, wie wir selbst gerne behandelt werden möchten.</li>
            <li>Wir achten beim Zitieren auf das geistige Eigentum anderer und geben die entsprechende Quelle an.
            Wenn wir uns nicht sicher sind, ob der Urheber mit unserem Beitrag einverstanden ist, halten wir Rücksprache mit diesem Kollegen oder dieser Kollegin.</li>
            <li>Wir versuchen, Mutmaßungen zu vermeiden oder kennzeichnen diese klar im Beitrag.</li>
            <li>Ironie und Wortwitz funktionieren im Internet oftmals nicht so gut wie von Angesicht zu Angesicht.
            Wir achten darauf, dass unser Beitrag nicht zweideutig ist und somit falsch verstanden werden könnte.</li>
            <li>Beim Kommentieren eines Blog-Beitrages beziehen wir uns immer auf dessen Inhalt und diskutieren stets themennah.</li>
        </ul>
        <h3>Löschen von Beiträgen</h3>
        <p>Sollte es wider Erwarten zu einer Abweichung von diesen Blog-Regeln kommen, behalten wir uns vor, die entsprechenden Beiträge oder Kommentare zu löschen. Dies geschieht ohne Ankündigung, Sie werden jedoch über die Löschung Ihres Beitrags informiert.</p>
        <p>Darüber hinaus sehen wir uns dazu verpflichtet, alle Beiträge und Kommentare zu löschen, die:</p>
        <ul>
            <li>in irgendeiner Form beleidigend oder entwürdigend sind.</li>
            <li>den Blog als Werbefläche missbrauchen (gewerblich oder privat).</li>
            <li>die Rechte Dritter verletzen (insbesondere Urheberrecht).</li>
            <li>gewaltverherrlichend, pornographisch oder obszön sind.</li>
            <li>nicht in deutscher oder englischer Sprache verfasst wurden.</li>
            <li>maschinell eingetragen werden.</li>
            <li>Links zu illegalen Downloads enthalten.</li>
        </ul>
        <p>Beiträge, die Kolleginnen oder Kollegen aufgrund ihres Geschlechts, ihres Alters, ihrer Sprache, ihrer Abstammung, ihrer Religion, ihrer Weltanschauung, einer Behinderung oder ihrer sexuellen Orientierung diskriminieren oder diffamieren, werden gelöscht.
        Denken Sie daran, dass Sie es mit Menschen und nicht mit virtuellen Persönlichkeiten zu tun haben.</p>
        <p>Sollten Sie Fragen zum Mitarbeiter-Blog oder den Blog-Regeln haben, können Sie sich jederzeit an uns unter <a href="mailto:zuv-intranet@lmu.de">zuv-intranet@lmu.de</a> wenden.</p>
        <p><strong>Viel Spaß beim Bloggen!<br /> Ihre Intranet-Redaktion</strong></p>
        """,
        'type': 'Blog Folder',
        'path': '/',
        'roles': {
            'ZUV-Intranet-Blog': ['Member', 'Contributor'],
            'in_sp_supportteam': ['Editor', 'Reviewer']
        }
    },
    'umfragen': {
        'title': 'Umfragen',
        'description': '',
        'text': """

""",
        'type': 'Poll Folder',
        'path': '/',
        'roles': {
            'ZUV-Intranet-Member': ['Member'],
            'in_sp_supportteam': ['Contributer', 'Editor', 'Reviewer']
        }
    },
    'pinnwand': {
        'title': 'Die ZUV Pinnwand',
        'description': 'Tauschen. Helfen. Kaufen.',
        'text': """
        <h2>Tipps und Tricks</h2>
        <ol>
        <li>Geben Sie Ihrer Anzeige eine aussagekräftige, konkrete Überschrift, damit diese besser gefunden wird und der Inhalt sofort erkennbar ist. </li>
        <li>Fotos erhöhen den Erfolg Ihrer Anzeige. Sie können bis zu 8 Fotos einbinden, stellen Sie dort die wichtigsten Merkmale dar. Tipps & Tricks, wie man das Produkt „in Szene“ setzen kann</li>
         <ul>
          <li>Sorgen Sie durch gute Lichtverhältnisse für gut erkennbare Fotos.</li>
          <li>Fotografieren Sie das Produkt ggf. von mehreren Seiten und ggf. auch Details des Produktes.</li>
          <li>Zeigen Sie der Fairness halber auch die Gebrauchsspuren oder eventuelle Schäden am Produkt.</li>
         </ul>
        <li> Beschreiben Sie, was Sie anbieten oder suchen, konkret, damit der Interessent oder die Interessentin sich ein genaues Bild darüber machen kann, was ihn oder sie erwartet. </li>
        <li>Formatieren Sie Ihr Angebot und überprüfen Sie den Text auf Rechtschreibfehler. Eine übersichtliche und fehlerlose Anzeige wird gerne gelesen. </li>
            </ol>
            <h2>Nutzungsbedingungen</h2>
            <ol>
             <li>Allgemeine Regeln</li>
             <ol>
              <li>Diese Nutzungsbedingungen regeln die Nutzung der ZUV-Pinnwand im ZUV-Intranet unter www.intranet.verwaltung.uni-muenchen.de. Betreiber der ZUV-Pinnwand ist die Zentrale Universitätsverwaltung der LMU München (Betreiberin). Die Betreiberin behält sich vor, diese Nutzungsbedingungen jederzeit anzupassen. Maßgebend sind die jeweils zum Zeitpunkt der Nutzung geltenden Nutzungsbedingungen.
              <li>Die ZUV-Pinnwand ist ein freiwilliges kostenloses digitales Angebot der Betreiberin und dient dem einfachen und schnellen Austausch und der Mitteilung von privaten Informationen, insbesondere von Gesuchen und Angeboten. Die Beiträge müssen den Kategorien „Suche“ oder „Biete“ zugeteilt werden.</li>
              <li>Die ZUV-Pinnwand darf nur von Mitarbeiterinnen und Mitarbeitern (Nutzern) genutzt werden, die Zugriff auf das ZUV-Intranet haben. Andere Personen sind von der Nutzung ausgeschlossen. </li>
              <li>Beiträge können von den Nutzern selbstständig veröffentlicht werden. Veröffentlichte Beiträge erscheinen immer mit dem Vor- und Nachnamen der Verfasserin bzw. des Verfassers. </li>
              <li>Die ZUV-Pinnwand unterliegt als Teil des ZUV-Intranets den Benutzungsrichtlinien für Informationsverarbeitungssysteme an der LMU.
              Es ist insofern untersagt, Inhalte zu veröffentlichen, die gegen bestehende Gesetze (z.B. Strafgesetz, Gesetz zum Schutz der Jugend, Datenschutzgesetz) verstoßen oder Rechte Dritter (z.B. Namensrechte, Persönlichkeitsrechte, Urheberrechte) verletzen. Unzulässig sind insbesondere Nutzungen, die kriminelle, terroristische, rassistische, diskriminierende, verleumderische, pornographische Ziele oder eine Propaganda für verfassungswidrige Organisationen beinhalten oder auf andere Weise geltendes Recht verletzen oder gegen die guten Sitten verstoßen.</li>
              <li>Die ZUV-Pinnwand darf nicht für kommerzielle Werbung, Marketing und Spam oder in übermäßiger Art und Weise verwendet werden. Auf externe Internetseiten darf nicht verlinkt werden. </li>
              <li>Die Nutzung der ZUV-Pinnwand für gewerbliche Zwecke oder eine Nutzung in gewerbeähnlichem Umfang ist ausgeschlossen. Das gilt auch für Inserate im Namen Dritter.</li>
              <li>Bei den Einträgen auf der ZUV-Pinnwand soll auf die Verwendung von Abkürzungen verzichtet werden.</li>
             </ol>
             <li>Verantwortlichkeit und Haftungsausschluss</li>
              <ol>
              <li>Die Betreiberin bemüht sich im Rahmen der gegebenen Möglichkeiten um Sicherstellung der Erreichbarkeit und Funktionstüchtigkeit der ZUV-Pinnwand über das ZUV-Intranet, ist aber nicht verpflichtet, die Erreichbarkeit und Funktionstüchtigkeit der ZUV-Pinnwand durchgängig und zu jeder Zeit zu gewährleisten. Die Betreiberin stellt die ZUV-Pinnwand lediglich mit der Möglichkeit der Kontaktaufnahme zur Verfügung, übernimmt aber keine Verantwortung für einen reibungslosen und fehlerfreien Ablauf.</li>
              <li>Die Betreiberin haftet nicht für eine fehlerfreie Funktion oder Anzeige. Die Betreiberin haftet auch nicht für den Inhalt, die Richtigkeit, Aktualität, Qualität, Vollständigkeit, Sicherheit und Rechtskonformität der Inserate und Kommunikation. Zu einer detaillierten Prüfung der Inhalte ist die Betreiberin weder verpflichtet noch in der Lage, die Pinnwand wird aber regelmäßig einer Qualitätssicherung unterzogen.</li>
              <li>Für den Inhalt einer veröffentlichten Nachricht ist die Verfasserin bzw. der Verfasser der Inhalte eigenverantwortlich und haftet nach den allgemeinen Regeln. Die Betreiberin ist für Inhalte, die von Nutzern an der Pinnwand angebracht wurden, nicht verantwortlich. Die Betreiberin distanziert sich hiermit ausdrücklich von allen Kommunikationsinhalten der Nutzer. </li>
              <li>Die Nutzer sind verpflichtet, der Betreiberin den aus der missbräuchlichen Nutzung entstandenen bzw. entstehenden Schaden zu ersetzen. Die jeweilige Nutzerin bzw. der jeweilige Nutzer stellt die Betreiberin von allen Verpflichtungen und Ansprüchen Dritter frei, die daraus entstehen, dass die Betreiberin von Dritten in Anspruch genommen wird, weil die Nutzerin bzw. der Nutzer deren Rechte schuldhaft verletzt hat. </li>
              <li>Die Nutzer gewähren der Betreiberin das unentgeltliche, zeitlich und räumlich unbegrenzte Recht, ihre Kommentare oder Einträge ganz oder teilweise in der ZUV-Pinnwand zu verwenden.</li>
             </ol>
             <li>Datenschutz</li>
             <ol>
              <li>Die Betreiberin setzt zum Betrieb der ZUV-Pinnwand Session Cookies ein. Die Session Cookies dienen der Identifikation der Nutzer während der Nutzung der ZUV-Pinnwand. Die Session Cookies werden nach Beendigung der jeweiligen Sitzung gelöscht.
              <li>Die ZUV-Pinnwand wird im Einklang mit den geltenden Datenschutzregelungen betrieben. Die personenbezogenen Daten der Nutzer werden entsprechend den geltenden Datenschutzbestimmungen gespeichert und verarbeitet. Es werden nur die Daten erhoben, die für den Betrieb der ZUV-Pinnwand erforderlich sind.
              Im Rahmen des Betriebs der ZUV-Pinnwand werden von der Betreiberin auch solche Informationen gespeichert, die die Nutzer selbst eingeben oder in sonstiger Weise übermitteln.</li>
              <li>Das Löschen von eigenen Einträgen, z.B. aufgrund von Tippfehlern oder inhaltlichen Fehlern, ist jederzeit möglich. Die Nutzer müssen zudem vor der Veröffentlichung eines Beitrags ein Datum angeben, an dem ihr Pinnwand-Eintrag automatisiert gelöscht wird. Das Datum kann ab dem Veröffentlichungsdatum maximal drei Monate in der Zukunft liegen. Ziffer 5.1 Satz 1 bleibt unberührt.</li>
             </ol>
             <li>Urheberrechtsschutz</li>
             <li>
              Die Nutzer sind verpflichtet, Nutzungs-, Urheber-, gewerbliche Schutzrechte und das Gesetz gegen den unlauteren Wettbewerb (UWG) zu beachten und hinsichtlich ggf. von ihnen in das Intranet eingestellter Inhalte deutlich und in angemessener Art und Weise auf die entsprechenden Nutzungs-, Urheber- und gewerblichen Schutzrechte hinzuweisen. Auf jeden Fall ist die Quelle zu nennen.
             </li>
             <li>Verstoß gegen Nutzungsbedingungen und geltendes Recht</li>
             <li>
              Bei Verstößen gegen die Nutzungsbedingungen oder geltendes Recht werden die entsprechenden Beiträge des Nutzers von der Betreiberin unverzüglich gelöscht.
              Darüber hinaus sind disziplinarrechtliche, arbeitsrechtliche, zivilrechtliche und strafrechtliche Sanktionen sowie der temporäre oder permanente Ausschluss vom Zugang zur ZUV-Pinnwand bzw. zum ZUV-Intranet möglich.
             </li>
            </ol>
        """,
        'type': 'Pinnwand Folder',
        'path': '/',
        'roles': {
            'ZUV-Intranet-Pinnwand': ['Member', 'Contributor'],
            'in_sp_supportteam': ['Editor', 'Reviewer']
        }
    },
}
