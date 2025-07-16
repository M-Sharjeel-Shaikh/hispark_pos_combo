{
    "name": "POS – Combo & Custom Deal Builder",
    "version": "16.0",
    "category": "Point of Sale",
    "summary": "Create flexible combo deals and custom product packs directly from the POS interface, "
               "with support for half-and-half options and dynamic product selection.",
    "description":"""
        This module enhances the Odoo Point of Sale (POS) system by enabling advanced combo and deal-building features commonly used in restaurants, food chains, and retail stores. It allows for both fixed combos and "Make Your Own" product configurations, ensuring flexibility and customer satisfaction at the POS level.

        Key Features:
        - Combo Product Support**: Mark products as combo deals and define fixed items included.
        - Custom Combo Builder**: Enable “Make Your Own” product selections where customers can choose items from predefined categories (e.g., Pizza, Drinks, Sides).
        - POS Integration**: Fully integrated within the POS screen, making selection intuitive and quick.
        - Product Tagging**: Mark any product as a fixed combo or a customizable product.
        - Half-and-Half Support**: Handle special cases like customers requesting two different flavors or halves of a product (e.g., pizza).
        - Easy UX/UI**: Dynamic interface for fast selection, quantity adjustment, and clear visibility of combo contents.
        
        This module is ideal for:
        - Restaurants & Cafés
        - Fast Food Chains
        - Grocery Stores with Meal Deals
        - Any POS setup needing product bundling or dynamic combo creation
        
        Boost customer satisfaction and upsell opportunities by offering interactive, personalized combo options right from your Odoo POS!
    """,

    "author": "Hi Spark Solutions",
    "company": "Hi Spark Solutions",
    "maintainer": "Hi Spark Solutions",
    "website": "https://www.hisparksolutions.com/",

    "depends": ["base", "point_of_sale", "pos_restaurant"],
    "demo": [],
    "data": [
        "security/ir.model.access.csv",
        "security/security_group.xml",
        "views/pos_product_pack_view.xml",
        "views/combo_selective_product.xml",
        "views/combo_fixed_product.xml",
        "views/pos_order_line.xml"
    ],
    "assets": {
        "point_of_sale.assets": [
            "hispark_pos_combo/static/src/css/pos_product_pack.css",
            "hispark_pos_combo/static/src/lib/jquery-ui.js",
            "hispark_pos_combo/static/src/js/pos_product_pack_file.js",
            "hispark_pos_combo/static/src/js/product_screen.js",
            "hispark_pos_combo/static/src/js/combo_screen.js",
            "hispark_pos_combo/static/src/xml/pos_view.xml",
        ],
    },

    "images": ["static/description/banner.gif"],
    "qweb": [],
    "live_test_url": "",

    "license": "OPL-1",
    "application": True,
    "auto_install": False,
    "installable": True,
    "price": "5",
    "currency": "USD",
}
