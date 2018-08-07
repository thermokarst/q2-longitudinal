# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .const import (
    INDIVIDUAL, FORMULA, GROUP_BY_VALUE, DATUM_METRIC_EXPR, DATUM_GROUPER_EXPR,
    METRIC_VALUE, GLOBAL_VALS, AGGREGATE, MEAN, MIN, MAX, STDEV,
    METRIC_SIGNAL, MIN_X, MAX_X, MIN_Y, MAX_Y, CL0, CL1, CL2, CL3, EXT,
    AGG_BY_DATA, CI0, CI1, COUNT, SELECTED)


def _control_chart_data(control_chart_data, state):
    return [
        {'name': INDIVIDUAL,
         'values': control_chart_data.to_dict('record'),
         'transform': [
             {'type': FORMULA, 'as': GROUP_BY_VALUE,
              'expr': DATUM_GROUPER_EXPR},
             {'type': FORMULA, 'as': METRIC_VALUE,
              'expr': DATUM_METRIC_EXPR}]},
        {'name': GLOBAL_VALS,
         'source': INDIVIDUAL,
         'transform': [
             {'type': AGGREGATE,
              'ops': [MEAN, MIN, MAX, STDEV, MIN, MAX],
              'fields': [
                  {'signal': METRIC_SIGNAL},
                  state,
                  state,
                  {'signal': METRIC_SIGNAL},
                  {'signal': METRIC_SIGNAL},
                  {'signal': METRIC_SIGNAL}],
              'as': [MEAN, MIN_X, MAX_X, STDEV, MIN_Y, MAX_Y]},
             # TODO: clean up these expressions
             {'type': FORMULA, 'as': CL0,
              'expr': 'datum.mean - (3 * datum.stdev)'},
             {'type': FORMULA, 'as': CL1,
              'expr': 'datum.mean - (2 * datum.stdev)'},
             {'type': FORMULA, 'as': CL2,
              'expr': 'datum.mean + (2 * datum.stdev)'},
             {'type': FORMULA, 'as': CL3,
              'expr': 'datum.mean + (3 * datum.stdev)'},
             {'type': FORMULA, 'as': EXT,
              'expr': '[datum.cl0, datum.cl3]'}]},
        {'name': AGG_BY_DATA,
         'source': INDIVIDUAL,
         'transform': [
             {'type': AGGREGATE,
              'groupby': [GROUP_BY_VALUE, state],
              # TODO: parameterize these intervals
              # I don't see an easy way at the moment to define
              # your own confidence interval in vega.
              'ops': [MEAN, CI0, CI1, COUNT],
              'fields': [
                  {'signal': METRIC_SIGNAL},
                  {'signal': METRIC_SIGNAL},
                  {'signal': METRIC_SIGNAL},
                  {'signal': METRIC_SIGNAL}],
              'as': [MEAN, CI0, CI1, COUNT]}]},
        # These are just UI state vars to keep track of what has been clicked
        # in the legend.
        {'name': SELECTED,
         'on': [
             {'trigger': 'clear', 'remove': True},
             {'trigger': '!shift', 'remove': True},
             {'trigger': '!shift && clicked', 'insert': 'clicked'},
             {'trigger': 'shift && clicked', 'toggle': 'clicked'}]}]
