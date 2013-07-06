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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui_expressions import Ui_expressions
# Initialize Qt resources from file resources.py
import resources_rc
import os.path
import functions

class expressionsDialog(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        # Set up the user interface from Designer.
        self.ui = Ui_expressions()
        self.ui.setupUi(self)
        
    def addFunction(self, name):
        self.ui.functionsList.addItem(name)

class ExpressionsPlus:
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'expressions_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
                
    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/expressions/icon.svg"),
            u"Registered Functions", self.iface.mainWindow())
        
        self.dlg = expressionsDialog()
        self.action.triggered.connect(self.dlg.exec_)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&QgsFunctions +", self.action)
        
        for func in functions.registerFunctions():
            self.dlg.addFunction(func)
              
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&QgsFunctions +", self.action)
        self.iface.removeToolBarIcon(self.action)
        
        functions.unregisterFunctions()

    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass
