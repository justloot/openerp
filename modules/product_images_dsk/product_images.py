#########################################################################
# Copyright (C) 2009  Sharoon Thomas, Open Labs Business solutions      #
#                                                                       #
#This program is free software: you can redistribute it and/or modify   #
#it under the terms of the GNU General Public License as published by   #
#the Free Software Foundation, either version 3 of the License, or      #
#(at your option) any later version.                                    #
#                                                                       #
#This program is distributed in the hope that it will be useful,        #
#but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#GNU General Public License for more details.                           #
#                                                                       #
#You should have received a copy of the GNU General Public License      #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#########################################################################
from osv import osv, fields
import base64, urllib

class product_images(osv.osv):
    def get_image(self, cr, uid, id):
        each = self.read(cr, uid, id, ['image'])
        return each['image']

    def _get_image(self, cr, uid, ids, field_name, arg, context={}):
        res = {}
        for each in ids:
            res[each] = self.get_image(cr, uid, each)
        return res

    _name = "product.images"
    _columns = {
        'name':fields.char('Image title', size=100),
        'sequence': fields.integer('Sequence', help="Gives the sequence order when displaying a list of follow-up lines."),
        'type': fields.selection(
            [('image', 'Image'), ('scheme', 'Scheme'), ('flash3d', '3D flash animation')],
            'Image type', required=True),
        'image': fields.binary('Image', filters='*.png,*.jpg,*.swf', required=True),
        'file_ext': fields.selection([('jpg', 'JPG'), ('png', 'PNG'), ('gif', 'GIF')], 'File extension'),
        'preview': fields.function(_get_image, type="binary", method=True),
        'comments': fields.text('Comments'),
        'product_id': fields.many2one('product.product', 'Product', ondelete='cascade', required=True)
    }
    _order = 'sequence'
product_images()