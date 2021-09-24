{
    "name": "Documentation management",
    "version": "14.0.1.0.0",
    "website": "https://www.aktivesoftware.com",
    "category": "Document",
    "summary": """Document related work""",
    "description": "This module manage all document related work",
    "depends": [
        "base",
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/document_views.xml",
        "views/document_tag_views.xml",
        "views/document_version_views.xml",
    ],
    "demo": [],
    "sequence": 2,
    "application": True,
    "installable": True,
    "auto-install": False,
}
