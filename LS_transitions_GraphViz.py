from transitions import Machine
from transitions.extensions import GraphMachine

class LightSensorSystem:
    states = ['light_detected', 'no_light_detected', 'motion_detected', 'no_motion_detected', 'led_on', 'led_off']

    def __init__(self):
        self.machine = GraphMachine(model=self, states=LightSensorSystem.states, initial='led_off')

        self.machine.add_transition(trigger='detect_light', source='*', dest='light_detected', after='turn_off_led')
        self.machine.add_transition(trigger='no_light', source='*', dest='no_light_detected', after='turn_on_led')
        self.machine.add_transition(trigger='detect_motion', source='*', dest='motion_detected', after='turn_on_led')
        self.machine.add_transition(trigger='no_motion', source='*', dest='no_motion_detected', after='dim_led')

    def turn_off_led(self):
        print("LED turned off")

    def turn_on_led(self):
        print("LED turned on")

    def dim_led(self):
        print("LED dimmed by 50%")

# Example usage
system = LightSensorSystem()
system.no_light()  # LED turned on
system.detect_motion()  # LED turned on
system.no_motion()  # LED dimmed by 50%

# Export the state machine to a Graphviz dot file
system.get_graph().draw('state_machine.png', prog='dot')