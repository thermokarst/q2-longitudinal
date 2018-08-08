# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .const import (
    DAT_GLOBAL_VALS, FLD_MIN_X, FLD_MAX_X, FLD_CTRL_MEAN, FLD_CTRL_CL0,
    FLD_CTRL_CL1, FLD_CTRL_CL2, FLD_CTRL_CL3, SCL_CTRL_X, SCL_CTRL_Y,
    SIG_SHOW_GLOBAL_MEAN, STY_STROKE_2, STY_DASH_A, STY_DASH_B,
    SIG_SHOW_GLOBAL_CTRL_LIMS, SIG_WIDTH, SIG_CTRL_CHART_HEIGHT, DAT_SERIES,
    AGG_BY_DATA, GROUP_BY_VALUE, LINE, ASCENDING_ORDER, SCL_CTRL_COLOR,
    SIG_CTRL_MEAN_LINE_THICKNESS, SIG_CTRL_MEAN_SYMBOL_SIZE, GROUP_TEST,
    SIG_CTRL_MEAN_LINE_OPACITY, SIG_CTRL_MEAN_SYMBOL_OPACITY, FLD_CTRL_CI0,
    FLD_CTRL_CI1, ERROR_BAR_TEST, DAT_SPAGHETTIS, DAT_INDIVIDUAL,
    SIG_CTRL_SPG_LINE_THICKNESS, SIG_METRIC, SIG_GROUP,
    SIG_CTRL_SPG_LINE_OPACITY, SIG_CTRL_SPG_SYMBOL_SIZE,
    SIG_CTRL_SPG_SYMBOL_OPACITY)


def _control_chart_subplot(yscale):
    return \
        {'description': 'Control Chart',
         'name': 'spaghetti',
         'type': 'group',
         'encode': {
             'enter': {
                 'y': {'value': 0},
                 'width': {'signal': SIG_WIDTH},
                 'height': {'signal': SIG_CTRL_CHART_HEIGHT},
                }},
         'marks': [],
         'scales': [],
         'axes': [],
         'legends': []}


def _control_chart_global_marks():
    return [
        # Global Mean
        {'type': 'rule',
         'from': {'data': DAT_GLOBAL_VALS},
         'encode': {
             'update': {
                 'strokeWidth': {'value': STY_STROKE_2},
                 'x': {'scale': SCL_CTRL_X, 'field': FLD_MIN_X},
                 'x2': {'scale': SCL_CTRL_X, 'field': FLD_MAX_X},
                 'y': {'scale': SCL_CTRL_Y, 'field': FLD_CTRL_MEAN},
                 'strokeOpacity': [
                     {'test': SIG_SHOW_GLOBAL_MEAN, 'value': 1.0},
                     {'value': 0.0}]}}},
        # Global confidence limit, -3x std dev
        {'type': 'rule',
         'from': {'data': DAT_GLOBAL_VALS},
         'encode': {
             'update': {
                 'strokeWidth': {'value': STY_STROKE_2},
                 'strokeDash': {'value': STY_DASH_A},
                 'x': {'scale': SCL_CTRL_X, 'field': FLD_MIN_X},
                 'x2': {'scale': SCL_CTRL_X, 'field': FLD_MAX_X},
                 'y': {'scale': SCL_CTRL_Y, 'field': FLD_CTRL_CL0},
                 'strokeOpacity': [
                     {'test': SIG_SHOW_GLOBAL_CTRL_LIMS,
                      'value': 1.0},
                     {'value': 0.0},
                 ]}}},
        # Global confidence limit, -2x std dev
        {'type': 'rule',
         'from': {'data': DAT_GLOBAL_VALS},
         'encode': {
             'update': {
                 'strokeWidth': {'value': STY_STROKE_2},
                 'strokeDash': {'value': STY_DASH_B},
                 'x': {'scale': SCL_CTRL_X, 'field': FLD_MIN_X},
                 'x2': {'scale': SCL_CTRL_X, 'field': FLD_MAX_X},
                 'y': {'scale': SCL_CTRL_Y, 'field': FLD_CTRL_CL1},
                 'strokeOpacity': [
                     {'test': SIG_SHOW_GLOBAL_CTRL_LIMS,
                      'value': 1.0},
                     {'value': 0.0},
                 ]}}},
        # Global confidence limit, +2x std dev
        {'type': 'rule',
         'from': {'data': DAT_GLOBAL_VALS},
         'encode': {
             'update': {
                 'strokeWidth': {'value': STY_STROKE_2},
                 'strokeDash': {'value': STY_DASH_A},
                 'x': {'scale': SCL_CTRL_X, 'field': FLD_MIN_X},
                 'x2': {'scale': SCL_CTRL_X, 'field': FLD_MAX_X},
                 'y': {'scale': SCL_CTRL_Y, 'field': FLD_CTRL_CL2},
                 'strokeOpacity': [
                     {'test': SIG_SHOW_GLOBAL_CTRL_LIMS,
                      'value': 1.0},
                     {'value': 0.0},
                 ]}}},
        # Global confidence limit, +3x std dev
        {'type': 'rule',
         'from': {'data': DAT_GLOBAL_VALS},
         'encode': {
             'update': {
                 'strokeWidth': {'value': STY_STROKE_2},
                 'strokeDash': {'value': STY_DASH_B},
                 'x': {'scale': SCL_CTRL_X, 'field': FLD_MIN_X},
                 'x2': {'scale': SCL_CTRL_X, 'field': FLD_MAX_X},
                 'y': {'scale': SCL_CTRL_Y, 'field': FLD_CTRL_CL3},
                 'strokeOpacity': [
                     {'test': SIG_SHOW_GLOBAL_CTRL_LIMS,
                      'value': 1.0},
                     {'value': 0.0},
                 ]}}}]


