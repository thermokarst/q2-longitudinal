# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# Some thoughts on "rules"
# 1. These constants should be used for identifiers only (don't worry about
#    values or things like mark types).
# 2. Names should be prefixed with a 3 character abbreviation:
#    SIG - signal
#    SCL - scale
#    DAT - data
#    FLD - field
#    TST - test
#    EXP - expression

# TODO: ag for these

# SIGNALS
###############################################################################
SIG_METRIC = 'metric'
SIG_GROUP = 'grouper'
SIG_SHOW_GLOBAL_MEAN = 'showGlobalMean'
SIG_SHOW_GLOBAL_CTRL_LIMS = 'showGlobalControlLimits'
SIG_COLOR_SCHEME = 'colorScheme'
SIG_CTRL_CHART_HEIGHT = 'controlChartHeight'
SIG_CTRL_MEAN_LINE_THICKNESS = 'meanLineThickness'
SIG_CTRL_MEAN_LINE_OPACITY = 'meanLineOpacity'
SIG_CTRL_MEAN_SYMBOL_SIZE = 'meanSymbolSize'
SIG_CTRL_MEAN_SYMBOL_OPACITY = 'meanSymbolOpacity'
SIG_CTRL_SPG_LINE_THICKNESS = 'spaghettiLineThickness'
SIG_CTRL_SPG_LINE_OPACITY = 'spaghettiLineOpacity'
SIG_CTRL_SPG_SYMBOL_SIZE = 'spaghettiSymbolSize'
SIG_CTRL_SPG_SYMBOL_OPACITY = 'spaghettiSymbolOpacity'

# TODO: should this be templated?
GLOBAL_DOMAIN_SIGNAL = ("[min(data('globalVals')[0].cl0,data('globalVals')[0].minY), "  # noqa: E501
                        " max(data('globalVals')[0].cl3,data('globalVals')[0].maxY)]")  # noqa: E501

STROKE_2 = 2
RECT_2 = 2.0
DASH_A = [8, 8]
DASH_B = [6, 2]
OPACITY_000 = 0.0
OPACITY_015 = 0.15
OPACITY_025 = 0.25
OPACITY_100 = 1.0
SIZE_100 = 100
BAND_050 = 0.5

RULE = 'rule'
RECT = 'rect'
GROUP = 'group'
SYMBOL = 'symbol'
FORMULA = 'formula'

GLOBAL_VALS = 'globalVals'
MIN_X = 'minX'
MAX_X = 'maxX'
MIN_Y = 'minY'
MAX_Y = 'maxY'
MEAN = 'mean'
MIN = 'min'
MAX = 'max'
STDEV = 'stdev'
CL0 = 'cl0'
CL1 = 'cl1'
CL2 = 'cl2'
CL3 = 'cl3'
CI0 = 'ci0'
CI1 = 'ci1'
EXT = 'ext'
INDIVIDUAL = 'individual'
SERIES = 'series'
SPAGHETTIS = 'spaghettis'

CONTROL_X_SCALE = 'x'
CONTROL_Y_SCALE = 'y'
CONTROL_COLOR_SCALE = 'color'
LINEAR = 'linear'
WIDTH = 'width'
HEIGHT = 'height'
ORDINAL = 'ordinal'
BAND = 'band'

SELECTED = 'selected'
COUNT = 'count'

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

AGG_BY_DATA = 'aggBy'
GROUP_BY_VALUE = 'groupByVal'

LINE = 'line'
ASCENDING_ORDER = 'ascending'

METRIC_VALUE = 'metricVal'
AGGREGATE = 'aggregate'

ROW_1 = 'row1'
ROW_2 = 'row2'
LAYOUT_Y = 'layoutY'
