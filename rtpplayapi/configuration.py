class RTPPlayConfig:
    def __init__(self, config):
        rtp_play_json_config = config.get("config", {})
        self.AUTH_URL_ENDPOINT = rtp_play_json_config.get("auth_url", "")
        self.BASE_API_URL_ENDPOINT = rtp_play_json_config.get("base_api_url", "")
        self.SEARCH_URL_ENDPOINT = rtp_play_json_config.get("search_url", "")
        self.PEER5 = rtp_play_json_config.get("peer5", "") == 1
        self.DVR_CHANNELS = rtp_play_json_config.get("dvr_channels", [])
        related_apps_android = rtp_play_json_config.get("related_apps_android", {})
        self.APPS_PALCO = related_apps_android.get("palco", 0)
        self.APPS_ZIGZAG = related_apps_android.get("zigzag", 0)
        self.APPS_NOTICIAS = related_apps_android.get("noticias", 0)
        self.APPS_ARQUIVOS = related_apps_android.get("arquivos", 0)
        self.APPS_ESTUDO_EM_CASA = related_apps_android.get("estudoemcasa", 0)
        self.MENU = [{ent["type"]: ent["title"]} for ent in config.get("menu", [])]
