from tuya_sharing import (
    Manager,
    SharingTokenListener,
    CustomerDevice,
)
from tuya_sharing.device import DeviceStatusRange

from local_tuya_config import (
    TUYA_CLIENT_ID,
    CONF_USER_CODE,
    CONF_TERMINAL_ID,
    CONF_TOKEN_INFO,
    MY_ACCESS_KEY,
    MY_ACCESS_SECRET,
    CONF_TEST_DEVICE_ID,
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

# token_listener = TokenListener()
# manager = Manager(
#     TUYA_CLIENT_ID,
#     CONF_USER_CODE,
#     CONF_TERMINAL_ID,
#     CONF_ENDPOINT,
#     CONF_TOKEN_INFO,
#     token_listener,
# )

# print(manager.update_device_cache())

# md = None
# for device in manager.device_map.values():
#     print(device)
#     if device.product_id == 'fbvia0apnlnattcy':
#         md = device


# print('===')
# print(md)
# print(md.status)


from tuya_connector import (
	TuyaOpenAPI,
)

ACCESS_ID = MY_ACCESS_KEY
ACCESS_KEY = MY_ACCESS_SECRET

# Init OpenAPI and connect
openapi = TuyaOpenAPI(CONF_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Call any API from Tuya
response = openapi.get(f"/v1.0/devices/{CONF_TEST_DEVICE_ID}/statistics/total?code=add_ele", dict())
print(response)
