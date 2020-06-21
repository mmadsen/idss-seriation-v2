import pytest
import datetime


@pytest.fixture
def three_event_list():
    """
    Simple event list with the following properties:
    1.  2 total hours usage during the day
    2.  40 minutes average length of usage interval during day
    3.  Hours 0, 3, and 10 have usage statistics, others record zeros for totals
    4.  Hour 0 = 30 total, Hour 3 = 30 total, Hour 10 = 1 hour usage total
    """
    event_list = [
        (
            datetime.datetime(2019, 2, 1, 0, 0, 0),
            datetime.datetime(2019, 2, 1, 0, 30, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 3, 0, 0),
            datetime.datetime(2019, 2, 1, 3, 30, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 10, 0, 0),
            datetime.datetime(2019, 2, 1, 11, 0, 0),
        ),
    ]
    return event_list


@pytest.fixture
def detailed_hour_event_list():
    """
    Simple event list with the following properties:
    1.  Max usage length for hour 0 = 30 min
    2.  Min usage length for hour 0 = 5 min
    3.  Avg usage length for hour 0 = 15 min
    4.  Min idle gap for hour 0 = 5 min
    5.  Max idle gap for hour 0 = 9 min
    6.  Avg idle gap for hour 0 = 7 min
    """
    event_list = [
        (
            datetime.datetime(2019, 2, 1, 0, 0, 0),
            datetime.datetime(2019, 2, 1, 0, 30, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 0, 35, 0),
            datetime.datetime(2019, 2, 1, 0, 45, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 0, 54, 0),
            datetime.datetime(2019, 2, 1, 0, 59, 0),
        ),
    ]
    return event_list


@pytest.fixture
def event_list():
    """Contains:
    * First six events actually go with 2019,1,31 timeslot, final four go with 2019,2,1 timeslot
    """
    event_list = [
        (
            datetime.datetime(2019, 2, 1, 0, 0, 0),
            datetime.datetime(2019, 2, 1, 0, 25, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 0, 40, 0),
            datetime.datetime(2019, 2, 1, 0, 48, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 3, 0, 0),
            datetime.datetime(2019, 2, 1, 3, 15, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 3, 20, 0),
            datetime.datetime(2019, 2, 1, 3, 25, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 3, 35, 0),
            datetime.datetime(2019, 2, 1, 4, 22, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 5, 15, 0),
            datetime.datetime(2019, 2, 1, 6, 5, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 10, 15, 0),
            datetime.datetime(2019, 2, 1, 11, 15, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 13, 20, 0),
            datetime.datetime(2019, 2, 1, 13, 25, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 20, 0, 0),
            datetime.datetime(2019, 2, 1, 21, 45, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 23, 35, 0),
            datetime.datetime(2019, 2, 2, 0, 20, 0),
        ),
    ]
    return event_list


@pytest.fixture
def result_duration_statistics_day_timeslots_eventlist():
    """
    MEAN_EPISODE_DURATION = 1
    MAX_EPISODE_DURATION = 2
    MIN_EPISODE_DURATION = 3
    COUNT_EPISODES_IN_TIMESLOT = 4
    :return:
    """
    return {
        datetime.datetime(2019, 1, 31, 10, 0): {
            1: 25.0,
            2: 50.0,
            3: 5.0,
            4: 6,
        },
        datetime.datetime(2019, 2, 1, 10, 0): {
            1: 53.75,
            2: 105.0,
            3: 5.0,
            4: 4,
        },
    }


@pytest.fixture
def result_idle_statistics_day_timeslots_eventlist():
    """
    MEAN_EPISODE_DURATION = 1
    MAX_EPISODE_DURATION = 2
    MIN_EPISODE_DURATION = 3
    COUNT_EPISODES_IN_TIMESLOT = 4
    :return:
    """
    return {
        datetime.datetime(2019, 1, 31, 10, 0): {
            5: 184.28571428571428,
            6: 132.0,
            7: 5.0,
            8: 7,
        },
        datetime.datetime(2019, 2, 1, 10, 0): {
            5: 245.0,
            6: 395.0,
            7: 15.0,
            8: 5,
        },
    }


