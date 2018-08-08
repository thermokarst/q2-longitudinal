# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# Some thoughts on "rules"
# 1. These constants should be used for identifiers only (don't worry about
#    values or things like mark types). The exception is when we are
#    coordinating styles across multiple components.
# 2. Names should be prefixed with a 3 character abbreviation:
#    SIG - signal
#    SCL - scale
#    DAT - data
#    FLD - field
#    TST - test
#    EXP - expression
#    STY - style
#    LEG - legend

# TODO: ag for these
# TODO: revise the json names

# SIGNALS
###############################################################################
SIG_METRIC = 'metric'
SIG_GROUP = 'grouper'
SIG_SHOW_GLOBAL_MEAN = 'showGlobalMean'
SIG_SHOW_GLOBAL_CTRL_LIMS = 'showGlobalControlLimits'
SIG_SHOW_ERROR_BARS = 'showErrorBars'
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
SIG_WIDTH = 'width'  # this is a special signal in vega
SIG_HEIGHT = 'height'  # this is a special signal in vega

# STYLES
###############################################################################
STY_STROKE_2 = 2
STY_DASH_A = [8, 8]
STY_DASH_B = [6, 2]

# DATA
###############################################################################
DAT_GLOBAL_VALS = 'globalVals'
DAT_INDIVIDUAL = 'individual'
DAT_SERIES = 'series'
DAT_SPAGHETTIS = 'spaghettis'
DAT_SELECTED = 'selected'

# FIELDS
###############################################################################
# TODO: These minx/maxx should be updated to mention they are CTRL plot
FLD_MIN_X = 'minX'
FLD_MAX_X = 'maxX'
FLD_MIN_Y = 'minY'
FLD_MAX_Y = 'maxY'
FLD_CTRL_MEAN = 'mean'
FLD_CTRL_MIN = 'min'
FLD_CTRL_STDEV = 'stdev'
FLD_CTRL_COUNT = 'count'
FLD_CTRL_CL0 = 'cl0'
FLD_CTRL_CL1 = 'cl1'
FLD_CTRL_CL2 = 'cl2'
FLD_CTRL_CL3 = 'cl3'
FLD_CTRL_CI0 = 'ci0'
FLD_CTRL_CI1 = 'ci1'
FLD_CTRL_EXT = 'ext'

# SCALES
###############################################################################
SCL_CTRL_X = 'x'
SCL_CTRL_Y = 'y'
SCL_CTRL_COLOR = 'color'

# TESTS
###############################################################################
TST_OPACITY = "!length(data('{0}')) || indata('{0}', 'value', datum.value)".format(DAT_SELECTED)  # noqa: E501
TST_GROUP = "!length(data('{0}')) || indata('{0}', 'value', datum.groupByVal)".format(DAT_SELECTED)  # noqa: E501

###############################################################################
###############################################################################
# NEEDS TO BE EVALUATED
###############################################################################
###############################################################################

# COLORS
###############################################################################

# LEGEND
###############################################################################
LEG_CTRL_SYMBOL = 'legendSymbol'
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
