# -*- coding: utf-8 -*-

{
    "name": "Tracking order",
    "summary": """""",
    "description": """""",
    "author": "Akash Patel",
    "website": "aktivsoftware.com",
    # for the full list
    "category": "sale",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["base", "sale_management", "sale"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/tracking_order_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
