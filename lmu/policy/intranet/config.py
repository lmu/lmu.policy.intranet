# -*- coding: utf-8 -*-

required_groups = {
    'cms-admins': {
        'roles': ['Manager'],
        'title': 'CMS Admins (Virtual Group)',
        'description': 'Virtual Group for Administrators derifed from Shibboleth via "cn=cms-admin-insp,ou=..."'
    },
    'in_sp_supportteam': {
        'roles': ['Contributor', 'Editor', 'Reader', 'Reviewer'],
        'title': 'Intranet Supportteam (Virtual Group)',
        'description': 'Virtual Group for the Intranet-Supportteam derifed from Shibboleth via "cn=in_sp_supportteam,ou=..."'
    },
    'in_members': {
        'roles': ['Member'],
        'title': 'ZUV-Intranet Users (Virtual Group)',
        'description': 'Virtual Group for Users of the ZUV-Intranet derifed from Shibboleth via "cn=ZUV-Mitarbeiter,ou=..."'
    }
}

base_content = {
    'blog-mit': {
        'title': 'Blog mit!',
        'description': 'Mitarbeiten, Mitreden, Mitmachen.',
        'text': """
        <h2>Willkommen zum Mitarbeiter Blog der ZUV!</h2>
        <p>Ziel von Blog MIT, dem Mitarbeiter-Blog im ZUV-Intranet, ist der interne Austausch und die Vernetzung aller Mitarbeiterinnen und Mitarbeiter der ZUV über die Hierarchieebenen hinweg.
        Wir laden Sie herzlich ein, zu aktuellen Themen unserer täglichen Arbeit, zu Projekten, Prozessen, Fragestellungen und Dienstleistungen der ZUV Beiträge zu verfassen und zu kommentieren.
        Alle Beiträge und Kommentare werden mit dem Namen des Verfassers veröffentlicht, um eine faire und respektvolle Kommunikationskultur sicherzustellen.
        Darüber hinaus haben wir Ihnen im Folgenden einige Regeln und Tipps zusammengestellt, die den Umgang mit dem Mitarbeiter-Blog erleichtern. Wir freuen uns über Ihre Beiträge und Kommentare.</p>
        <h3>Tipps und Tricks</h3>
        <ul>
            <li>Wählen Sie einen aussagekräftigen Titel für Ihren Beitrag. Gut formulierte Überschriften machen neugierig und geben einen klaren Hinweis zum Inhalt des Beitrags.</li>
            <li>Falls Sie Ihrem Beitrag ein Bild beifügen möchten, verwenden Sie stets hochwertiges Bildmaterial und achten Sie auf einen Bezug zum Beitrag.</li>
            <li>Ihr Blog-Beitrag wird von vielen Kolleginnen und Kollegen gelesen. Achten Sie deshalb auf Rechtschreibung und drücken Sie erst auf „Senden“ wenn Sie sich sicher sind, dass Sie Ihren Beitrag so veröffentlichen möchten.</li>
        </ul>
        <h3>Blog-Verhaltensregeln</h3>
        <ul>
            <li>Im Mitarbeiter-Blog behandeln wir andere Nutzer so, wie wir selbst gerne behandelt werden möchten.</li>
            <li>Wir achten beim Zitieren auf das geistige Eigentum anderer und geben die entsprechende Quelle an. Wenn wir uns nicht sicher sind, ob der Urheber mit unserem Beitrag einverstanden ist, halten wir Rücksprache mit diesem Kollegen oder dieser Kollegin.</li>
            <li>Wir versuchen, Mutmaßungen zu vermeiden oder kennzeichnen diese klar im Beitrag.</li>
            <li>Ironie und Wortwitz funktionieren im Internet oftmals nicht so gut wie von Angesicht zu Angesicht. Wir achten darauf, dass unser Beitrag nicht zweideutig ist und somit falsch verstanden werden könnte.</li>
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
<p>Beiträge, die Kolleginnen oder Kollegen aufgrund ihres Geschlechts, ihres Alters, ihrer Sprache, ihrer Abstammung, ihrer Religion, ihrer Weltanschauung, einer Behinderung oder ihrer sexuellen Orientierung diskriminieren oder diffamieren, werden gelöscht. Denken Sie daran, dass Sie es mit Menschen und nicht mit virtuellen Persönlichkeiten zu tun haben.</p>
<p>Sollten Sie Fragen zum Mitarbeiter-Blog oder den Blog-Regeln haben, können Sie sich jederzeit an uns unter blog-redaktion@intern.lmu.de wenden.</p>
<p><strong>Viel Spaß beim Bloggen!<br />
Ihre Intranet-Redaktion</strong></p>
""",
        'type': 'Blog Folder',
        'path': '/'
    },
    'umfragen': {
        'title': 'Umfragen',
        'description': '',
        'text': """

""",
        'type': 'Poll Folder',
        'path': '/'
    },
    'pinnwand': {
        'title': 'Die ZUV Pinnwand',
        'description': 'Tauschen. Helfen. Kaufen.',
        'text': """
        <h2>Nutzungshinweise</h2>
        <p>Die ZUV-Pinnwand ist ein kostenloser Service für Mitarbeiterinnen und Mitarbeiter der ZUV. Die Pinnwand ist Teil des ZUV-Intranets und unterliegt daher der Ordnung für die Nutzung der ZUV-Infrastruktur. Mit der Nutzung der ZUV-Infrastruktur – einschließlich der Pinnwand – verpflichten sich Nutzerinnen und Nutzer, die in dieser Ordnung dargelegten Bestimmungen einzuhalten.</p>
        <h3>Zuständigkeit und Verantwortlichkeit für Pinnwand-Inhalte</h3>
        <p>Für den Inhalt einer veröffentlichten Nachricht ist die Verfasserin bzw. der Verfasser der Inhalte verantwortlich.
        Die LMU  kann für Inhalte, die von Einzelpersonen an die Pinnwand angebracht wurden, nicht haftbar gemacht werden.
        Sollte der Redaktion die Anbringung von bestimmungs- und/oder gesetzeswidrigen Inhalten bekannt werden, wird diese Nachricht gelöscht; die Pinnwand wird regelmäßig einer Qualitätssicherung unterzogen, eine ständige Prüfung der Pinnwand ist jedoch nicht möglich.</p>
        <p>Insbesondere sind Nutzungen unzulässig, die kriminelle, terroristische, rassistische, diskriminierende, verleumderische, pornographische Ziele oder eine Propaganda für verfassungswidrige Organisationen beinhalten oder auf andere Weise Strafgesetze verletzen.</p>
        <h3>Gewerbliche Nutzung</h3>
        <p>Die Nutzung der Pinnwand für gewerbliche Zwecke oder eine Nutzung in gewerbeähnlichem Umfang sind unzulässig.</p>
        <h3>Tipps und Tricks</h3>
        <ol>
            <li>Geben Sie Ihrer Anzeige eine aussagekräftige, konkrete Überschrift, damit diese besser gefunden wird und der Inhalt sofort erkennbar ist.</li>
            <li>Fotos erhöhen den Erfolg Ihrer Anzeige. Sie können bis zu 8 Fotos einbinden, stellen Sie dort die wichtigsten Merkmale dar. Tipps & Tricks, wie man das Produkt "in Szene" setzen kann<ul>
                <li>Sorgen Sie durch gute Lichtverhältnisse für gut erkennbare Fotos.</li>
                <li>Fotografieren Sie das Produkt ggf. von mehreren Seiten und ggf. auch Details des Produktes.</li>
                <li>Zeigen Sie der Fairness halber auch die Gebrauchsspuren oder eventuelle Schäden am Produkt.</li>
                </ul></li>
            <li>Beschreiben Sie, was Sie anbieten oder suchen, konkret, damit der Interessent oder die Interessentin sich ein genaues Bild darüber machen kann, was ihn oder sie erwartet.</li>
<li>Formatieren Sie Ihr Angebot und überprüfen Sie den Text auf Rechtschreibfehler. Eine übersichtliche und fehlerlose Anzeige wird gerne gelesen.</li>
</ol>
        """,
        'type': 'Pinnwand Folder',
        'path': '/'
    },
}
