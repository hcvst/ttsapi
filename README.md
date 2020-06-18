

# ttsapi
A caching text-to-speech server using Google Cloud text-to-speech API

```
hcvst at eybuntu in ~/dev/python/ttsapi/ttsapi (master●●●) (ttsapi-EFmfwQLo) 
$ GOOGLE_APPLICATION_CREDENTIALS=/home/hcvst/dev/google-service-account-text2speech.token AUDIO_DIR=/tmp ROOT_URL=http://127.0.0.1:8000 AUTH_TOKEN=123 gunicorn server:app
[2020-06-18 22:34:34 +0200] [4481] [INFO] Starting gunicorn 20.0.4
[2020-06-18 22:34:34 +0200] [4481] [INFO] Listening at: http://127.0.0.1:8000 (4481)
[2020-06-18 22:34:34 +0200] [4481] [INFO] Using worker: sync
[2020-06-18 22:34:34 +0200] [4484] [INFO] Booting worker with pid: 4484

```

## Environment variables
- `AUDIO_DIR` - absolute path of where to save audio files to 
- `AUTH_TOKEN` - Token clients need send in `Authentication` header
- `ROOT_URL` - server's address e.g. http://example.com:1234
- `GOOGLE_APPLICATION_CREDENTIALS` - Google credentials json file

## Google credentials
Please consult https://cloud.google.com/text-to-speech/docs/reference/libraries#setting_up_authentication.

## LD_LIBRARY_PATH
If you an encounter `ImportError: libstdc++.so.6: cannot open shared object file` please point 
`LD_LIBRARY` path at the directory containing the hared library e.g.:

`LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/`