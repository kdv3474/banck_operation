import pytest
from conftest import sample_data
from scr.masks import get_mask_card_number

def test_get_mask_card_number(sample_data):
    number_card, mask_new = sample_data
    assert get_mask_card_number(number_card) == mask_new