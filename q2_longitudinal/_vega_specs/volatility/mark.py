# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .const import (
    GLOBAL_VALS, MIN_X, MAX_X, MEAN, CL0, CL1, CL2, CL3, CONTROL_X_SCALE,
    CONTROL_Y_SCALE, SIG_SHOW_GLOBAL_MEAN, STROKE_2, OPACITY_000,
    OPACITY_100, DASH_A, DASH_B, SIG_SHOW_GLOBAL_CTRL_LIMS, WIDTH,
    SIG_CTRL_CHART_HEIGHT, RULE, GROUP, SERIES, AGG_BY_DATA,
    GROUP_BY_VALUE, LINE, ASCENDING_ORDER, CONTROL_COLOR_SCALE,
    CONTROL_MEAN_LINE_THICKNESS_SIGNAL, SYMBOL,
    CONTROL_MEAN_SYMBOL_SIZE_SIGNAL, GROUP_TEST,
    CONTROL_MEAN_LINE_OPACITY_SIGNAL, CONTROL_MEAN_SYMBOL_OPACITY_SIGNAL,
    RECT_2, RECT, BAND_050, CI0, CI1, ERROR_BAR_TEST, SPAGHETTIS, INDIVIDUAL,
    CONTROL_SPAGHET_LINE_THICKNESS_SIGNAL, SIG_METRIC, SIG_GROUP,
    CONTROL_SPAGHET_LINE_OPACITY_SIGNAL, CONTROL_SPAGHET_SYMBOL_SIZE_SIGNAL,
    CONTROL_SPAGHET_SYMBOL_OPACITY_SIGNAL)


def _control_chart_subplot(yscale):
    return \
        {'description': 'Control Chart',
         'name': 'spaghetti',
         'type': GROUP,
         'encode': {
             'enter': {
                 'y': {'value': 0},
                 'width': {'signal': WIDTH},
                 'height': {'signal': SIG_CTRL_CHART_HEIGHT},
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
                     {'test': SIG_SHOW_GLOBAL_MEAN, 'value': OPACITY_100},
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
                     {'test': SIG_SHOW_GLOBAL_CTRL_LIMS,
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
                     {'test': SIG_SHOW_GLOBAL_CTRL_LIMS,
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
                     {'test': SIG_SHOW_GLOBAL_CTRL_LIMS,
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
                     {'test': SIG_SHOW_GLOBAL_CTRL_LIMS,
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


def _control_chart_individual_marks(individual_id, state):
    datum_state = 'datum["%s"]' % state
    # TODO: clean this up
    spaghetti_signal = ('{"title": "spaghetti", "individual_id": '
                        'datum["%s"], "group": datum.groupByVal, "state": '
                        'datum["%s"], "metric": datum.metricVal}' %
                        (individual_id, state))
    return \
        {'type': GROUP,
         'from': {
             # Regroup by "individual_id" column
             'facet': {
                 'name': SPAGHETTIS,
                 'data': INDIVIDUAL,
                 'groupby': individual_id}},
         'marks': [
             {'type': LINE, 'from': {'data': SPAGHETTIS},
              'sort': {'field': datum_state, 'order': ASCENDING_ORDER},
              'encode': {
                  'update': {
                      'strokeWidth': {'signal':
                                      CONTROL_SPAGHET_LINE_THICKNESS_SIGNAL},
                      'x': {'scale': CONTROL_X_SCALE, 'field': state},
                      'y': {'scale': CONTROL_Y_SCALE,
                            'field': {'signal': SIG_METRIC}},
                      'stroke': {'scale': CONTROL_COLOR_SCALE,
                                 'field': {'signal': SIG_GROUP}},
                      'opacity': [
                          {'test': GROUP_TEST,
                           'signal': CONTROL_SPAGHET_LINE_OPACITY_SIGNAL},
                          {'value': OPACITY_000}]}}},
             # Need to add symbols into plot for mouseover
             # https://github.com/vega/vega-tooltip/issues/120
             {'type': SYMBOL,
              'from': {'data': SPAGHETTIS},
              'encode': {
                  'update': {
                      'tooltip': {'signal': spaghetti_signal},
                      'size': {'signal': CONTROL_SPAGHET_SYMBOL_SIZE_SIGNAL},
                      'x': {'scale': CONTROL_X_SCALE, 'field': state},
                      'y': {'scale': CONTROL_Y_SCALE,
                            'field': {'signal': SIG_METRIC}},
                      'stroke': {'scale': CONTROL_COLOR_SCALE,
                                 'field': {'signal': SIG_GROUP}},
                      'fill': {'scale': CONTROL_COLOR_SCALE,
                               'field': {'signal': SIG_GROUP}},
                      'opacity': [
                          {'test': GROUP_TEST,
                           'signal': CONTROL_SPAGHET_SYMBOL_OPACITY_SIGNAL},
                          {'value': OPACITY_000}]}}}]}
