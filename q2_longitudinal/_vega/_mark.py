# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._data import _GLOBAL_VALS, _MIN_X, _MAX_X, _MEAN, _CL0, _CL1, _CL2, _CL3
# from ._test import GROUP_TEST, ERROR_BAR_TEST
from ._scale import _CONTROL_X_SCALE, _CONTROL_Y_SCALE
from ._signal import (_SHOW_GLOBAL_MEAN_SIGNAL,
                      _SHOW_GLOBAL_CONTROL_LIMITS_SIGNAL)


_GLOBAL_STROKE = 2
_GLOBAL_3X_DASH = [8, 8]
_GLOBAL_2X_DASH = [6, 2]
_OPACITY_0 = 0.0
_OPACITY_1 = 1.0


# This looks grosser than it is (you can't do variable assignment in a
# vega expr, so no temp helper vars) - basically find the min and max
# extents of the metric in question for the y-axis rendering, including
# the 3x stdev (depending on the spread this could be beyond the metric's
# own limits.
domain_expr = ("[min(data('globalVals')[0].cl0,"
               "data('globalVals')[0].minY),"
               "max(data('globalVals')[0].cl3,"
               "data('globalVals')[0].maxY)]")

# # TODO: new template names
# mean_signal = ('{"title": "group mean", "group": datum.groupByVal,'
#                ' "state": datum["%s"], "count": datum.count,'
#                ' "mean": datum.mean, "ci0": datum.ci0, "ci1": datum.ci1}'
#                % state)


def _control_chart_global_marks():
    return [
        # Global Mean
        {'type': 'rule',
         'from': {'data': _GLOBAL_VALS},
         'encode': {
             'update': {
                 'strokeWidth': {'value': _GLOBAL_STROKE},
                 'x': {'scale': _CONTROL_X_SCALE, 'field': _MIN_X},
                 'x2': {'scale': _CONTROL_X_SCALE, 'field': _MAX_X},
                 'y': {'scale': _CONTROL_Y_SCALE, 'field': _MEAN},
                 'strokeOpacity': [
                     {'test': _SHOW_GLOBAL_MEAN_SIGNAL, 'value': _OPACITY_1},
                     {'value': _OPACITY_0}]}}},
        # Global confidence limit, -3x std dev
        {'type': 'rule',
         'from': {'data': 'globalVals'},
         'encode': {
             'update': {
                 'strokeWidth': {'value': _GLOBAL_STROKE},
                 'strokeDash': {'value': _GLOBAL_3X_DASH},
                 'x': {'scale': _CONTROL_X_SCALE, 'field': _MIN_X},
                 'x2': {'scale': _CONTROL_X_SCALE, 'field': _MAX_X},
                 'y': {'scale': _CONTROL_Y_SCALE, 'field': _CL0},
                 'strokeOpacity': [
                     {'test': _SHOW_GLOBAL_CONTROL_LIMITS_SIGNAL,
                      'value': _OPACITY_1},
                     {'value': _OPACITY_0},
                 ]}}},
        # Global confidence limit, -2x std dev
        {'type': 'rule',
         'from': {'data': _GLOBAL_VALS},
         'encode': {
             'update': {
                 'strokeWidth': {'value': _GLOBAL_STROKE},
                 'strokeDash': {'value': _GLOBAL_2X_DASH},
                 'x': {'scale': _CONTROL_X_SCALE, 'field': _MIN_X},
                 'x2': {'scale': _CONTROL_X_SCALE, 'field': _MAX_X},
                 'y': {'scale': _CONTROL_Y_SCALE, 'field': _CL1},
                 'strokeOpacity': [
                     {'test': _SHOW_GLOBAL_CONTROL_LIMITS_SIGNAL,
                      'value': _OPACITY_1},
                     {'value': _OPACITY_0},
                 ]}}},
        # Global confidence limit, +2x std dev
        {'type': 'rule',
         'from': {'data': _GLOBAL_VALS},
         'encode': {
             'update': {
                 'strokeWidth': {'value': _GLOBAL_STROKE},
                 'strokeDash': {'value': _GLOBAL_2X_DASH},
                 'x': {'scale': _CONTROL_X_SCALE, 'field': _MIN_X},
                 'x2': {'scale': _CONTROL_X_SCALE, 'field': _MAX_X},
                 'y': {'scale': _CONTROL_Y_SCALE, 'field': _CL2},
                 'strokeOpacity': [
                     {'test': _SHOW_GLOBAL_CONTROL_LIMITS_SIGNAL,
                      'value': _OPACITY_1},
                     {'value': _OPACITY_0},
                 ]}}},
        # Global confidence limit, +3x std dev
        {'type': 'rule',
         'from': {'data': _GLOBAL_VALS},
         'encode': {
             'update': {
                 'strokeWidth': {'value': _GLOBAL_STROKE},
                 'strokeDash': {'value': _GLOBAL_3X_DASH},
                 'x': {'scale': _CONTROL_X_SCALE, 'field': _MIN_X},
                 'x2': {'scale': _CONTROL_X_SCALE, 'field': _MAX_X},
                 'y': {'scale': _CONTROL_Y_SCALE, 'field': _CL3},
                 'strokeOpacity': [
                     {'test': _SHOW_GLOBAL_CONTROL_LIMITS_SIGNAL,
                      'value': _OPACITY_1},
                     {'value': _OPACITY_0},
                 ]}}}]


