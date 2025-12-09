import pyvts
from body_interface import BodyInterface

class VTubeStudioBody(BodyInterface):
    def __init__(self):
        # Your specific Hotkey IDs mapped to English names
        self.expression_map = {
            "watermark_off": "6145dd7b4fe942c58fc3fb42c4f09dd5", # 水印关闭
            "ears_off": "6c2e0ed63a0e4e86b8a3767d1cc21585",      # 兽耳关闭
            "ponytail_right": "ae2c0c5b879847c3a1aaba7788aa6848", # 右马尾
            "basic_gestures": "04796c76be374e2186b07681a5d5133f", # 基础手势
            "jacket_waist": "34ad98e1e59a40649a3bc504252b7489",   # 外套系腰
            "tail_toggle": "03615b3343614d9fbd4a7ad37c9632a5",    # 尾巴开关
            "ponytail_left": "ae0d58eabc794eb6ace0b11ed5f9afd2",  # 左马尾
            "phone_neck": "672fdcd9d7a145b2afe3811ca6b40ecb",     # 挂脖手机
            "star_eyes": "8ba834f3aff44bb2965789261477e72a",      # 星星眼
            "heart_hands": "e9ec7893d54d4cd7b810e99486aa1b46",    # 比心手
            "heart_eyes": "1bec327624424067a25cb84b1c46071e",     # 爱心眼
            "mask_white": "ddb88fdc29974627bfbb50ba7af27606",     # 白色口罩
            "pocky_flavor": "a6bf3893faf146e292160157db3dc281",   # 百奇口味切换
            "pocky_hand": "41f060f183854520a8568ef29180a4c2",     # 百奇手
            "glasses": "d9094d84d76948c0a683392269c624fc",        # 眼镜
            "jacket_wear": "8c819c14c99c4044938e2eb49aab25db",    # 穿外套
            "mask_pink": "931fd1380f134c5d9bd45a3e3106dc2b",      # 粉色口罩
            "blush": "e3cbe887470142c693cd9b4d1a736bd0",          # 脸红
            "selfie_hand": "9f6dbcac8eae415299b1cd62ea044fe7",    # 自拍手
            "flying_head_01": "b124ff8ce9f64ee1a0059637d29d6eac", # 飞头01
            "flying_head_02": "8ee87bea48e04b40a1067b751cbea620", # 飞头02
            "dark_face": "d6bd3ca0cc944c069057853bd1bbb06f",      # 黑脸
            "mask_black": "82710441629948d08466fe230c1e8e08",     # 黑色口罩
            "clear_all": "58e5e70d5cdf451e9640da577e0003d3"       # 清除所有按键表情
        }
        
        self.plugin_info = {
            "plugin_name": "MARIE Core",
            "developer": "Mansal",
            "authentication_token_path": "./token.txt"
        }
        self.vts = pyvts.vts(plugin_info=self.plugin_info)

    async def connect(self):
        print("[Body-VTS] Connecting to VTube Studio...")
        await self.vts.connect()
        await self.vts.request_authenticate_token()
        await self.vts.request_authenticate()
        print("[Body-VTS] Connected successfully.")
        
        # AUTOMATICALLY TURN OFF WATERMARK
        print("[Body-VTS] Removing Watermark...")
        await self.trigger_expression("watermark_off")

    async def trigger_expression(self, expression_name: str):
        hotkey_id = self.expression_map.get(expression_name)
        if hotkey_id:
            await self.vts.request(
                self.vts.vts_request.requestTriggerHotKey(hotkey_id)
            )
        else:
            print(f"[Body-VTS] Warning: Expression '{expression_name}' not found.")

    async def close(self):
        await self.vts.close()