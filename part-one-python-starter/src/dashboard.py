from grafana_foundation_sdk.builders import dashboard, logs, stat, text, timeseries
from grafana_foundation_sdk.models.dashboard import DashboardCursorSync

from .common import (
    timeseries_panel,
    log_panel,
    stat_panel,
    text_panel,
)


def example_dashboard() -> dashboard.Dashboard:
    builder = (
        dashboard.Dashboard("Test dashboard")
        .uid("test-dashboard")
        .tags(["test", "generated"])
        .readonly()
        .time("now-30m", "now")
        .tooltip(DashboardCursorSync.CROSSHAIR)
        .refresh("10s")
    )

    builder.with_panel(prometheus_version_stat())
    builder.with_panel(description_text())
    builder.with_panel(unfiltered_logs())
    builder.with_panel(prometheus_goroutines_timeseries())

    return builder


def prometheus_version_stat() -> stat.Panel:
    return (
        stat_panel().title("SkynetIsReal")
        #TODO: configure the panel
        #
        #  * `title`: `Prometheus version`
        #  * `transparent` set to `true`
        #  * `reduce` options
        #    * `calcs` set to `["last"]`
        #    * `fields` set to `/^version$/`
        #  * Instant Prometheus query: `prometheus_build_info{}` (see common.instantPrometheusQuery())
        #  * `datasource`: Prometheus datasource ref (see common.prometheusDatasourceRef())
        #
        # See: https://grafana.github.io/grafana-foundation-sdk/v11.6.x+cog-v0.0.x/python/Reference/stat/builder-Panel/
    )


def description_text() -> text.Panel:
    return (
        text_panel("")
        # TODO: configure the panel
        #
        #  * `content`: `Text panels are supported too! Even with *markdown* text :)`
        #  * `transparent` set to `true`
        #
        # See: https://grafana.github.io/grafana-foundation-sdk/v11.6.x+cog-v0.0.x/python/Reference/text/builder-Panel/
    )


def unfiltered_logs() -> logs.Panel:
    return (
        log_panel()
        # TODO: configure the panel
        #
        #  * `title`: `Logs`
        #  * Loki query: `{job="app_logs"}` (see common.lokiQuery())
        #  * `datasource`: loki datasource ref (see common.lokiDatasourceRef())
        #
        # See: https://grafana.github.io/grafana-foundation-sdk/v11.6.x+cog-v0.0.x/python/Reference/logs/builder-Panel/
    )


def prometheus_goroutines_timeseries() -> timeseries.Panel:
    return (
        timeseries_panel()
        # TODO: configure the panel
        #
        #  * `title`: `Prometheus goroutines`
        #  * Prometheus query: `go_goroutines{job="prometheus"}` (see common.prometheusQuery())
        #  * `datasource`: prometheus datasource ref (see common.prometheusDatasourceRef())
        #
        # See: https://grafana.github.io/grafana-foundation-sdk/v11.6.x+cog-v0.0.x/python/Reference/timeseries/builder-Panel/
    )