# def _foo(state):
#     return {
#             'type': 'group',
#             'from': {
#                 'facet': {
#                     'name': 'series',
#                     'data': 'aggBy',
#                     'groupby': 'groupByVal',
#                 },
#             },
#             'marks': [
#                 {
#                     'type': 'line',
#                     'from': {
#                         'data': 'series',
#                     },
#                     'sort': {
#                         'field': 'datum.%s' % state,
#                         'order': 'ascending',
#                     },
#                     'encode': {
#                         'update': {
#                             'x': {
#                                 'scale': 'x',
#                                 'field': state,
#                             },
#                             'y': {
#                                 'scale': 'y',
#                                 'field': 'mean',
#                             },
#                             'stroke': {
#                                 'scale': 'color',
#                                 'field': 'groupByVal',
#                             },
#                             'strokeWidth': {
#                                 'signal': 'meanLineThickness',
#                             },
#                             'opacity': [
#                                 {
#                                     'test': group_test,
#                                     'signal': 'meanLineOpacity',
#                                 },
#                                 {
#                                     'value': 0.0,
#                                 },
#                             ],
#                         },
#                     },
#                 },
#                 # Need to add symbols into plot for mouseover
#                 # https://github.com/vega/vega-tooltip/issues/120
#                 {
#                     'type': 'symbol',
#                     'from': {
#                         'data': 'series',
#                     },
#                     'encode': {
#                         'update': {
#                             'tooltip': {
#                                 'signal': mean_signal,
#                             },
#                             'x': {
#                                 'scale': 'x',
#                                 'field': state,
#                             },
#                             'y': {
#                                 'scale': 'y',
#                                 'field': 'mean',
#                             },
#                             'stroke': {
#                                 'scale': 'color',
#                                 'field': 'groupByVal',
#                             },
#                             'fill': {
#                                 'scale': 'color',
#                                 'field': 'groupByVal',
#                             },
#                             'size': {
#                                 'signal': 'meanSymbolSize',
#                             },
#                             'opacity': [
#                                 {
#                                     'test': group_test,
#                                     'signal': 'meanSymbolOpacity',
#                                 },
#                                 {
#                                     'value': 0.0,
#                                 },
#                             ],
#                         },
#                     },
#                 },
#                 {
#                     'type': 'rect',
#                     'from': {
#                         'data': 'series',
#                     },
#                     'encode': {
#                         'update': {
#                             'width': {
#                                 'value': 2.0,
#                             },
#                             'x': {
#                                 'scale': 'x',
#                                 'field': state,
#                                 'band': 0.5,
#                             },
#                             'y': {
#                                 'scale': 'y',
#                                 'field': 'ci0',
#                             },
#                             'y2': {
#                                 'scale': 'y',
#                                 'field': 'ci1',
#                             },
#                             'fill': {
#                                 'scale': 'color',
#                                 'field': 'groupByVal',
#                             },
#                             'opacity': [
#                                 {
#                                     'test': error_bar_test,
#                                     'value': 1.0,
#                                 },
#                                 {
#                                     'value': 0.0,
#                                 },
#                             ],
#                         },
#                     },
#                 },
#             ],
#         },
#     ]
#
#
def _individual_marks(individual_id, state, metric_signal, group_signal,
                      group_test, spaghetti_signal):
    return {
        'type': 'group',
        'from': {
            'facet': {
                'name': 'spaghettis',
                'data': 'individual',
                'groupby': individual_id,
            },
        },
        'marks': [
            {
                'type': 'line',
                'from': {
                    'data': 'spaghettis',
                },
                'sort': {
                    'field': 'datum.%s' % state,
                    'order': 'ascending',
                },
                'encode': {
                    'update': {
                        'strokeWidth': {
                            'signal': 'spaghettiLineThickness',
                        },
                        'x': {
                            'scale': 'x',
                            'field': state,
                        },
                        'y': {
                            'scale': 'y',
                            'field': metric_signal,
                        },
                        'stroke': {
                            'scale': 'color',
                            'field': group_signal,
                        },
                        'opacity': [
                            {
                                'test': group_test,
                                'signal': 'spaghettiLineOpacity',
                            },
                            {
                                'value': 0.0,
                            },
                        ],
                    },
                },
            },
            # Need to add symbols into plot for mouseover
            # https://github.com/vega/vega-tooltip/issues/120
            {
                'type': 'symbol',
                'from': {
                    'data': 'spaghettis',
                },
                'encode': {
                    'update': {
                        'tooltip': {
                            'signal': spaghetti_signal,
                        },
                        'size': {
                            'signal': 'spaghettiSymbolSize',
                        },
                        'x': {
                            'scale': 'x',
                            'field': state,
                        },
                        'y': {
                            'scale': 'y',
                            'field': metric_signal,
                        },
                        'stroke': {
                            'scale': 'color',
                            'field': group_signal,
                        },
                        'fill': {
                            'scale': 'color',
                            'field': group_signal,
                        },
                        'opacity': [
                            {
                                'test': group_test,
                                'signal': 'spaghettiSymbolOpacity',
                            },
                            {
                                'value': 0.0,
                            },
                        ],
                    },
                },
            },
        ],
    }


