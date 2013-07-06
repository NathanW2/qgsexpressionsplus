# -*- coding: utf-8 -*-
"""
/***************************************************************************
 expressionsDialog
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
"""

from PyQt4 import QtCore, QtGui
from ui_expressions import Ui_expressions
# create the dialog for zoom to point


class expressionsDialog(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        # Set up the user interface from Designer.
        self.ui = Ui_expressions()
        self.ui.setupUi(self)
        
    def addFunction(self, name):
        self.ui.functionsList.addItem(name)
