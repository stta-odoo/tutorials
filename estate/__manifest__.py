{
    'name': 'Real Estate',
    'application': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_views.xml',
        'views/estate_property_menus.xml',
        'views/res_users_views.xml',
        'data/estate_property_type_data.xml',
        'demo/estate_property_demo.xml',
    ],
}