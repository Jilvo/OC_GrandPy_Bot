""" V1.0--cleaning coding"""
import sys
import os
sys.path.append(f"{os.getcwd()}/flask_app/")
from parse_question import parsing


def test_parsing():
    """This function testing if the module parse_question is correctly"""
    results = ['musée', "d'art", "d'histoire", 'de', 'Fribourg,']
    assert (
        parsing(
            "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
        )
        == results
    )

def test_error():
    """This function testing """
    results = ['dhvhsvhsdvsjhjshvsbdhsvb']
    assert (
        parsing(
            "dhvhsvhsdvsjhjshvsbdhsvb"
        )
        == results
    )