def _control_chart_grouped_marks(state):
    datum_state = "datum['%s']" % state
    # TODO: Clean this up
    mean_signal = ('{"title": "group mean", "group": datum.groupByVal,'
                   ' "state": datum["%s"], "count": datum.count,'
                   ' "mean": datum.%s, "ci0": datum.%s, "ci1": datum.%s}'
                   % (state, FLD_CTRL_MEAN, FLD_CTRL_CI0, FLD_CTRL_CI1))
    return [
        {'type': 'group',
         'from': {
             # Regroup by "group" column
             'facet': {
                 'name': DAT_SERIES,
                 'data': AGG_BY_DATA,
                 'groupby': GROUP_BY_VALUE}},
         'marks': [
             # Per-group mean lines
             {'type': LINE,
              'from': {'data': DAT_SERIES},
              'sort': {'field': datum_state, 'order': ASCENDING_ORDER},
              'encode': {
                  'update': {
                      'x': {'scale': SCL_CTRL_X, 'field': state},
                      'y': {'scale': SCL_CTRL_Y, 'field': FLD_CTRL_MEAN},
                      'stroke': {'scale': SCL_CTRL_COLOR,
                                 'field': GROUP_BY_VALUE},
                      'strokeWidth': {'signal':
                                      SIG_CTRL_MEAN_LINE_THICKNESS},
                      'opacity': [
                          {'test': GROUP_TEST,
                           'signal': SIG_CTRL_MEAN_LINE_OPACITY},
                          {'value': 0.0},
                      ]}}},
             # per-group symbols
             {'type': 'symbol',
              'from': {'data': DAT_SERIES},
              'encode': {
                  'update': {
                      'tooltip': {'signal': mean_signal},
                      'x': {'scale': SCL_CTRL_X, 'field': state},
                      'y': {'scale': SCL_CTRL_Y, 'field': FLD_CTRL_MEAN},
                      'stroke': {'scale': SCL_CTRL_COLOR,
                                 'field': GROUP_BY_VALUE},
                      'fill': {'scale': SCL_CTRL_COLOR,
                               'field': GROUP_BY_VALUE},
                      'size': {'signal': SIG_CTRL_MEAN_SYMBOL_SIZE},
                      'opacity': [
                          {'test': GROUP_TEST,
                           'signal': SIG_CTRL_MEAN_SYMBOL_OPACITY},
                          {'value': 0.0}]}}},
             # Per-group error bars
             {'type': 'rect',
              'from': {'data': DAT_SERIES},
              'encode': {
                  'update': {
                      'width': {'value': 2.0},
                      'x': {'scale': SCL_CTRL_X, 'field': state,
                            'band': 0.5},
                      'y': {'scale': SCL_CTRL_Y, 'field': FLD_CTRL_CI0},
                      'y2': {'scale': SCL_CTRL_Y, 'field': FLD_CTRL_CI1},
                      'fill': {'scale': SCL_CTRL_COLOR,
                               'field': GROUP_BY_VALUE},
                      'opacity': [
                          {'test': ERROR_BAR_TEST, 'value': 1.0},
                          {'value': 0.0}]}}}]}]


def _control_chart_individual_marks(individual_id, state):
    datum_state = 'datum["%s"]' % state
    # TODO: clean this up
    spaghetti_signal = ('{"title": "spaghetti", "individual_id": '
                        'datum["%s"], "group": datum.groupByVal, "state": '
                        'datum["%s"], "metric": datum.metricVal}' %
                        (individual_id, state))
    return \
        {'type': 'group',
         'from': {
             # Regroup by "individual_id" column
             'facet': {
                 'name': DAT_SPAGHETTIS,
                 'data': DAT_INDIVIDUAL,
                 'groupby': individual_id}},
         'marks': [
             {'type': LINE, 'from': {'data': DAT_SPAGHETTIS},
              'sort': {'field': datum_state, 'order': ASCENDING_ORDER},
              'encode': {
                  'update': {
                      'strokeWidth': {'signal':
                                      SIG_CTRL_SPG_LINE_THICKNESS},
                      'x': {'scale': SCL_CTRL_X, 'field': state},
                      'y': {'scale': SCL_CTRL_Y,
                            'field': {'signal': SIG_METRIC}},
                      'stroke': {'scale': SCL_CTRL_COLOR,
                                 'field': {'signal': SIG_GROUP}},
                      'opacity': [
                          {'test': GROUP_TEST,
                           'signal': SIG_CTRL_SPG_LINE_OPACITY},
                          {'value': 0.0}]}}},
             # Need to add symbols into plot for mouseover
             # https://github.com/vega/vega-tooltip/issues/120
             {'type': 'symbol',
              'from': {'data': DAT_SPAGHETTIS},
              'encode': {
                  'update': {
                      'tooltip': {'signal': spaghetti_signal},
                      'size': {'signal': SIG_CTRL_SPG_SYMBOL_SIZE},
                      'x': {'scale': SCL_CTRL_X, 'field': state},
                      'y': {'scale': SCL_CTRL_Y,
                            'field': {'signal': SIG_METRIC}},
                      'stroke': {'scale': SCL_CTRL_COLOR,
                                 'field': {'signal': SIG_GROUP}},
                      'fill': {'scale': SCL_CTRL_COLOR,
                               'field': {'signal': SIG_GROUP}},
                      'opacity': [
                          {'test': GROUP_TEST,
                           'signal': SIG_CTRL_SPG_SYMBOL_OPACITY},
                          {'value': 0.0}]}}}]}
