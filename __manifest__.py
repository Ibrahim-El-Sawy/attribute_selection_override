{
    'name': 'POS Custom Attribute Image Size',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Increase product attribute image size in POS by 3x',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'attribute_selection_override/static/src/css/pos_custom_style.css',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}