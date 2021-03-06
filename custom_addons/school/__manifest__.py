{
    "name": "School Management",
    "version": "14.0.1.0.0",
    "category": "Education",
    "summary": "School management system",
    "sequence": 1,
    "website": "https://www.aktivesoftware.com/",
    "description": "This module gives a framework for SMS text messaging",
    "depends": ["mail", "website_sale"],
    "data": [
        "security/ir.model.access.csv",
        "security/school_security.xml",
        "data/school_website_data.xml",
        "data/school_mail_template.xml",
        "wizard/create_wizard_views.xml",
        "views/controllers_views.xml",
        "views/school_views.xml",
        "views/student_views.xml",
        "wizard/create_wizard_views.xml",
        "report/student_detail_report.xml",
        "report/school_detail_report.xml",
        # "views/school_settings_views.xml",
    ],
    "demo": [
        "data/school_data.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}
