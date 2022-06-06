import os


class Command:

    @staticmethod
    def run(commend):
        stream = os.popen(commend)
        return stream.read()

    def disconnect(self):
        result = self.run('warp-cli disconnect')
        if result == 'Success':
            return True
        return False

    def connect(self):
        result = self.run('warp-cli connect')
        if result == 'Success':
            return True
        return False

    def status(self):
        output = self.run('warp-cli status')
        output = output.split('\n')
        for row in output:
            data = row.split(':')
            if data[0] == 'Status update':
                return data[1].strip()
        return False

    def set_mode(self, mode):
        result = self.run('warp-cli set-mode {}'.format(mode))
        if result == 'Success':
            return True
        return False

    def is_connected(self):
        status = self.status()
        if status == 'Connected':
            return True
        return False

    # def find_os(self):
