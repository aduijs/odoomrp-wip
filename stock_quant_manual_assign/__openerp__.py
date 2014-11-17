
# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Manual assignment of quants",
    "version": "1.0",
    "depends": ["base", "stock"],
    "author": "OdooMRP team",
    "contributors": ["Mikel Arregi <mikelarregi@avanzosc.es>"],
    "category": "quant",
    "description": """
    With this module, user can change manualy the automatic selection of quants
    """,
    'data': ['wizard/assign_manual_quants_view.xml',
             'views/stock_move_view.xml'],
    "installable": True,
    "auto_install": False,
}
