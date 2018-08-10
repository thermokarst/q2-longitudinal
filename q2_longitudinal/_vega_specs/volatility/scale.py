# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from .const import (
    SIG_CTRL_CHART_WIDTH, DAT_GLOBAL_VALS, FLD_MIN_Y, FLD_MAX_Y, FLD_CTRL_CL0,
    FLD_CTRL_CL3, DAT_INDIVIDUAL, SIG_CTRL_CHART_HEIGHT, SIG_COLOR_SCHEME,
    FLD_GROUP_BY, SCL_CTRL_X, SCL_CTRL_Y, SCL_CTRL_COLOR,

    FLD_STATS_MIN, FLD_STATS_MAX, SIG_STATS_CHART_WIDTH, SCL_STATS_X,
    SIG_STATS, DAT_STATS_SCALE, SCL_STATS_Y, DAT_STATS, FLD_STATS_ID,
    SIG_STATS_SORT, SIG_STATS_SORT_DIR, SIG_STATS_CHART_HEIGHT
    )


def render_scales_ctrl(state, yscale):
    return [
        {'name': SCL_CTRL_X,
         'type': 'linear',
         'range': {'signal': SIG_CTRL_CHART_WIDTH},
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
         # TODO: this signal is valid for when we have individual vals in the
         # plot (spaghettis), otherwise we should only use the group means for
         # determining the domain.
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


def render_scales_stats(side):
    side = side['name'].title()
    return [
        {'name': SCL_STATS_X,
         'domain': {'signal': 'if({0}{4} === "Cumulative Average Change", '
                              '   [-1, 1], '
                              '   [data("{1}{4}")[0].{2},'
                              '    data("{1}{4}")[0].{3}])'
                              .format(SIG_STATS, DAT_STATS_SCALE,
                                      FLD_STATS_MIN, FLD_STATS_MAX, side)},
         'range': [0, {'signal': SIG_STATS_CHART_WIDTH}],
         'nice': True},
        {'name': SCL_STATS_Y,
         'type': 'band',
         'domain': {
             'data': DAT_STATS, 'field': FLD_STATS_ID,
             'sort': {'field': {'signal': '%s%s' % (SIG_STATS_SORT, side)},
                      'order': {'signal': '%s%s' % (SIG_STATS_SORT_DIR, side)},
                      'op': 'mean'}},
         'range': [0, {'signal': SIG_STATS_CHART_HEIGHT}]}]
