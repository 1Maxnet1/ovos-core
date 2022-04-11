from ovos_plugin_manager.tts import OVOSTTSFactory, load_tts_plugin
from mycroft.configuration import Configuration
from ovos_plugin_manager.templates.tts import TTS, RemoteTTS, \
    RemoteTTSException, RemoteTTSTimeoutException

class TTSFactory(OVOSTTSFactory):
    @staticmethod
    def create(config=None):
        config = config or Configuration.get()
        return OVOSTTSFactory.create(config)
