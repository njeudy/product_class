# -*- coding: utf-8 -*-

{
    "name": 'product_class',
    "description": u"""
===========
Description
===========

This module add a class on product to manage different kind of product and easy filter
This is not a replacement for category. It's just a functionnal field use in many other modules.

====
Team
====

- Nicolas JEUDY <njeudy@tuxservices.com>

""",
    "version": "0.1",
    "depends": [
        'base',
        'product',
        'sale',
    ],
    "author": "Tuxservices - 0k.io",
    "installable" : True,
    "active" : False,
    "data": [
        'product_class_view.xml',
        'ir_actions_act_window_record.xml',
        'ir_ui_menu_record.xml',
        'security/access.xml',
    ],
}

