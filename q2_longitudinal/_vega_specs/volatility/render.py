# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


# TODO: prefix constants with underscore

import json

import pandas as pd

from .axis import _control_chart_axes
from .legend import _control_chart_legend
from .mark import (
    _control_chart_global_marks, _control_chart_subplot,
    _control_chart_grouped_marks, _control_chart_individual_marks)
from .signal import _volatility_signals, _spaghetti_signals
from .scale import _layout_scale, _color_scale, _control_chart_subplot_scales
from .data import _control_chart_data
from .const import METRIC_SIGNAL


# TODO: do I need the feature flag?
# TODO: break out more placeholder values (like signal dicts)
# TODO: split this spec composition up a bit more
def render_volatility_spec(is_feat_vol_plot: bool,
                           control_chart_data: pd.DataFrame,
                           features_chart_data: pd.DataFrame,
                           individual_id: str, state: str,
                           default_group: str, group_columns: list,
                           default_metric: str, metric_columns: list,
                           yscale: str) -> str:
    spec = {
        # This `$schema` is only fetched as part of the interactive vega
        # editor, which opens up outside of the visualization - this doesn't
        # appear to create any kind of XHR side-effect when loading the
        # visualization in an offline context.
        '$schema': 'https://vega.github.io/schema/vega/v3.0.json',
        'autosize': {'type': 'fit-x', 'contains': 'padding', 'resize': True},
        # This dimension is here for when the viz is opened in the online
        # Vega Editor.
        'width': 800,
        'signals': [],
        # TODO: can color scale get moved into the control chart?
        'scales': [_layout_scale(), _color_scale()],
        'marks': [],
        'data': _control_chart_data(control_chart_data, METRIC_SIGNAL, state),
    }

    control_chart = _control_chart_subplot(yscale)
    control_chart['marks'] = _control_chart_global_marks() + \
        _control_chart_grouped_marks(state)
    control_chart['scales'] = _control_chart_subplot_scales(state, yscale)
    control_chart['axes'] = _control_chart_axes(state)
    control_chart['legends'] = _control_chart_legend()

    spec['signals'].extend(_volatility_signals(features_chart_data,
                                               default_group, group_columns,
                                               default_metric, metric_columns))

    if individual_id:
        control_chart['marks'].append(
            _control_chart_individual_marks(individual_id, state))
        spec['signals'].extend(_spaghetti_signals())

    spec['marks'].append(control_chart)
    return json.dumps(spec)
