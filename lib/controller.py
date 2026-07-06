import fischertechnik.factories as txt_factory

txt_factory.init()
txt_factory.init_motor_factory()
txt_factory.init_servomotor_factory()
txt_factory.init_counter_factory()


TXT = txt_factory.controller_factory.create_graphical_controller()
TXT_M1_encodermotor = txt_factory.motor_factory.create_encodermotor(TXT, 1)
TXT_M2_encodermotor = txt_factory.motor_factory.create_encodermotor(TXT, 2)
TXT_M3_encodermotor = txt_factory.motor_factory.create_encodermotor(TXT, 3)
TXT_M4_encodermotor = txt_factory.motor_factory.create_encodermotor(TXT, 4)
TXT_S1_servomotor = txt_factory.servomotor_factory.create_servomotor(TXT, 1)
TXT_C1_motor_step_counter = txt_factory.counter_factory.create_encodermotor_counter(TXT, 1)
TXT_C1_motor_step_counter.set_motor(TXT_M1_encodermotor)
TXT_C2_motor_step_counter = txt_factory.counter_factory.create_encodermotor_counter(TXT, 2)
TXT_C2_motor_step_counter.set_motor(TXT_M2_encodermotor)
TXT_C3_motor_step_counter = txt_factory.counter_factory.create_encodermotor_counter(TXT, 3)
TXT_C3_motor_step_counter.set_motor(TXT_M3_encodermotor)
TXT_C4_motor_step_counter = txt_factory.counter_factory.create_encodermotor_counter(TXT, 4)
TXT_C4_motor_step_counter.set_motor(TXT_M4_encodermotor)
txt_factory.initialized()