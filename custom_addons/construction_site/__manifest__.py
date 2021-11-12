# -*- coding: utf-8 -*-

{
    "name": "Construction site",
    "summary": """Construction site related information""",
    "description": """""",
    "author": "Patel Akash",
    "website": "https://www.aktivsoftware.com/",
    "category": "Construction",
    "version": "14.0.1.0.0",
    "depends": [
        "sale_management",
        "purchase",
        "account",
        "hr",
        "stock",
        "project",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/construction_site_wizard_views.xml",
        "views/construction_site_views.xml",
        "views/sale_order_views.xml",
        "views/purchase_views.xml",
        "views/project_task_views.xml",
        "report/student_detail_report.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