@pytest.fixture
def result_total_usage_credited_hour_timeslots_eventlist():
    return {
        datetime.datetime(2019, 2, 1, 0, 0): 33.0,
        datetime.datetime(2019, 2, 1, 1, 0): 0,
        datetime.datetime(2019, 2, 1, 2, 0): 0,
        datetime.datetime(2019, 2, 1, 3, 0): 45.0,
        datetime.datetime(2019, 2, 1, 4, 0): 22.0,
        datetime.datetime(2019, 2, 1, 5, 0): 45.0,
        datetime.datetime(2019, 2, 1, 6, 0): 5.0,
        datetime.datetime(2019, 2, 1, 7, 0): 0,
        datetime.datetime(2019, 2, 1, 8, 0): 0,
        datetime.datetime(2019, 2, 1, 9, 0): 0,
        datetime.datetime(2019, 2, 1, 10, 0): 45.0,
        datetime.datetime(2019, 2, 1, 11, 0): 15.0,
        datetime.datetime(2019, 2, 1, 12, 0): 0,
        datetime.datetime(2019, 2, 1, 13, 0): 5.0,
        datetime.datetime(2019, 2, 1, 14, 0): 0,
        datetime.datetime(2019, 2, 1, 15, 0): 0,
        datetime.datetime(2019, 2, 1, 16, 0): 0,
        datetime.datetime(2019, 2, 1, 17, 0): 0,
        datetime.datetime(2019, 2, 1, 18, 0): 0,
        datetime.datetime(2019, 2, 1, 19, 0): 0,
        datetime.datetime(2019, 2, 1, 20, 0): 60.0,
        datetime.datetime(2019, 2, 1, 21, 0): 45.0,
        datetime.datetime(2019, 2, 1, 22, 0): 0,
        datetime.datetime(2019, 2, 1, 23, 0): 25.0,
        datetime.datetime(2019, 2, 2, 0, 0): 20.0,
    }


@pytest.fixture
def event_list_single_day_hnl():
    """Contains events from a single day in Hawaii time, even though
    the events cross a day in UTC time.  This measures whether we
    properly assign events to the day timeslot in their local time zone
    even though they cross UTC day boundaries.
    """
    event_list = [
        (
            datetime.datetime(2019, 2, 1, 12, 0, 0),
            datetime.datetime(2019, 2, 1, 12, 25, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 12, 40, 0),
            datetime.datetime(2019, 2, 1, 12, 48, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 13, 0, 0),
            datetime.datetime(2019, 2, 1, 13, 15, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 13, 20, 0),
            datetime.datetime(2019, 2, 1, 13, 25, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 13, 35, 0),
            datetime.datetime(2019, 2, 1, 14, 22, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 15, 15, 0),
            datetime.datetime(2019, 2, 1, 16, 5, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 19, 15, 0),
            datetime.datetime(2019, 2, 1, 19, 15, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 20, 20, 0),
            datetime.datetime(2019, 2, 1, 20, 25, 0),
        ),
        (
            datetime.datetime(2019, 2, 2, 6, 0, 0),
            datetime.datetime(2019, 2, 2, 6, 45, 0),
        ),
        (
            datetime.datetime(2019, 2, 2, 7, 35, 0),
            datetime.datetime(2019, 2, 2, 8, 20, 0),
        ),
    ]
    return event_list


@pytest.fixture
def result_assign_events_day_timeslots():
    return {
        datetime.datetime(2019, 2, 1, 10, 0): [
            (
                datetime.datetime(2019, 2, 1, 12, 0, 0),
                datetime.datetime(2019, 2, 1, 12, 25, 0),
            ),
            (
                datetime.datetime(2019, 2, 1, 12, 40, 0),
                datetime.datetime(2019, 2, 1, 12, 48, 0),
            ),
            (
                datetime.datetime(2019, 2, 1, 13, 0, 0),
                datetime.datetime(2019, 2, 1, 13, 15, 0),
            ),
            (
                datetime.datetime(2019, 2, 1, 13, 20, 0),
                datetime.datetime(2019, 2, 1, 13, 25, 0),
            ),
            (
                datetime.datetime(2019, 2, 1, 13, 35, 0),
                datetime.datetime(2019, 2, 1, 14, 22, 0),
            ),
            (
                datetime.datetime(2019, 2, 1, 15, 15, 0),
                datetime.datetime(2019, 2, 1, 16, 5, 0),
            ),
            (
                datetime.datetime(2019, 2, 1, 19, 15, 0),
                datetime.datetime(2019, 2, 1, 19, 15, 0),
            ),
            (
                datetime.datetime(2019, 2, 1, 20, 20, 0),
                datetime.datetime(2019, 2, 1, 20, 25, 0),
            ),
            (
                datetime.datetime(2019, 2, 2, 6, 0, 0),
                datetime.datetime(2019, 2, 2, 6, 45, 0),
            ),
            (
                datetime.datetime(2019, 2, 2, 7, 35, 0),
                datetime.datetime(2019, 2, 2, 8, 20, 0),
            ),
        ]
    }


@pytest.fixture
def result_total_daily_usage_during_core_hours_eventlist():
    return {
        datetime.datetime(2019, 1, 31, 10, 0): 150.0,
        datetime.datetime(2019, 2, 1, 10, 0): 175.0,
    }


@pytest.fixture
def result_total_daily_usage_during_core_events_with_core():
    return {
        datetime.datetime(2019, 1, 31, 10, 0): 33.0,
        datetime.datetime(2019, 2, 1, 10, 0): 150.0,
    }


@pytest.fixture
def result_total_usage_credited_day_timeslots_events_with_core():
    return {
        datetime.datetime(2019, 1, 31, 10, 0): 219.0,
        datetime.datetime(2019, 2, 1, 10, 0): 215.0,
    }


