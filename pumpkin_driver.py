import time
import sys
import select

class pumpkin_driver:
    def __init__(self):
        self.viper1 = [2, 3, 4, 17]
        self.action_time = 0
        
    def parse_line(self, line_in):
        '''
        This function takes in a command string `line_in`.
        Allowed strings are:
        - 'forward'
        - 'reverse'
        - 'left'
        - 'right'
        - 'stop'
        '''

    def forward(self, array):
	GPIO.output(array[0], True)
	GPIO.output(array[1], False)
	GPIO.output(array[2], True)
	GPIO.output(array[3], False)
	
        if line_in is 'forward':
            self.forward(self.viper1)
            self.action_time = time.time()

    def stop(self, array):
	GPIO.output(array[0], False)
	GPIO.output(array[1], False)
	GPIO.output(array[2], False)
	GPIO.output(array[3], False)


if __name__ == '__main__':
    jim = pumpkin_driver()
    while True:
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = sys.stdin.readline()
            if line:
                jim.parse_line(line)
            else:
                print "eof"
                exit(0)
        else:
            if time.time() - jim.action_time > 1:
                jim.stop(jim.viper1)

        time.sleep(.01)
