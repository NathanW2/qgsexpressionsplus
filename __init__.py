# -*- coding: utf-8 -*-
"""
/***************************************************************************
 expressions
                                 A QGIS plugin
 Extra functions for the expression engine which didn't make it into 2.0
                             -------------------
        begin                : 2013-06-29
        copyright            : (C) 2013 by Nathan Woodrow
        email                : woodrow.nathan@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load expressions class from file expressions
    from expressionsplus import ExpressionsPlus
    return ExpressionsPlus(iface)
