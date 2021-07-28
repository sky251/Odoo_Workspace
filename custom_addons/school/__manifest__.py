
{
    'name': 'School Management',
    'version': '14.0.1.0.0',
    'category': 'Education',
    'summary': 'School management system',
    'sequence': 1,
    'website': 'https://www.google.com/',
    'description': 'This module gives a framework for SMS text messaging',
    'depends': ['base'],
    "data": [
        "security/ir.model.access.csv",
        "views/school_views.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": True,
}
