from transitions import Machine
import threading

class LightSensorSystem:
    states = ['light_detected', 'no_light_detected', 'motion_detected', 'no_motion_detected', 'led_on', 'led_off', 
              'led_dimmed', 'led_brightened']







    def __init__(self):
        self.machine = Machine(model=self, states=LightSensorSystem.states, initial='led_off')
        self.no_motion_timer = None





        self.machine.add_transition(trigger='detect_light', source='*', dest='light_detected', after='disable_motion_detector')
        self.machine.add_transition(trigger='detect_light', source='*', dest='light_detected', after='turn_off_led')

        self.machine.add_transition(trigger='no_light', source='*', dest='no_light_detected', after='enable_motion_detector')
        self.machine.add_transition(trigger='no_light', source='*', dest='no_light_detected', after='turn_on_led')

        self.machine.add_transition(trigger='detect_motion', source='*', dest='motion_detected', after='turn_on_led')
        self.machine.add_transition(trigger='detect_motion', source='*', dest='no_motion_detected', after='start_no_motion_timer')
        
        self.machine.add_transition(trigger='no_motion', source='motion_detected', dest='no_motion_detected', after='dim_led')
        self.machine.add_transition(trigger='no_motion', source='*', dest='no_motion_detected', after='start_no_motion_timer')

        self.machine.add_transition(trigger='timer_expired', source='*', dest='led_off', after='turn_off_led')
        self.machine.add_transition(trigger='timer_expired', source='*', dest='led_dimmed', after='dim_led')
        
        self.machine.add_transition(trigger='










    def turn_off_led(self):
        print("LED turned off")

    def turn_on_led(self):
        print("LED turned on")
        if self.no_motion_timer:
            self.no_motion_timer.cancel()

    def dim_led(self):
        print("LED dimmed by 50%")

    def disable_motion_detector(self):
        print("Motion detector disabled")

    def enable_motion_detector(self):
        print("Motion detector enabled")

    def start_no_motion_timer(self):
        print("No motion detected, starting timer")
        if self.no_motion_timer:
            self.no_motion_timer.cancel()
        self.no_motion_timer = threading.Timer(420.0, self.no_motion_timer_expired)  # 7 minutes = 420 seconds
        self.no_motion_timer.start()

    def no_motion_timer_expired(self):
        print("No motion timer expired, turning off LED")
        self.timer_expired()

# Example usage
system = LightSensorSystem()
system.no_light()  # LED turned on
system.no_light()  # Motion detector enabled

system.detect_motion()  # LED turned on
system.no_motion()  # No motion detected, starting timer, LED dimmed by 50%
system.detect_light()  # Motion detector disabled
