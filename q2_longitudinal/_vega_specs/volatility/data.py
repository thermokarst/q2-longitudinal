# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .const import (
    INDIVIDUAL, GROUP_BY_VALUE, METRIC_VALUE, DAT_GLOBAL_VALS, AGGREGATE,
    FLD_CTRL_MEAN, FLD_CTRL_STDEV, SIG_METRIC, SIG_GROUP, FLD_MIN_X, FLD_MAX_X,
    FLD_MIN_Y, FLD_MAX_Y, FLD_CTRL_CL0, FLD_CTRL_CL1, FLD_CTRL_CL2,
    FLD_CTRL_CL3, EXT, AGG_BY_DATA, CI0, CI1, COUNT, SELECTED)


def _control_chart_data(control_chart_data, state):
    return [
        {'name': INDIVIDUAL,
         'values': control_chart_data.to_dict('record'),
         'transform': [
             {'type': 'formula', 'as': GROUP_BY_VALUE,
              'expr': 'datum[%s]' % SIG_GROUP},
             {'type': 'formula', 'as': METRIC_VALUE,
              'expr': 'datum[%s]' % SIG_METRIC}]},
        {'name': DAT_GLOBAL_VALS,
         'source': INDIVIDUAL,
         'transform': [
             {'type': AGGREGATE,
              'ops': ['mean', 'min', 'max', 'stdev', 'min', 'max'],
              'fields': [
                  {'signal': SIG_METRIC},
                  state,
                  state,
                  {'signal': SIG_METRIC},
                  {'signal': SIG_METRIC},
                  {'signal': SIG_METRIC}],
              'as': [FLD_CTRL_MEAN, FLD_MIN_X, FLD_MAX_X, FLD_CTRL_STDEV,
                     FLD_MIN_Y, FLD_MAX_Y]},
             # TODO: clean up these expressions
             {'type': 'formula', 'as': FLD_CTRL_CL0,
              'expr': 'datum.%s - (3 * datum.%s)' % (FLD_CTRL_MEAN,
                                                     FLD_CTRL_STDEV)},
             {'type': 'formula', 'as': FLD_CTRL_CL1,
              'expr': 'datum.%s - (2 * datum.%s)' % (FLD_CTRL_MEAN,
                                                     FLD_CTRL_STDEV)},
             {'type': 'formula', 'as': FLD_CTRL_CL2,
              'expr': 'datum.%s + (2 * datum.%s)' % (FLD_CTRL_MEAN,
                                                     FLD_CTRL_STDEV)},
             {'type': 'formula', 'as': FLD_CTRL_CL3,
              'expr': 'datum.%s + (3 * datum.%s)' % (FLD_CTRL_MEAN,
                                                     FLD_CTRL_STDEV)},
             {'type': 'formula', 'as': EXT,
              'expr': '[datum.%s, datum.%s]' % (FLD_CTRL_CL0, FLD_CTRL_CL3)}]},
        {'name': AGG_BY_DATA,
         'source': INDIVIDUAL,
         'transform': [
             {'type': AGGREGATE,
              'groupby': [GROUP_BY_VALUE, state],
              # TODO: parameterize these intervals
              # I don't see an easy way at the moment to define
              # your own confidence interval in vega.
              'ops': ['mean', 'ci0', 'ci1', 'count'],
              'fields': [
                  {'signal': SIG_METRIC},
                  {'signal': SIG_METRIC},
                  {'signal': SIG_METRIC},
                  {'signal': SIG_METRIC}],
              'as': [FLD_CTRL_MEAN, CI0, CI1, COUNT]}]},
        # These are just UI state vars to keep track of what has been clicked
        # in the legend.
        {'name': SELECTED,
         'on': [
             {'trigger': 'clear', 'remove': True},
             {'trigger': '!shift', 'remove': True},
             {'trigger': '!shift && clicked', 'insert': 'clicked'},
             {'trigger': 'shift && clicked', 'toggle': 'clicked'}]}]
