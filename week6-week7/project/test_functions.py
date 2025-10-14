from pytest import approx
import pytest

from readinglife_calculator import add_books,BOOKS, sum_page, read_time, character_life, life, days_reading


def test_add_books_and_sum_page():
    BOOKS.clear()

    add_books("Dune", 500)
    add_books("Mistborn", 700)

    assert "Dune" in BOOKS
    assert BOOKS["Dune"] == 500
    assert sum_page() == 1200

def test_read_time():
    BOOKS.clear()
    add_books("Book A",120)

    minutes_per_page = 2
    hours = read_time(minutes_per_page)

    assert hours == pytest.approx(4)
    assert hours > 0
    assert isinstance(hours, float)





pytest.main(["-v", "--tb=line", "-rN", __file__])
