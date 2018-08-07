# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .const import (
    CONTROL_SYMBOL_LEGEND, CONTROL_LABEL_LEGEND, TRANSPARENT, SIG_GROUP,
    CONTROL_COLOR_SCALE, OPACITY_TEST, STROKE_2, OPACITY_015, OPACITY_025,
    OPACITY_100, SIZE_100)


def _control_chart_legend():
    return [
        {'stroke': CONTROL_COLOR_SCALE,
         'title': SIG_GROUP,
         'encode': {
             'symbols': {
                 'name': CONTROL_SYMBOL_LEGEND,
                 'interactive': True,
                 'update': {
                     'fill': {'value': TRANSPARENT},
                     'strokeWidth': {'value': STROKE_2},
                     'opacity': [
                         {'test': OPACITY_TEST, 'value': OPACITY_100},
                         {'value': OPACITY_015},
                     ],
                     'size': {'value': SIZE_100}}},
             'labels': {
                 'name': CONTROL_LABEL_LEGEND,
                 'interactive': True,
                 'update': {
                     'opacity': [
                         {'test': OPACITY_TEST, 'value': OPACITY_100},
                         {'value': OPACITY_025}]}}}}]
