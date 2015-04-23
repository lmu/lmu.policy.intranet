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
