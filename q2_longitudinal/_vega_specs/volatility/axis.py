# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .const import (SIG_METRIC, CONTROL_X_SCALE, CONTROL_Y_SCALE,
                    BOTTOM_ORIENT_AXIS, LEFT_ORIENT_AXIS)


def _control_chart_axes(state):
    return [
        {'orient': BOTTOM_ORIENT_AXIS, 'scale': CONTROL_X_SCALE,
         'title': state},
        {'orient': LEFT_ORIENT_AXIS, 'scale': CONTROL_Y_SCALE,
         # TODO: for feature volatility, include the fact
         # that this is the relative abundance
         'title': {'signal': SIG_METRIC}}]


# TODO: placeholder for feature vol axes
