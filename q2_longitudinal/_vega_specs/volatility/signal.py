# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .const import (
    SIG_METRIC, SIG_GROUP, SIG_SHOW_GLOBAL_MEAN, SIG_SHOW_GLOBAL_CTRL_LIMS,
    SIG_CTRL_CHART_HEIGHT, SIG_COLOR_SCHEME, SIG_CTRL_MEAN_LINE_THICKNESS,
    SIG_CTRL_MEAN_LINE_OPACITY, SIG_CTRL_MEAN_SYMBOL_SIZE,
    SIG_CTRL_MEAN_SYMBOL_OPACITY, SIG_CTRL_SPG_LINE_THICKNESS,
    SIG_CTRL_SPG_LINE_OPACITY, SIG_CTRL_SPG_SYMBOL_SIZE,
    SIG_CTRL_SPG_SYMBOL_OPACITY, SIG_WIDTH, SIG_HEIGHT, SIG_SHOW_ERROR_BARS,
    LEG_CTRL_SYMBOL
    )


def _volatility_signals(features_chart_data, default_group, group_columns,
                        default_metric, metric_columns):
    return [
        # LAYOUT/DIMENSIONS
        {'name': SIG_CTRL_CHART_HEIGHT, 'value': 400},
        # TODO: you don't belong in here
        {'name': 'importancesChartHeight',
         # TODO: make this a vega expression
         'value': 10 * len(features_chart_data.index)},
        {'name': SIG_HEIGHT,
         'update': '%s + importancesChartHeight' % SIG_CTRL_CHART_HEIGHT},
        {'name': 'halfWidth', 'update': 'width / 2'},
        {'name': SIG_WIDTH, 'value': '', 'bind': {'input': 'text'},
         'on': [{'events': {'source': 'window', 'type': 'resize'},
                 'update': 'containerSize()[0]'}]},

        # UI WIDGETS
        {'name': SIG_SHOW_ERROR_BARS, 'value': False,
         'bind': {'input': 'checkbox', 'element': '#toggle-error-bars'}},
        {'name': SIG_GROUP,
         'value': default_group,
         'bind': {'input': 'select', 'element': '#group-column',
                  'options': group_columns}},
        {'name': SIG_METRIC, 'value': default_metric,
         'bind': {'input': 'select', 'element': '#metric-column',
                  'options': metric_columns},
         # TODO: Is this a problem to leave this here?
         'on': [
             # I couldn't get event merging to work correctly here.
             {'events': '@feature_importances:click',
              'update': 'datum.id', 'force': True},
             {'events': '@descriptive_stats:click',
              'update': 'datum.id', 'force': True}]},
        {'name': SIG_SHOW_GLOBAL_MEAN, 'value': False,
         'bind': {'input': 'checkbox', 'element': '#toggle-global-mean'}},
        {'name': SIG_SHOW_GLOBAL_CTRL_LIMS, 'value': False,
         'bind': {'input': 'checkbox',
                  'element': '#toggle-global-control-limits'}},
        {'name': SIG_CTRL_MEAN_LINE_THICKNESS, 'value': 3,
         'bind': {'input': 'range', 'min': 0.1, 'max': 10, 'step': 0.1,
                  'element': '#mean-line-thickness'}},
        {'name': SIG_CTRL_MEAN_LINE_OPACITY, 'value': 1.0,
         'bind': {'input': 'range', 'min': 0.0, 'max': 1.0, 'step': 0.01,
                  'element': '#mean-line-opacity'}},
        {'name': SIG_CTRL_MEAN_SYMBOL_SIZE, 'value': 50.0,
         'bind': {'input': 'range', 'min': 0.0, 'max': 500.0, 'step': 1.0,
                  'element': '#mean-symbol-size'}},
        {'name': SIG_CTRL_MEAN_SYMBOL_OPACITY, 'value': 0.0,
         'bind': {'input': 'range', 'min': 0.0, 'max': 1.0, 'step': 0.01,
                  'element': '#mean-symbol-opacity'}},
        {'name': SIG_COLOR_SCHEME, 'value': 'category10',
         'bind': {'input': 'select', 'element': '#color-scheme',
                  'options': ['accent', 'category10', 'category20',
                              'category20b', 'category20c', 'dark2', 'paired',
                              'pastel1', 'pastel2', 'set1', 'set2', 'set3',
                              'tableau10', 'tableau20']}},

        # LEGEND EVENTS
        {'name': 'clear', 'value': True,
         'on': [{'events': 'mouseup[!event.item]', 'update': 'true',
                 'force': True}]},
        {'name': 'shift', 'value': False,
         'on': [{'events': '@%s:click, @legendLabel:click' %
                           LEG_CTRL_SYMBOL,
                 'update': 'event.shiftKey', 'force': True}]},
        {'name': 'clicked', 'value': None,
         'on': [{'events': '@%s:click, @legendLabel:click' %
                           LEG_CTRL_SYMBOL,
                 'update': '{value: datum.value}', 'force': True}]},
    ]


def _spaghetti_signals():
    return [
        {'name': SIG_CTRL_SPG_LINE_THICKNESS, 'value': 0.5,
         'bind': {'input': 'range', 'min': 0.1, 'max': 10, 'step': 0.1,
                  'element': '#spaghetti-line-thickness'}},
        {'name': SIG_CTRL_SPG_LINE_OPACITY, 'value': 0.5,
         'bind': {'input': 'range', 'min': 0.0, 'max': 1.0, 'step': 0.01,
                  'element': '#spaghetti-line-opacity'}},
        {'name': SIG_CTRL_SPG_SYMBOL_SIZE, 'value': 50.0,
         'bind': {'input': 'range', 'min': 0.0, 'max': 500.0, 'step': 1.0,
                  'element': '#spaghetti-symbol-size'}},
        {'name': SIG_CTRL_SPG_SYMBOL_OPACITY, 'value': 0.0,
         'bind': {'input': 'range', 'min': 0.0, 'max': 1.0, 'step': 0.01,
                  'element': '#spaghetti-symbol-opacity'}}]


#         # TODO: only add this if feature volatility
#         {
#             'name': 'feature_stats',
#             'value': 'Cumulative Average Change',
#             'bind': {
#                 'input': 'select',
#                 'element': '#feature-stats',
#                 'options': [
#                     'Cumulative Average Change',
#                     'Variance',
#                     'Mean',
#                     'Median',
#                     'Standard Deviation',
#                     'CV (%)',
#                 ],
#             },
#         },
#         {
#             'name': 'feature_sort',
#             'value': 'importance',
#             'bind': {
#                 'input': 'select',
#                 'element': '#sort-features',
#                 'options': [
#                     'importance',
#                     'Cumulative Avg Decrease',
#                     'Cumulative Avg Increase',
#                     'Variance',
#                     'Mean',
#                     'Median',
#                     'Standard Deviation',
#                     'CV (%)',
#                 ],
#             },
#         },
#         {
#             'name': 'sort_direction',
#             'value': 'descending',
#             'bind': {
#                 'input': 'select',
#                 'element': '#sort-direction',
#                 'options': [
#                     'ascending',
#                     'descending',
#                 ],
#             },
#         },
#         # END TODO
