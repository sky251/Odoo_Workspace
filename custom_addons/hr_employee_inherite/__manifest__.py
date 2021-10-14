# -*- coding: utf-8 -*-

{
    "name": "HR Employee",
    "version": "14.0.1.0.0",
    "sequence": 1,
    "category": "Human Resources",
    "description": """Hr sequence and wizard.""",
    "summary": "HR Employee",
    "depends": ["hr"],
    "data": [
        "security/ir.model.access.csv",
        "data/sequence_view.xml",
        "wizard/test_wizard_view.xml",
        "views/inherit_seq_view.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}