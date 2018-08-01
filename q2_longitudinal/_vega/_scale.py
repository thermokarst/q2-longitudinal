# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


_CONTROL_X_SCALE = 'x'
_CONTROL_Y_SCALE = 'y'


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
