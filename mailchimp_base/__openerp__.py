# -*- coding: utf-8 -*-
###############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2014-Today Trey, Kilobytes de Soluciones <www.trey.es>
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
###############################################################################

{
    'name': 'Mailchimp base',
    'summary': 'Mailchimp connect',
    'category': 'Management',
    'version': '1.0',
    'description': """
Connect with MailChimp account and performs several operations.

Need install mailchimp module:
    pip install mailchimp
    """,
    'author': 'Trey Kilobytes de Soluciones (www.trey.es)',
    'website': 'http://www.trey.es',
    'depends': [
        'base',
    ],
    'data': [
        # security
        'security/security.xml',
        'security/ir.model.access.csv',

        'wizards/mailchimp_change_list.xml',
        'views/mailchimp_base.xml',
        'views/menu.xml'
    ],
    'test': [
    ],
    'installable': True,
}