@pytest.fixture
def query_start():
    return datetime.datetime(2019, 2, 1, 0, 0, 0)


@pytest.fixture
def query_end():
    """Just to capture the day-wrapping of the test data set"""
    return datetime.datetime(2019, 2, 2, 1, 59, 0)


@pytest.fixture
def events_with_core():
    event_list_with_core_usage = [
        (
            datetime.datetime(2019, 2, 1, 0, 0, 0),
            datetime.datetime(2019, 2, 1, 0, 25, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 0, 40, 0),
            datetime.datetime(2019, 2, 1, 0, 48, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 3, 0, 0),
            datetime.datetime(2019, 2, 1, 3, 15, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 3, 20, 0),
            datetime.datetime(2019, 2, 1, 3, 25, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 3, 35, 0),
            datetime.datetime(2019, 2, 1, 4, 22, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 8, 0, 0),
            datetime.datetime(2019, 2, 1, 10, 0, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 10, 15, 0),
            datetime.datetime(2019, 2, 1, 11, 15, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 13, 20, 0),
            datetime.datetime(2019, 2, 1, 13, 25, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 20, 0, 0),
            datetime.datetime(2019, 2, 1, 21, 45, 0),
        ),
        (
            datetime.datetime(2019, 2, 1, 23, 35, 0),
            datetime.datetime(2019, 2, 2, 0, 20, 0),
        ),
    ]
    return event_list_with_core_usage


@pytest.fixture
def ibis_hawaii_org():
    return {
        "reply_days": 10,
        "asset_usage_episode_months": 3,
        "name": "Ibis Office",
        "energy_management": True,
        "dp60_days": 45,
        "is_active": True,
        "price_model_id": 37,
        "updated_at": 1554809319,
        "packet_days": 1,
        "org_type": "customer",
        "mode": "normal",
        "summary_meas_86400_years": 10,
        "summary_meas_3600_months": 120,
        "timezone_name": "Pacific/Honolulu",
        "asset_management": True,
        "id": 8004,
        "core_hours_end_time": {
            "second_of_day": 54000,
            "second": 0,
            "minute": 0,
            "hour": 15,
        },
        "core_hours_start_time": {
            "second_of_day": 28800,
            "second": 0,
            "minute": 0,
            "hour": 8,
        },
    }


@pytest.fixture
def ibis_hawaii_org_direct_database():
    return {
        "reply_days": 10,
        "asset_usage_episode_months": 3,
        "name": "Ibis Office",
        "energy_management": True,
        "dp60_days": 45,
        "is_active": True,
        "price_model_id": 37,
        "updated_at": 1554809319,
        "packet_days": 1,
        "org_type": "customer",
        "mode": "normal",
        "summary_meas_86400_years": 10,
        "summary_meas_3600_months": 120,
        "timezone_name": "Pacific/Honolulu",
        "asset_management": True,
        "id": 8004,
        "core_hours_end_time": 54000,
        "core_hours_start_time": 28800,
    }


@pytest.fixture
def ibis_hawaii_org_without_core_hours():
    return {
        "reply_days": 10,
        "asset_usage_episode_months": 3,
        "name": "Ibis Office",
        "energy_management": True,
        "dp60_days": 45,
        "is_active": True,
        "price_model_id": 37,
        "updated_at": 1554809319,
        "packet_days": 1,
        "org_type": "customer",
        "mode": "normal",
        "summary_meas_86400_years": 10,
        "summary_meas_3600_months": 120,
        "timezone_name": "Pacific/Honolulu",
        "asset_management": True,
        "id": 8004,
        "core_hours_start_time": None,
        "core_hours_end_time": None,
    }


@pytest.fixture
def az_maryland_org():
    return {
        "asset_management": "True",
        "energy_management": "True",
        "mainly_lab_equipment": "True",
        "dp60_days": "False",
        "core_hours_start_time": 28800,
        "core_hours_end_time": 64800,
        "id": 9499,
        "name": "CBRE AstraZeneca Gaithersburg",
        "timezone_name": "America/New_York",
        "is_active": "True",
        "mode": "normal",
        "note": "None",
        "flags": "None",
        "org_type": "customer",
        "mode_params": {"demo_days": "365", "pilot_days": "45"},
        "data_window_start_utc": "None",
        "data_window_end_utc": "None",
        "features_tier": 1,
    }


@pytest.fixture
def swedish_org_positive_utc():
    return {
        "asset_management": "True",
        "energy_management": "True",
        "mainly_lab_equipment": "True",
        "dp60_days": "False",
        "core_hours_start_time": 28800,
        "core_hours_end_time": 64800,
        "id": 9499,
        "name": "Random Company",
        "timezone_name": "Europe/Stockholm",
        "is_active": "True",
        "mode": "normal",
        "note": "None",
        "flags": "None",
        "org_type": "customer",
        "mode_params": {"demo_days": "365", "pilot_days": "45"},
        "data_window_start_utc": "None",
        "data_window_end_utc": "None",
        "features_tier": 1,
    }
