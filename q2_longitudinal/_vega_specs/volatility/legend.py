# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .const import (
    CONTROL_SYMBOL_LEGEND, CONTROL_LABEL_LEGEND, TRANSPARENT, SIG_GROUP,
    SCL_CTRL_COLOR, OPACITY_TEST, STY_STROKE_2,
    )


def _control_chart_legend():
    return [
        {'stroke': SCL_CTRL_COLOR,
         'title': SIG_GROUP,
         'encode': {
             'symbols': {
                 'name': CONTROL_SYMBOL_LEGEND,
                 'interactive': True,
                 'update': {
                     'fill': {'value': TRANSPARENT},
                     'strokeWidth': {'value': STY_STROKE_2},
                     'opacity': [
                         {'test': OPACITY_TEST, 'value': 1.0},
                         {'value': 0.15},
                     ],
                     'size': {'value': 100}}},
             'labels': {
                 'name': CONTROL_LABEL_LEGEND,
                 'interactive': True,
                 'update': {
                     'opacity': [
                         {'test': OPACITY_TEST, 'value': 1.0},
                         {'value': 0.25}]}}}}]
