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

METRIC_SIGNAL2 = 'metric'
GROUP_SIGNAL2 = 'grouper'
FEATURE_TOOLTIP_SIGNAL = 'datum'

SHOW_GLOBAL_MEAN_SIGNAL = 'showGlobalMean'
SHOW_GLOBAL_CONTROL_LIMITS_SIGNAL = 'showGlobalControlLimits'
CONTROL_CHART_HEIGHT_SIGNAL = 'controlChartHeight'
COLOR_SCHEME_SIGNAL = 'colorScheme'

CONTROL_MEAN_LINE_THICKNESS_SIGNAL = 'meanLineThickness'
CONTROL_MEAN_LINE_OPACITY_SIGNAL = 'meanLineOpacity'
CONTROL_MEAN_SYMBOL_SIZE_SIGNAL = 'meanSymbolSize'
CONTROL_MEAN_SYMBOL_OPACITY_SIGNAL = 'meanSymbolOpacity'
CONTROL_SPAGHET_LINE_THICKNESS_SIGNAL = 'spaghettiLineThickness'
CONTROL_SPAGHET_LINE_OPACITY_SIGNAL = 'spaghettiLineOpacity'
CONTROL_SPAGHET_SYMBOL_SIZE_SIGNAL = 'spaghettiSymbolSize'
CONTROL_SPAGHET_SYMBOL_OPACITY_SIGNAL = 'spaghettiSymbolOpacity'

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

DATUM_GROUPER_EXPR = 'datum[grouper]'
DATUM_METRIC_EXPR = 'datum[metric]'
METRIC_VALUE = 'metricVal'
AGGREGATE = 'aggregate'

ROW_1 = 'row1'
ROW_2 = 'row2'
LAYOUT_Y = 'layoutY'
