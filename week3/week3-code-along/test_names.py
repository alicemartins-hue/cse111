from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
        assert make_full_name("Sally", "Brown") == "Brown; Sally"
        assert make_full_name("Maria-Joaquina", "Candido") == "Candido; Maria-Joaquina"
        assert make_full_name("Li","Chang") == "Chang; Li"
        assert make_full_name("Francesca","De Lorenzo") == "De Lorenzo; Francesca"


def test_extract_family_name():
        assert extract_family_name("Brown; Sally") == "Brown"
        assert extract_family_name("De Lorenzo; Francesca") == "De Lorenzo"
        assert extract_family_name("Chang; Li") == "Chang"
        assert extract_family_name("Candido; Maria-Joaquina") == "Candido"

def test_extract_given_name():
        assert extract_given_name("Brown; Sally") == "Sally"
        assert extract_given_name("De Lorenzo; Francesca") == "Francesca"
        assert extract_given_name("Chang; Li") == "Li"
        assert extract_given_name("Candido; Maria-Joaquina") == "Maria-Joaquina"




#call the main function that is part of pytest so that the 
#computer will execute the test function in this file.
pytest.main(["-v","--tb=line","-rN", __file__])