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
    CONTROL_CHART_HEIGHT_SIGNAL, RULE, GROUP, SERIES, AGG_BY_DATA,
    GROUP_BY_VALUE, LINE, ASCENDING_ORDER, CONTROL_COLOR_SCALE,
    CONTROL_MEAN_LINE_THICKNESS_SIGNAL, SYMBOL,
    CONTROL_MEAN_SYMBOL_SIZE_SIGNAL, GROUP_TEST,
    CONTROL_MEAN_LINE_OPACITY_SIGNAL, CONTROL_MEAN_SYMBOL_OPACITY_SIGNAL,
    RECT_2, RECT, BAND_050, CI0, CI1, ERROR_BAR_TEST)


def _control_chart_subplot(yscale):
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


def _control_chart_grouped_marks(state):
    datum_state = "datum['%s']" % state
    # TODO: Clean this up
    mean_signal = ('{"title": "group mean", "group": datum.groupByVal,'
                   ' "state": datum["%s"], "count": datum.count,'
                   ' "mean": datum.mean, "ci0": datum.ci0, "ci1": datum.ci1}'
                   % state)
    return [
        {'type': GROUP,
         'from': {
             # Regroup by "group" column
             'facet': {
                 'name': SERIES,
                 'data': AGG_BY_DATA,
                 'groupby': GROUP_BY_VALUE}},
         'marks': [
             # Per-group mean lines
             {'type': LINE,
              'from': {'data': SERIES},
              'sort': {'field': datum_state, 'order': ASCENDING_ORDER},
              'encode': {
                  'update': {
                      'x': {'scale': CONTROL_X_SCALE, 'field': state},
                      'y': {'scale': CONTROL_Y_SCALE, 'field': MEAN},
                      'stroke': {'scale': CONTROL_COLOR_SCALE,
                                 'field': GROUP_BY_VALUE},
                      'strokeWidth': {'signal':
                                      CONTROL_MEAN_LINE_THICKNESS_SIGNAL},
                      'opacity': [
                          {'test': GROUP_TEST,
                           'signal': CONTROL_MEAN_LINE_OPACITY_SIGNAL},
                          {'value': OPACITY_000},
                      ]}}},
             # per-group symbols
             {'type': SYMBOL,
              'from': {'data': SERIES},
              'encode': {
                  'update': {
                      'tooltip': {'signal': mean_signal},
                      'x': {'scale': CONTROL_X_SCALE, 'field': state},
                      'y': {'scale': CONTROL_Y_SCALE, 'field': MEAN},
                      'stroke': {'scale': CONTROL_COLOR_SCALE,
                                 'field': GROUP_BY_VALUE},
                      'fill': {'scale': CONTROL_COLOR_SCALE,
                               'field': GROUP_BY_VALUE},
                      'size': {'signal': CONTROL_MEAN_SYMBOL_SIZE_SIGNAL},
                      'opacity': [
                          {'test': GROUP_TEST,
                           'signal': CONTROL_MEAN_SYMBOL_OPACITY_SIGNAL},
                          {'value': OPACITY_000}]}}},
             # Per-group error bars
             {'type': RECT,
              'from': {'data': SERIES},
              'encode': {
                  'update': {
                      'width': {'value': RECT_2},
                      'x': {'scale': CONTROL_X_SCALE, 'field': state,
                            'band': BAND_050},
                      'y': {'scale': CONTROL_Y_SCALE, 'field': CI0},
                      'y2': {'scale': CONTROL_Y_SCALE, 'field': CI1},
                      'fill': {'scale': CONTROL_COLOR_SCALE,
                               'field': GROUP_BY_VALUE},
                      'opacity': [
                          {'test': ERROR_BAR_TEST, 'value': OPACITY_100},
                          {'value': OPACITY_000}]}}}]}]


# TODO: revisit this
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
