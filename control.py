from exceptions import ChannelError, VolumeError
class Control:

    def __init__(self):
        self._on = False
        self._volume = 5
        self._channel = 3

    @property
    def on(self):
        return self._on

    @on.setter
    def on(self, on):
        self._on = on

    @property
    def volume(self):
        return self._volume

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel):
        if channel >= 1 and channel <= 100:
            self._channel = channel
        else:
            raise ChannelError('Canal deve ser entre 1 e 100')

    def increase_volume(self):
        if self._volume < 100:
            self._volume += 1
        else:
            raise VolumeError('Volume está no máximo!')

    def decrease_volume(self):
        if self._volume > 0:
            self._volume -= 1
        else:
            raise VolumeError('Volume está no mínimo!')

    def increase_channel(self):
        if self._channel < 100:
            self._channel += 1
        else:
            raise ChannelError('Você está no último canal!')

    def decrease_channel(self):
        if self._channel > 0:
            self._channel -= 1
        else:
            raise ChannelError('Você está no primeiro canal!')
