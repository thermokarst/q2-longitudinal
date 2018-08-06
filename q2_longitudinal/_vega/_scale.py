# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from ._const import (INDIVIDUAL, CONTROL_CHART_HEIGHT_SIGNAL,
                     COLOR_SCHEME_SIGNAL, GLOBAL_DOMAIN_SIGNAL, GROUP_BY_VALUE,
                     CONTROL_X_SCALE, LINEAR, WIDTH, CONTROL_Y_SCALE,
                     CONTROL_COLOR_SCALE, ORDINAL)


def _layout_scale():
    return {
        'name': 'layoutY',
        'type': 'band',
        'domain': ['row1', 'row2'],
        'range': 'height',
        'nice': True,
    }


def _color_scale():
    return {
        'name': 'color',
        'type': 'ordinal',
        'range': {
            'scheme': {
                'signal': 'colorScheme',
            },
        },
        'domain': {
            'data': 'individual',
            'field': 'groupByVal',
        },
        'nice': True,
    }


def _control_chart_subplot_scales(state, yscale):
    return [
        {'name': CONTROL_X_SCALE,
         'type': LINEAR,
         'range': WIDTH,
         'nice': True,
         'domain': {
             'data': INDIVIDUAL,
             'field': state,
             'sort': True,
         }},
        {'name': CONTROL_Y_SCALE,
         # Signal registration on this param is currently
         # blocked by https://github.com/vega/vega/issues/525,
         # which is why this setting is still a QIIME 2 param to
         # this viz.
         'type': yscale,
         'range': [{'signal': CONTROL_CHART_HEIGHT_SIGNAL}, 0],
         'nice': True,
         'domain': {'signal': GLOBAL_DOMAIN_SIGNAL, 'sort': True}},
        {'name': CONTROL_COLOR_SCALE,
         'type': ORDINAL,
         'range': {'scheme': {'signal': COLOR_SCHEME_SIGNAL}},
         'domain': {'data': INDIVIDUAL, 'field': GROUP_BY_VALUE}}]
