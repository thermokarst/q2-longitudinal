# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import json

import pandas as pd

from ._mark import _spaghetti_marks, _individual_marks, _control_chart_marks
from ._signal import _volatility_signals, _spaghetti_signals
from ._scale import _layout_scale, _color_scale
from ._data import _control_chart_data
from ._test import OPACITY_TEST, GROUP_TEST, ERROR_BAR_TEST


# TODO: do I need the feature flag?
# TODO: break out more placeholder values (like signal dicts)
# TODO: split this spec composition up a bit more
def _render_volatility_spec(is_feat_vol_plot: bool,
                            control_chart_data: pd.DataFrame,
                            features_chart_data: pd.DataFrame,
                            individual_id: str, state: str,
                            default_group: str, group_columns: list,
                            default_metric: str, metric_columns: list,
                            yscale: str) -> str:
    metric_signal = {'signal': 'metric'}
    group_signal = {'signal': 'grouper'}

    # These templates customize the tooltips
    # TODO: new template names
    mean_signal = ('{"title": "group mean", "group": datum.groupByVal,'
                   ' "state": datum["%s"], "count": datum.count,'
                   ' "mean": datum.mean, "ci0": datum.ci0, "ci1": datum.ci1}'
                   % state)

    spaghetti_marks = _spaghetti_marks(state, GROUP_TEST, mean_signal,
                                       ERROR_BAR_TEST)
    signals = _volatility_signals(features_chart_data, default_group,
                                  group_columns, default_metric,
                                  metric_columns)

    if individual_id:
        spaghetti_signal = ('{"title": "spaghetti", "individual_id": '
                            'datum["%s"], "group": datum.groupByVal, "state": '
                            'datum["%s"], "metric": datum.metricVal}' %
                            (individual_id, state))
        spaghetti_marks.append(_individual_marks(individual_id, state,
                                                 metric_signal, group_signal,
                                                 GROUP_TEST, spaghetti_signal))

        signals.extents(_spaghetti_signals())
    # Just a quick note, order doesn't matter here (JSON documents are not
    # ordered) - this will render out stochastically, which is fine - vega
    # knows what to do.
    spec = {
        # This `$schema` is only fetched as part of the interactive vega
        # editor, which opens up outside of the visualization - this doesn't
        # appear to create any kind of XHR side-effect when loading the
        # visualization in an offline context.
        '$schema': 'https://vega.github.io/schema/vega/v3.0.json',
        'autosize': {
            'type': 'fit-x',
            'contains': 'padding',
            'resize': True,
        },
        # These dimensions are here for when the viz is opened in the
        # Vega Editor.
        'width': 800,
        'signals': signals,
        'scales': [_layout_scale(), _color_scale()],
        'marks': _control_chart_marks(spaghetti_marks, state, yscale,
                                      group_signal, metric_signal,
                                      OPACITY_TEST),
        'data': _control_chart_data(control_chart_data, metric_signal, state),
    }

    return json.dumps(spec)
