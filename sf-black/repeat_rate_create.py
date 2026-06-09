import pathlib

import duckdb

from cli.black.util import import_to_db
from magickpi.engine.extension.metric import MetricNumericalRateDrillDown
from src.magickpi.engine import SignificantFactorsEngine
from src.magickpi.engine.extension.metric import MetricAverageDrillDown
from src.magickpi.engine.extension.segment import SegmentSetCover, SegmentMILP


def run_analysis(base_path):
    # STEP 1: Initialize engine
    db_path = base_path / 'data_drill_down.duckdb'
    db = duckdb.connect(db_path)
    engine = SignificantFactorsEngine(db)

    # STEP 2: Prepare data
    # No steps. Usually removing infrequent values.

    # STEP 3: Add augmenters
    # No steps. Usually transforming / quantizing values.

    # STEP 4: Set features
    engine.set_agg_features([
        'First_order_best_category', 'First_order_best_sub_catgeory',
        'FirstOrderCity', 'FirstOrderCityTier',
        'First_order_OrderPlatform',
        'First_order_campaign_medium',
        'First_order_campaign_source',
        'First_order_campaign_term',
        'First_order_referrer_type',
        'OrderTiming',
        'DiscountUsageSegment',
        'WeekdayWeekendPreference'
    ])

    # STEP 5: Add metric
    engine.set_super_aggregate_and_segments_from_metric(
        MetricNumericalRateDrillDown(
            in_numerator='repeated_users_segment',
            in_denominator='total_users_segment',
            in_count=None,

            out_agg_numerator='agg_numerator',
            out_agg_denominator='agg_denominator',
            out_agg_count='agg_count',

            out_summary_numerator='summary_numerator',
            out_summary_denominator='summary_denominator',
            out_summary_count='summary_count',
            out_summary_metric='summary_metric',

            out_segment_numerator='repeat_customers',
            out_segment_denominator='total_customers',
            out_segment_metric='order_repeat_rate',
            out_segment_count='count',
            out_segment_risk_ratio='risk_ratio',
            out_segment_impact='impact',
            out_segment_z_value='z'
        )
    )

    # STEP 6: Prepare super-aggregates
    # No steps. Usually for converting null values to unknowns

    engine.add_mutually_exclusive_agg_features(['First_order_best_category', 'First_order_best_sub_catgeory'])
    engine.add_mutually_exclusive_agg_features(['FirstOrderCity', 'FirstOrderCityTier'])

    # STEP 7: Enrich segment
    # No steps

    engine.add_enrich_segment(SegmentMILP(
        in_agg_target='agg_metric',
        in_agg_weight='agg_count',
        out_segment_score='score',
        max_segments=1000
    ))

    # FINALLY, RUN THE ENGINE
    engine.run(
        min_support=0.02,
        # risk_ratio_boundary=(0.7, 1.3)
    )


if __name__ == '__main__':
    BASE_PATH = pathlib.Path(__file__).parent.parent.parent / 'data/black/mece'

    import_to_db(BASE_PATH)
    run_analysis(BASE_PATH)

