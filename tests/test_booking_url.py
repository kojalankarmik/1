import datetime
import pytest

# Assuming the function 'build_booking_url' is imported from the module
# from your_module import build_booking_url

# Example tests for the build_booking_url function

def test_build_booking_url_without_parameters():
    expected_url = "https://example.com/booking"
    assert build_booking_url() == expected_url


def test_build_booking_url_with_source_tag():
    expected_url = "https://example.com/booking?source=testing"
    assert build_booking_url(source='testing') == expected_url


def test_build_booking_url_with_utm_parameters():
    expected_url = "https://example.com/booking?utm_source=google&utm_medium=cpc"
    assert build_booking_url(utm_source='google', utm_medium='cpc') == expected_url


def test_build_booking_url_with_date_formatting():
    # Given a specific date
    test_date = datetime.datetime(2026, 2, 14)
    expected_url = f"https://example.com/booking?date={test_date.strftime('%Y-%m-%d')}"
    assert build_booking_url(date=test_date) == expected_url
