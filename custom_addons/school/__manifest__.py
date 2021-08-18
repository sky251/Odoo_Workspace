
{
    'name': 'School Management',
    'version': '14.0.1.0.0',
    'category': 'Education',
    'summary': 'School management system',
    'sequence': 1,
    'website': 'https://www.aktivesoftware.com/',
    'description': 'This module gives a framework for SMS text messaging',
    'depends': ['base', 'mail', ],
    "data": [
        "security/ir.model.access.csv",
        "data/school_data.xml",
        "data/student_data.xml",
        "views/school_views.xml",
        "views/student_views.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": True,
}
