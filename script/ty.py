from base_script import BaseScript

package_name = 'com.netease.pm02'
class Ty(BaseScript):
    def start(self):
        self.d.app_start(package_name)
        return 'end'

    def end(self):
        print('i am over!')
        return 'end'


ty = Ty('192.168.31.184','0')
ty.run()
