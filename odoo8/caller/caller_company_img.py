# -*- coding: utf-8 -*-
# got from https://raw.githubusercontent.com/netjunky-hub/company_setup/master/company_setup/company_image.py

from openerp import api, fields, models


class res_company(models.Model):
    _inherit = "res.company"
    _name = "res.company"

    def init(self, cr):
        img = open(os.path.join(os.path.dirname(__file__),
                                'static', 'src', 'img', 'logo.png'), 'rb').read().encode('base64')
        cr.execute('UPDATE res_partner SET image=%s WHERE is_company=TRUE', (img,))
        size = (180, None)
        cr.execute('UPDATE res_company SET logo_web=%s', (image_resize_image(img, size),))
