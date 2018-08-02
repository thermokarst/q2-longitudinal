# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# TODO: ag for these
# TODO: just ship signal names around, not the dict
METRIC_SIGNAL = {'signal': 'metric'}
GROUP_SIGNAL = {'signal': 'grouper'}
FEATURE_STATS_SIGNAL = {'signal': 'feature_stats'}
FEATURE_TOOLTIP_SIGNAL = 'datum'

SHOW_GLOBAL_MEAN_SIGNAL = 'showGlobalMean'
SHOW_GLOBAL_CONTROL_LIMITS_SIGNAL = 'showGlobalControlLimits'
CONTROL_CHART_HEIGHT_SIGNAL = 'controlChartHeight'
COLOR_SCHEME_SIGNAL = 'colorScheme'

# TODO: should this be templated?
GLOBAL_DOMAIN_SIGNAL = ("[min(data('globalVals')[0].cl0,data('globalVals')[0].minY), "  # noqa: E501
                        " max(data('globalVals')[0].cl3,data('globalVals')[0].maxY)]")  # noqa: E501

STROKE_2 = 2
DASH_A = [8, 8]
DASH_B = [6, 2]
OPACITY_000 = 0.0
OPACITY_015 = 0.15
OPACITY_025 = 0.25
OPACITY_100 = 1.0
SIZE_100 = 100

RULE = 'rule'
GROUP = 'group'

GLOBAL_VALS = 'globalVals'
MIN_X = 'minX'
MAX_X = 'maxX'
MEAN = 'mean'
CL0 = 'cl0'
CL1 = 'cl1'
CL2 = 'cl2'
CL3 = 'cl3'
INDIVIDUAL = 'individual'

CONTROL_X_SCALE = 'x'
CONTROL_Y_SCALE = 'y'
CONTROL_COLOR_SCALE = 'color'
LINEAR = 'linear'
WIDTH = 'width'
ORDINAL = 'ordinal'

OPACITY_TEST = "!length(data('selected')) || indata('selected', 'value', datum.value)"  # noqa: E501
FEATURE_STATS_TEST = 'feature_stats === "Cumulative Average Change"'
GROUP_TEST = "!length(data('selected')) || indata('selected', 'value', datum.groupByVal)"  # noqa: E501
ERROR_BAR_TEST = 'showErrorBars && (%s)' % GROUP_TEST

BOTTOM_ORIENT_AXIS = 'bottom'
LEFT_ORIENT_AXIS = 'left'

# COLORS
###############################################################################
TRANSPARENT = 'transparent'

# LEGEND
###############################################################################
CONTROL_SYMBOL_LEGEND = 'legendSymbol'
CONTROL_LABEL_LEGEND = 'labelSymbol'