def _control_chart_marks(spaghetti_marks, state, yscale, group_signal,
                         metric_signal, opacity_test):
    return [
        {
            'description': 'Control Chart',
            'name': 'spaghetti',
            'type': 'group',
            'encode': {
                'enter': {
                    'y': {
                        'value': 0,
                    },
                    'width': {
                        'signal': 'width',
                    },
                    'height': {
                        'signal': 'controlChartHeight',
                    },
                },
            },
            'marks': spaghetti_marks,
            'scales': [
                {
                    'name': 'x',
                    'type': 'linear',
                    'range': 'width',
                    'nice': True,
                    'domain': {
                        'data': 'individual',
                        'field': state,
                        'sort': True,
                    },
                },
                {
                    'name': 'y',
                    # Signal registration on this param is currently
                    # blocked by https://github.com/vega/vega/issues/525,
                    # which is why this setting is still a QIIME 2 param to
                    # this viz.
                    'type': yscale,
                    'range': [
                        {
                            'signal': 'controlChartHeight',
                        },
                        0,
                    ],
                    'nice': True,
                    'domain': {
                        'signal': domain_expr,
                        'sort': True,
                    },
                },
                {
                    'name': 'color',
                    'type': 'ordinal',
                    'range': {
                        'scheme': {
                            'signal': 'colorScheme',
                        },
                    },
                    'domain': {
                        'data': 'individual',
                        'field': group_signal,
                    },
                },
            ],
            'axes': [
                {
                    'orient': 'bottom',
                    'scale': 'x',
                    'title': state,
                },
                {
                    'orient': 'left',
                    'scale': 'y',
                    # TODO: for feature volatility, include the fact
                    # that this is the relative abundance
                    'title': metric_signal,
                },
            ],
            'legends': [
                {
                    'stroke': 'color',
                    'title': group_signal,
                    'encode': {
                        'symbols': {
                            'name': 'legendSymbol',
                            'interactive': True,
                            'update': {
                                'fill': {
                                    'value': 'transparent',
                                },
                                'strokeWidth': {
                                    'value': 2,
                                },
                                'opacity': [
                                    {
                                        'test': opacity_test,
                                        'value': 1.0,
                                    },
                                    {
                                        'value': 0.15,
                                    },
                                ],
                                'size': {
                                    'value': 100,
                                },
                            },
                        },
                        'labels': {
                            'name': 'legendLabel',
                            'interactive': True,
                            'update': {
                                'opacity': [
                                    {
                                        'test': opacity_test,
                                        'value': 1,
                                    },
                                    {
                                        'value': 0.25,
                                    },
                                ],
                            },
                        },
                    },
                },
            ],
        },
    ]
