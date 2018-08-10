# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .const import SCL_CTRL_X, SCL_CTRL_Y, SCL_STATS_X, SIG_STATS


def render_axes_ctrl(state):
    return [
        {'orient': 'bottom', 'scale': SCL_CTRL_X,
         'title': state},
        {'orient': 'left', 'scale': SCL_CTRL_Y,
         'title': 'Metric Column'}]


def render_axes_stats(side):
    return [
        {'orient': 'top', 'scale': SCL_STATS_X,
         'title': {'signal': '%s%s' % (SIG_STATS, side['name'].title())}}]
