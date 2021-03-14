# RTPPlay-API
RTP is the portuguese public broadcaster (Rádio e Televisão de Portugal). Their platform, RTPPlay gives free access to on demand and live tv content.

This python package uses [rtpplay's](https://www.rtp.pt/play/) mobile api to fetch their content. As opposed to web scraping, this is not expected to break too often.

*This package is in no way official nor endorsed by RTP.*

## Installation
```shell
pip install rtpplayapi
```

## Usage
```python
from rtpplayapi import RTPPlayAPI

rtppapi = RTPPlayAPI()
print(rtpapi.search("offline"))
```

## Endpoints
**NOTE:** Some endpoints are missing, feel free to PR.

- get_live_tv_channels
- get_live_radio_channels
- get_slideshow
- get_collection
- get_channel_epg
- get_channel
- get_program
- get_episode
- list_episodes
- list_programs
- search

Look at the docstrings on rtpplayapi/api.py for example responses and parameter description.
