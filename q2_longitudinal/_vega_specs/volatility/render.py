# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import json

import pandas as pd

from .const import (
    SIG_METRIC, SIG_STATS_CHART_WIDTH, VAR_STATS_GAP
    )
from .axis import render_axes_ctrl, render_axes_stats
from .legend import render_legends_ctrl
from .mark import (
    render_marks_ctrl, render_marks_stats, render_marks_ctrl_global,
    render_marks_ctrl_grouped, render_marks_ctrl_individual,
    render_marks_stats_bars)
from .signal import (
    render_signals_ctrl, render_signals_ctrl_individual, render_signals_stats)
from .scale import render_scales_ctrl, render_scales_stats
from .data import render_data_ctrl, render_data_stats


SIDES = [
    {'name': 'left',
     'x': {'value': 0},
     'sort_field': 'Mean',
     'sort_dir': 'descending'},
    {'name': 'right',
     'x': {'signal': SIG_STATS_CHART_WIDTH, 'offset': VAR_STATS_GAP},
     'sort_field': 'Cumulative Average Change',
     'sort_dir': 'descending'}]


def render_subplot_ctrl(yscale, state):
    ctrl_chart = render_marks_ctrl()
    ctrl_chart['marks'] = render_marks_ctrl_global() + \
        render_marks_ctrl_grouped(state)
    ctrl_chart['scales'] = render_scales_ctrl(state, yscale)
    ctrl_chart['axes'] = render_axes_ctrl(state)
    ctrl_chart['legends'] = render_legends_ctrl()
    return ctrl_chart


def render_subplot_stats():
    sides = []
    for side in SIDES:
        chart = render_marks_stats(side)
        chart['marks'] = render_marks_stats_bars(side)
        chart['scales'] = render_scales_stats(side)
        chart['axes'] = render_axes_stats(side)
        sides.append(chart)
    return sides


def render_spec_volatility(control_chart_data: pd.DataFrame,
                           metric_stats_chart_data: pd.DataFrame,
                           individual_id: str, state: str,
                           default_group: str, group_columns: list,
                           default_metric: str, metric_columns: list,
                           yscale: str) -> str:
    spec = {
        # This `$schema` is only fetched as part of the interactive vega
        # editor, which opens up outside of the visualization - this doesn't
        # appear to create any kind of XHR side-effect when loading the
        # visualization in an offline context.
        '$schema': 'https://vega.github.io/schema/vega/v4.0.json',
        'autosize': {'type': 'fit-x', 'contains': 'padding', 'resize': True},
        # This dimension is here for when the viz is opened in the online
        # Vega Editor.
        'width': 800,
        'title': {'text': {'signal': SIG_METRIC}},
        'background': '#FFFFFF',
        # Not registering signals on a subplot level since they aren't super
        # helpful (e.g. can't `bind` in a subplot signal).
        'signals': render_signals_ctrl(default_group, group_columns,
                                       default_metric, metric_columns) + \
        render_signals_stats(SIDES),
        'scales': [],
        'marks': [],
        # Add data at root of plot, it is easier to use the built in view
        # accessor to debug values
        'data': render_data_ctrl(control_chart_data, state) + \
        render_data_stats(metric_stats_chart_data, SIDES),
    }

    ctrl_chart = render_subplot_ctrl(yscale, state)
    if individual_id:
        ctrl_chart['marks'].append(
            render_marks_ctrl_individual(individual_id, state))
        spec['signals'].extend(render_signals_ctrl_individual())
    spec['marks'].append(ctrl_chart)

    stats_chart = render_subplot_stats()
    spec['marks'].extend(stats_chart)

    return json.dumps(spec, indent=2, sort_keys=True)
