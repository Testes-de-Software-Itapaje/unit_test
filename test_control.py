import pytest

from control import Control
from exceptions import ChannelError


def test_create_control():
    c = Control()
    assert c.on == False
    assert c.channel == 3
    assert c.volume == 5

def test_create_control_2():
    c = Control()
    assert c.on == False and c.channel == 3 and c.volume == 5

def test_change_channel_over_100():
    c = Control()
    with pytest.raises(ChannelError) as error:
        c.channel = 101
    assert str(error.value) == 'Canal deve ser entre 1 e 100'