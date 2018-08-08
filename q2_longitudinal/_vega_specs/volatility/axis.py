# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .const import SIG_METRIC, SCL_CTRL_X, SCL_CTRL_Y


def _control_chart_axes(state):
    return [
        {'orient': 'bottom', 'scale': SCL_CTRL_X,
         'title': state},
        {'orient': 'left', 'scale': SCL_CTRL_Y,
         # TODO: for feature volatility, include the fact
         # that this is the relative abundance
         'title': {'signal': SIG_METRIC}}]


# TODO: placeholder for feature vol axes
