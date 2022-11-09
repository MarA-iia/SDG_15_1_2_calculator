# -*- coding: utf-8 -*-

"""
/***************************************************************************
 SDG_15_1_2_calculator
                                 A QGIS plugin
 Proportion of important sites for terrestrial and freshwater biodiversity that are covered by protected areas, by ecosystem type
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-07-14
        copyright            : (C) 2022 by IIA-CNR
        email                : aquilino@iia.cnr.it
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

__author__ = 'IIA-CNR'
__date__ = '2022-07-14'
__copyright__ = '(C) 2022 by IIA-CNR'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from qgis.core import QgsProcessingAlgorithm, QgsApplication
from .SDG_15_1_2_calculator_provider import SDG_15_1_2_calculatorProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class SDG_15_1_2_calculatorPlugin(object):

    def __init__(self):
        self.provider = None

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = SDG_15_1_2_calculatorProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
