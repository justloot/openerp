##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Product Reports",
    "version" : "1.0",
    "author" : "Denis Karataev",
    "category" : "Generic Modules",
    "depends" : ["product",
                 "product_base_dsk",
                 "eshop_base_dsk",
                 "product_attribute_dsk",
                 "product_category_flags_dsk",
                 "product_competitor_price_dsk",
                 "product_description_dsk",
                 "product_flags_dsk",
                 "product_images_dsk",
                 "product_manufacturer_dsk",
                 "product_size_dsk"],
    "init_xml" : [],
    "demo_xml" : [],
    "description": "A module that contains product reports",
    "update_xml" : ["eshop_xml_report.xml"],
    "active": False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
