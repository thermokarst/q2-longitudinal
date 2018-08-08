# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from .const import (
    DAT_GLOBAL_VALS, FLD_MIN_Y, FLD_MAX_Y, FLD_CTRL_CL0, FLD_CTRL_CL3,
    FLD_GROUP_BY, SCL_CTRL_X, SIG_WIDTH, SCL_CTRL_Y, SCL_CTRL_COLOR,
    DAT_INDIVIDUAL, SIG_CTRL_CHART_HEIGHT, SIG_COLOR_SCHEME)


def _control_chart_subplot_scales(state, yscale):
    return [
        {'name': SCL_CTRL_X,
         'type': 'linear',
         'range': SIG_WIDTH,
         'nice': True,
         'domain': {
             'data': DAT_INDIVIDUAL,
             'field': state,
             'sort': True,
         }},
        {'name': SCL_CTRL_Y,
         # Signal registration on this param is currently
         # blocked by https://github.com/vega/vega/issues/525,
         # which is why this setting is still a QIIME 2 param to
         # this viz.
         'type': yscale,
         'range': [{'signal': SIG_CTRL_CHART_HEIGHT}, 0],
         'nice': True,
         'domain': {'signal': "[min(data('{0}')[0].{3},"
                              "     data('{0}')[0].{1}),"
                              " max(data('{0}')[0].{4},"
                              "     data('{0}')[0].{2})]".format(
                                  DAT_GLOBAL_VALS, FLD_MIN_Y, FLD_MAX_Y,
                                  FLD_CTRL_CL0, FLD_CTRL_CL3),
                    'sort': True}},
        {'name': SCL_CTRL_COLOR,
         'type': 'ordinal',
         'range': {'scheme': {'signal': SIG_COLOR_SCHEME}},
         'domain': {'data': DAT_INDIVIDUAL, 'field': FLD_GROUP_BY}}]
