# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


# STICKING THIS HERE FOR NOW
#     if is_feat_vol_plot:
#         importances_subplot = {
#             'description': 'Feature Importances',
#             'name': 'importance_chart',
#             'type': 'group',
#             'encode': {
#                 'enter': {
#                     'y': {
#                         'signal': 'controlChartHeight',
#                         'offset': 75,
#                     },
#                     'width': {
#                         'signal': 'halfWidth - 25',
#                     },
#                     'height': {
#                         'signal': 'importancesChartHeight',
#                     },
#                 },
#             },
#             'scales': [
#                 # TODO: sort y axis
#                 # TODO: stop dupe
#                 {
#                     'name': 'y',
#                     'type': 'band',
#                     'domain': {
#                         'data': 'features',
#                         'field': 'id',
#                         'sort': {
#                             'field': {
#                                 'signal': 'feature_sort',
#                             },
#                             'order': {
#                                 'signal': 'sort_direction',
#                             },
#                             'op': 'mean',
#                         },
#                     },
#                     'range': [
#                         0,
#                         {
#                             'signal': 'importancesChartHeight',
#                         },
#                     ],
#                 },
#                 {
#                     'name': 'x',
#                     'domain': {
#                         'data': 'features',
#                         'field': 'importance',
#                     },
#                     'nice': True,
#                     'range': [
#                         0,
#                         {
#                             'signal': 'halfWidth - 25',
#                         },
#                     ],
#                 },
#             ],
#             'axes': [
#                 {
#                     'orient': 'top',
#                     'scale': 'x',
#                     'title': 'Importance',
#                 },
#             ],
#             'marks': [
#                 # TODO: add background highlight
#                 # TODO: JS variable name style
#                 {
#                     'name': 'feature_importances',
#                     'type': 'rect',
#                     'from': {
#                         'data': 'features',
#                     },
#                     'encode': {
#                         'enter': {
#                             'x': {
#                                 'scale': 'x',
#                                 'value': 0,
#                             },
#                             'width': {
#                                 'scale': 'x',
#                                 'field': 'importance',
#                             },
#                             'height': {
#                                 'scale': 'y',
#                                 'band': 1,
#                             },
#                             'fill': {
#                                 'value': '#AAAAAA',
#                             },
#                         },
#                         'update': {
#                             'y': {
#                                 'scale': 'y',
#                                 'field': 'id',
#                             },
#                             'fill': [
#                                 {
#                                     'test': 'metric === datum.id',
#                                     'value': '#FF0000',
#                                 },
#                                 {
#                                     'value': '#AAAAAA',
#                                 }
#                             ],
#                         },
#                     },
#                 },
#             ],
#         }
#         spec['marks'].append(importances_subplot)
#         first_diff_subplot = {
#             # TODO: make this dynamic?
#             'description': '',
#             'name': '',
#             'type': 'group',
#             'encode': {
#                 'enter': {
#                     'x': {
#                         'signal': 'halfWidth',
#                         'offset': 25,
#                     },
#                     'y': {
#                         'signal': 'controlChartHeight',
#                         'offset': 75,
#                     },
#                     'width': {
#                         'signal': 'halfWidth - 25',
#                     },
#                     'height': {
#                         'signal': 'importancesChartHeight',
#                     },
#                 },
#             },
#             'scales': [
#                 # TODO: sort y axis
#                 # TODO: stop dupe
#                 # TODO: figure out how to sort avg cumulative jazz
#                 {
#                     'name': 'y',
#                     'type': 'band',
#                     'domain': {
#                         'data': 'features',
#                         'field': 'id',
#                         'sort': {
#                             'field': {
#                                 'signal': 'feature_sort',
#                             },
#                             'order': {
#                                 'signal': 'sort_direction',
#                             },
#                             'op': 'mean',
#                         },
#                     },
#                     'range': [
#                         0,
#                         {
#                             'signal': 'importancesChartHeight',
#                         },
#                     ],
#                 },
#                 {
#                     'name': 'x',
#                     'domain': {
#                         'signal': 'if(feature_stats === "Cumulative Average '
#                                   'Change", [-1, 1], [data("statScale")[0].'
#                                   'min, data("statScale")[0].max])',
#                     },
#                     'range': [
#                         0,
#                         {
#                             'signal': 'halfWidth - 25',
#                         },
#                     ],
#                 },
#             ],
#             'axes': [
#                 {
#                     'orient': 'top',
#                     'scale': 'x',
#                     'title': feature_stats_signal,
#                 },
#
#             ],
#             'marks': [
#                 {
#                     'name': 'descriptive_stats',
#                     'type': 'rect',
#                     'from': {
#                         'data': 'features',
#                     },
#                     'encode': {
#                         'enter': {
#                             'height': {
#                                 'scale': 'y',
#                                 'band': 1,
#                             },
#                         },
#                         'update': {
#                             'tooltip': {
#                                 'signal': feature_tooltip_signal,
#                             },
#                             'x': [
#                                 {
#                                     'test': feature_stats_test,
#                                     'scale': 'x',
#                                     'field': 'Cumulative Avg Decrease',
#                                 },
#                                 {
#                                     'scale': 'x',
#                                     'value': 0,
#                                 },
#                             ],
#                             'y': {
#                                 'scale': 'y',
#                                 'field': 'id',
#                             },
#                             'x2': [
#                                 {
#                                     'test': feature_stats_test,
#                                     'scale': 'x',
#                                     'field': 'Cumulative Avg Increase',
#                                 },
#                                 {
#                                     'scale': 'x',
#                                     'field': feature_stats_signal,
#                                 },
#                             ],
#                             'fill': [
#                                 {
#                                     'test': 'metric === datum.id',
#                                     'value': '#FF0000',
#                                 },
#                                 {
#                                     'value': '#AAAAAA',
#                                 }
#                             ],
#                         },
#                     },
#                 },
#                 {
#                     'type': 'rule',
#                     'encode': {
#                         'enter': {
#                             'x': {
#                                 'scale': 'x',
#                                 'value': 0,
#                             },
#                             'x2': {
#                                 'scale': 'x',
#                                 'value': 0,
#                             },
#                             'y': {
#                                 'value': 0,
#                             },
#                             'y2': {
#                                 'signal': 'importancesChartHeight',
#                             },
#                         },
#                         'update': {
#                             'opacity': [
#                                 {
#                                     'test': feature_stats_test,
#                                     'value': 1,
#                                 },
#                                 {
#                                     'value': 0,
#                                 },
#                             ],
#                         },
#                     },
#                 },
#             ],
#         }
#         spec['marks'].append(first_diff_subplot)
#         spec['data'].append({
#             'name': 'features',
#             'values': features_chart_data.to_dict('records'),
#         })
#         spec['data'].append({
#             'name': 'statScale',
#             'source': 'features',
#             'transform': [
#                 {
#                     'type': 'aggregate',
#                     'ops': [
#                         'min',
#                         'max',
#                     ],
#                     'fields': [
#                         feature_stats_signal,
#                         feature_stats_signal,
#                     ],
#                     'as': [
#                         'min',
#                         'max',
#                     ],
#                 },
#             ],
#         })
