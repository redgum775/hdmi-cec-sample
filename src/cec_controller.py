import cec
import time

class CecController:
    """
    HDMI CECを経由してTVを制御する
    """
    def __init__(self):
        self.cec = cec.init()
        self.tv = cec.Device(cec.CECDEVICE_TV)
    
    def turn_on_tv(self):
        """
        TVの電源をオンにする
        """
        if not self.tv.is_on():
            self.tv.power_on()
    
    def turn_off_tv(self):
        """
        TVの電源をオフにする
        """
        if self.tv.is_on():
            self.tv.standby()
    
    def input_switching(self, parameters=b'\x20\x00'):
        """
        アクティブ入力ソースを設定する

        Parameters:
        ---
        parameters : bytes
            アクティブにしたい入力ソース（default：入力２（2.0.0.0））
        ---
        """
        self.destination = cec.CECDEVICE_BROADCAST
        self.opcode = cec.CEC_OPCODE_ACTIVE_SOURCE
        self.parameters = parameters
        cec.transmit(self.destination, self.opcode, self.parameters)
    
    def adjusting_volume(self, volume):
        """
        ボリュームを調整する

        Parameters:
        ---
        volume : int
            音量の増減量（＋で音量アップ、－で音量ダウン）
        ---
        """
        if volume > 0:
            for _ in range(volume):
                cec.volume_up()
                time.sleep(1)
        elif volume < 0:
            for _ in range(-volume):
                cec.volume_down()
                time.sleep(1)

if __name__ == '__main__':
    cec_controller = CecController()
    cec_controller.turn_on_tv()
    cec_controller.input_switching(parameters=b'\x40\x00')