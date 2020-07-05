""" V0.9--cleaning coding"""
import sys
import os

from flask_app.parse_question import parsing


def test_parsing():
    """This function testing if the module parse_question is correctly"""
    results = ['musée', "d'art", "d'histoire", 'de', 'Fribourg,']
    assert (
        parsing(
            "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
        )
        == results
    )
