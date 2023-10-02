from pyradios import RadioBrowser

from models import Radio


class RadioBackend:
    def __init__(self):
        self.rb = RadioBrowser()

    def get_radios(self):
        radios = self.rb.search(name="BBC", name_exact=False)
        result: list[Radio] = []
        for radio in radios:
            result.append(Radio(
                image=radio['favicon'],
                title=radio['name'],
                subtitle=radio['country'] + " | " + radio['language'],
                votes=radio['votes'],
                audio_url=radio['url_resolved'],
            ))
        return result
