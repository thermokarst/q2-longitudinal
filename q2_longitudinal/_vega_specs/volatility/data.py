# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


def _control_chart_data(control_chart_data, metric_signal, state):
    return [
        {
            'name': 'individual',
            'values': control_chart_data.to_dict('record'),
            'transform': [
                {
                    'type': 'formula',
                    'as': 'groupByVal',
                    'expr': 'datum[grouper]',
                },
                {
                    'type': 'formula',
                    'as': 'metricVal',
                    'expr': 'datum[metric]',
                },
            ],
        },
        {
            'name': 'globalVals',
            'source': 'individual',
            'transform': [
                {
                    'type': 'aggregate',
                    'ops': [
                        'mean',
                        'min',
                        'max',
                        'stdev',
                        'min',
                        'max',
                    ],
                    'fields': [
                        metric_signal,
                        state,
                        state,
                        metric_signal,
                        metric_signal,
                        metric_signal,
                    ],
                    'as': [
                        'mean',
                        'minX',
                        'maxX',
                        'stdev',
                        'minY',
                        'maxY',
                    ]
                },
                {
                    'type': 'formula',
                    'as': 'cl0',
                    'expr': 'datum.mean - (3 * datum.stdev)'
                },
                {
                    'type': 'formula',
                    'as': 'cl1',
                    'expr': 'datum.mean - (2 * datum.stdev)'
                },
                {
                    'type': 'formula',
                    'as': 'cl2',
                    'expr': 'datum.mean + (2 * datum.stdev)'
                },
                {
                    'type': 'formula',
                    'as': 'cl3',
                    'expr': 'datum.mean + (3 * datum.stdev)'
                },
                {
                    'type': 'formula',
                    'as': 'ext',
                    'expr': '[datum.cl0, datum.cl3]',
                },
            ],
        },
        {
            'name': 'aggBy',
            'source': 'individual',
            'transform': [
                {
                    'type': 'aggregate',
                    'groupby': [
                        'groupByVal',
                        state,
                    ],
                    'ops': [
                        'mean',
                        # TODO: parameterize these intervals
                        # I don't see an easy way at the moment to define
                        # your own confidence interval in vega.
                        'ci0',
                        'ci1',
                        'count',
                    ],
                    'fields': [
                        metric_signal,
                        metric_signal,
                        metric_signal,
                        metric_signal,
                    ],
                    'as': [
                        'mean',
                        'ci0',
                        'ci1',
                        'count',
                    ],
                },
            ],
        },
        {
            'name': 'selected',
            'on': [
                {
                    'trigger': 'clear',
                    'remove': True
                },
                {
                    'trigger': '!shift',
                    'remove': True
                },
                {
                    'trigger': '!shift && clicked',
                    'insert': 'clicked'
                },
                {
                    'trigger': 'shift && clicked',
                    'toggle': 'clicked'
                },
            ],
        },
    ]
