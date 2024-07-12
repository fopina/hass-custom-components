from tuya_sharing import (
    Manager,
    SharingTokenListener,
)

from local_tuya_config import (
    TUYA_CLIENT_ID,
    CONF_USER_CODE,
    CONF_TERMINAL_ID,
    CONF_TOKEN_INFO,
)

CONF_ENDPOINT = 'https://apigw.tuyaeu.com'

class TokenListener(SharingTokenListener):
    def update_token(self, token_info: dict[str, any]):
        global CONF_TOKEN_INFO
        CONF_TOKEN_INFO = {
            "t": token_info["t"],
            "uid": token_info["uid"],
            "expire_time": token_info["expire_time"],
            "access_token": token_info["access_token"],
            "refresh_token": token_info["refresh_token"],
        }

token_listener = TokenListener()
manager = Manager(
    TUYA_CLIENT_ID,
    CONF_USER_CODE,
    CONF_TERMINAL_ID,
    CONF_ENDPOINT,
    CONF_TOKEN_INFO,
    token_listener,
)

print(manager.update_device_cache())

for device in manager.device_map.values():
    print(device)
