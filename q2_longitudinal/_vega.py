# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import json


def _create_volatility_spec(data, group_by_field, time_field, metric_field,
                            individual_id_field):
    test = ('!length(data(\'selected\')) || '
            'indata(\'selected\', \'value\', datum.value)')
    spec = {
        '$schema': 'https://vega.github.io/schema/vega/v3.0.json',
        'width': 800,
        'height': 600,
        'padding': 5,
        'signals': [
            {
                'name': 'showSpaghetti',
                'value': True,
                'bind': {
                    'input': 'checkbox',
                    'name': 'Show me the spaghetti',
                },
            },
            {
                'name': 'showErrorBars',
                'value': False,
                'bind': {
                    'input': 'checkbox',
                    'name': 'Show me the error bars',
                },
            },
            {
                'name': 'meanLineThickness',
                'value': 3,
                'bind': {
                    'input': 'range',
                    'min': 1,
                    'max': 10,
                    'step': 1,
                },
            },
            {
                'name': 'clear',
                'value': True,
                'on': [
                    {
                        'events': 'mouseup[!event.item]',
                        'update': 'true',
                        'force': True,
                    },
                ],
            },
            {
                'name': 'shift',
                'value': False,
                'on': [
                    {
                        'events': '@legendSymbol:click, @legendLabel:click',
                        'update': 'event.shiftKey',
                        'force': True,
                    },
                ],
            },
            {
                'name': 'clicked',
                'value': None,
                'on': [
                    {
                        'events': '@legendSymbol:click, @legendLabel:click',
                        'update': '{value: datum.value}',
                        'force': True,
                    }
                ]
            },
        ],
        'scales': [
            {
                'name': 'x',
                'type': 'point',
                'range': 'width',
                'domain': {
                    'data': 'individual',
                    'field': 'month',
                },
            },
            {
                'name': 'y',
                'type': 'linear',
                'range': 'height',
                'nice': True,
                'zero': True,
                'domain': {
                    'data': 'individual',
                    'field': 'shannon',
                },
            },
            {
                'name': 'color',
                'type': 'ordinal',
                'range': 'category',
                'domain': {
                    'data': 'individual',
                    'field': 'delivery',
                },
            },
        ],
        'axes': [
            {
                'orient': 'bottom',
                'scale': 'x',
                'title': 'month',
            },
            {
                'orient': 'left',
                'scale': 'y',
                'title': 'shannon',
            }
        ],
        'legends': [
            {
                'stroke': 'color',
                'title': 'delivery',
                'encode': {
                    'symbols': {
                        'name': 'legendSymbol',
                        'interactive': True,
                        'update': {
                            'fill': {
                                'value': 'transparent',
                            },
                            'strokeWidth': {
                                'value': 2,
                            },
                            'opacity': [
                                {
                                    # TODO: finish adding these
                                    'test': test,
                                    'value': 1.0
                                },
                                {
                                    'value': 0.15,
                                },
                            ],
                            'size': {
                                'value': 100,
                            },
                        },
                    },
                    'labels': {
                        'name': 'legendLabel',
                        'interactive': True,
                        'update': {
                            'opacity': [
                                {
                                    'test': test,
                                    'value': 1,
                                },
                                {
                                    'value': 0.25,
                                },
                            ],
                        },
                    },
                },
            },
        ],
        'marks': [
            {
                'type': 'group',
                'from': {
                    'facet': {
                        'name': 'spaghettis',
                        'data': 'individual',
                        'groupby': 'studyid',
                    },
                },
                'marks': [
                    {
                        'type': 'line',
                        'from': {
                            'data': 'spaghettis',
                        },
                        'sort': {
                            'field': 'x',
                            'order': 'ascending',
                        },
                        'encode': {
                            'enter': {
                                'x': {
                                    'scale': 'x',
                                    'field': 'month',
                                },
                                'y': {
                                    'scale': 'y',
                                    'field': 'shannon',
                                },
                                'stroke': {
                                    'scale': 'color',
                                    'field': 'delivery',
                                },
                                'strokeWidth': {
                                    'value': 0.5
                                },
                            },
                            'update': {
                                'opacity': [
                                    {
                                        'test': 'showSpaghetti && '
                                                '(!length(data(\'selected\'))'
                                                '|| indata(\'selected\', '
                                                '\'value\', datum.delivery))',
                                        'value': 0.5,
                                    },
                                    {
                                        'value': 0.0,
                                    },
                                ],
                            },
                        },
                    },
                ],
             },
            {
                'type': 'group',
                'from': {
                    'facet': {
                        'name': 'series',
                        'data': 'aggByDelivery',
                        'groupby': 'delivery'
                    }
                },
                'marks': [
                    {
                        'type': 'line',
                        'from': {
                            'data': 'series'
                        },
                        'sort': {
                            'field': 'datum.month',
                            'order': 'ascending'
                        },
                        'encode': {
                            'enter': {
                                'x': {
                                    'scale': 'x',
                                    'field': 'month'
                                },
                                'y': {
                                    'scale': 'y',
                                    'field': 'mean'
                                },
                                'stroke': {
                                    'scale': 'color',
                                    'field': 'delivery'
                                }
                            },
                            'update': {
                                'strokeWidth': {
                                    'signal': 'meanLineThickness'
                                },
                                'opacity': [
                                    {
                                        'test': '!length(data(\'selected\')) '
                                                '|| indata(\'selected\', '
                                                '\'value\', datum.delivery)',
                                        'value': 1.0
                                    },
                                    {
                                        'value': 0.0
                                    }
                                ]
                            }
                        }
                    },
                    {
                        'type': 'rect',
                        'from': {
                            'data': 'series'
                        },
                        'encode': {
                            'enter': {
                                'fill': {
                                    'scale': 'color',
                                    'field': 'delivery'
                                },
                                'width': {
                                    'value': 2.0
                                }
                            },
                            'update': {
                                'x': {
                                    'scale': 'x',
                                    'field': 'month',
                                    'band': 0.5
                                },
                                'y': {
                                    'scale': 'y',
                                    'field': 'ci0'
                                },
                                'y2': {
                                    'scale': 'y',
                                    'field': 'ci1'
                                },
                                'opacity': [
                                    {
                                        'test': 'showErrorBars && '
                                                '(!length(data(\'selected\'))'
                                                '|| indata(\'selected\', '
                                                '\'value\', datum.delivery))',
                                        'value': 1.0
                                    },
                                    {
                                        'value': 0.0
                                    }
                                ]
                            }
                        }
                    }
                ]
            }
        ],
        'data': [
            {
                'name': 'individual',
                # TODO
                'values': [],
            }
        ],
    }

    return (json.dumps(spec)[:-1] + ',"data":{"values":' +
            data.to_json(orient='records') + '}}')
