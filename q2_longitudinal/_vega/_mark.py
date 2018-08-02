# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._const import (
    GLOBAL_VALS, MIN_X, MAX_X, MEAN, CL0, CL1, CL2, CL3, CONTROL_X_SCALE,
    CONTROL_Y_SCALE, SHOW_GLOBAL_MEAN_SIGNAL, STROKE_2, OPACITY_000,
    OPACITY_100, DASH_A, DASH_B, SHOW_GLOBAL_CONTROL_LIMITS_SIGNAL, WIDTH,
    CONTROL_CHART_HEIGHT_SIGNAL, RULE, GROUP)


# # TODO: new template names
# mean_signal = ('{"title": "group mean", "group": datum.groupByVal,'
#                ' "state": datum["%s"], "count": datum.count,'
#                ' "mean": datum.mean, "ci0": datum.ci0, "ci1": datum.ci1}'
#                % state)


def _control_chart_subplot(state, yscale):
    return \
        {'description': 'Control Chart',
         'name': 'spaghetti',
         'type': GROUP,
         'encode': {
             'enter': {
                 'y': {'value': 0},
                 'width': {'signal': WIDTH},
                 'height': {'signal': CONTROL_CHART_HEIGHT_SIGNAL},
                }},
         'marks': [],
         'scales': [],
         'axes': [],
         'legends': []}


def _control_chart_global_marks():
    return [
        # Global Mean
        {'type': RULE,
         'from': {'data': GLOBAL_VALS},
         'encode': {
             'update': {
                 'strokeWidth': {'value': STROKE_2},
                 'x': {'scale': CONTROL_X_SCALE, 'field': MIN_X},
                 'x2': {'scale': CONTROL_X_SCALE, 'field': MAX_X},
                 'y': {'scale': CONTROL_Y_SCALE, 'field': MEAN},
                 'strokeOpacity': [
                     {'test': SHOW_GLOBAL_MEAN_SIGNAL, 'value': OPACITY_100},
                     {'value': OPACITY_000}]}}},
        # Global confidence limit, -3x std dev
        {'type': RULE,
         'from': {'data': 'globalVals'},
         'encode': {
             'update': {
                 'strokeWidth': {'value': STROKE_2},
                 'strokeDash': {'value': DASH_A},
                 'x': {'scale': CONTROL_X_SCALE, 'field': MIN_X},
                 'x2': {'scale': CONTROL_X_SCALE, 'field': MAX_X},
                 'y': {'scale': CONTROL_Y_SCALE, 'field': CL0},
                 'strokeOpacity': [
                     {'test': SHOW_GLOBAL_CONTROL_LIMITS_SIGNAL,
                      'value': OPACITY_100},
                     {'value': OPACITY_000},
                 ]}}},
        # Global confidence limit, -2x std dev
        {'type': RULE,
         'from': {'data': GLOBAL_VALS},
         'encode': {
             'update': {
                 'strokeWidth': {'value': STROKE_2},
                 'strokeDash': {'value': DASH_B},
                 'x': {'scale': CONTROL_X_SCALE, 'field': MIN_X},
                 'x2': {'scale': CONTROL_X_SCALE, 'field': MAX_X},
                 'y': {'scale': CONTROL_Y_SCALE, 'field': CL1},
                 'strokeOpacity': [
                     {'test': SHOW_GLOBAL_CONTROL_LIMITS_SIGNAL,
                      'value': OPACITY_100},
                     {'value': OPACITY_000},
                 ]}}},
        # Global confidence limit, +2x std dev
        {'type': RULE,
         'from': {'data': GLOBAL_VALS},
         'encode': {
             'update': {
                 'strokeWidth': {'value': STROKE_2},
                 'strokeDash': {'value': DASH_A},
                 'x': {'scale': CONTROL_X_SCALE, 'field': MIN_X},
                 'x2': {'scale': CONTROL_X_SCALE, 'field': MAX_X},
                 'y': {'scale': CONTROL_Y_SCALE, 'field': CL2},
                 'strokeOpacity': [
                     {'test': SHOW_GLOBAL_CONTROL_LIMITS_SIGNAL,
                      'value': OPACITY_100},
                     {'value': OPACITY_000},
                 ]}}},
        # Global confidence limit, +3x std dev
        {'type': RULE,
         'from': {'data': GLOBAL_VALS},
         'encode': {
             'update': {
                 'strokeWidth': {'value': STROKE_2},
                 'strokeDash': {'value': DASH_B},
                 'x': {'scale': CONTROL_X_SCALE, 'field': MIN_X},
                 'x2': {'scale': CONTROL_X_SCALE, 'field': MAX_X},
                 'y': {'scale': CONTROL_Y_SCALE, 'field': CL3},
                 'strokeOpacity': [
                     {'test': SHOW_GLOBAL_CONTROL_LIMITS_SIGNAL,
                      'value': OPACITY_100},
                     {'value': OPACITY_000},
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
