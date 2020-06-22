import json
import os
import pathlib
from urllib.parse import urljoin

import falcon
from . import config, tts, utils


class TextToSpeech(object):
    def on_post(self, req, resp):
        if req.get_header("Authorization") != config.AUTH_TOKEN:
            raise falcon.HTTPUnauthorized()

        try:
            text = json.load(req.bounded_stream)["text"]
        except Exception:
            raise falcon.HTTPBadRequest(
                'Request requires JSON body {"text": "text to synthesize"}.'
            )

        audiofile = self.text_to_audiofile(text)
        resp.content_type = "application/json"
        resp.body = json.dumps(
            dict(
                href=urljoin(config.EXTERNAL_URL, f"{config.WWW_AUDIO_DIR}/{audiofile}")
            )
        )

    def text_to_audiofile(self, text):
        filename = utils.generate_filename(text, "mp3")
        path = os.path.join(config.AUDIO_DIR, filename)
        if not pathlib.Path(path).is_file():
            audio = tts.text_to_mp3(text)
            with open(path, "wb") as out:
                out.write(audio)
        return filename


app = falcon.App()
app.add_route("/synthesize", TextToSpeech())
app.add_static_route(config.WWW_AUDIO_DIR, config.AUDIO_DIR)
