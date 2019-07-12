class Tracer

  PWM_MAX = 100
  PWM = PWM_MAX / 6
  THRESHOLD = 20

  # コンストラクタ
  #
  # 引数でポートを渡せる、省略時はデフォルトのポートを使う
  def initialize(left_motor_port=:port_c,
                 right_motor_port=:port_b,
                 color_port=:port_3)
    @left_wheel = EV3RT_TECS::Motor.new(left_motor_port)
    @right_wheel = EV3RT_TECS::Motor.new(right_motor_port)
    @color_sensor = EV3RT_TECS::ColorSensor.new(color_port)
  end

  def init
    Util::Display.init(self.class.to_s)
  end

  def terminate
    Util::Display.message("Stopped", 2)
    @right_wheel.stop
    @left_wheel.stop
  end
  
  def calc_prop_value
    kp = 0.83        # <1>
    target = 10      # <2>
    bias = 0
    diff = @color_sensor.reflect - target  # <3>
    result = kp * diff + bias             # <4>
  end

  def run
    Util::Display.message("running...", 2)
    turn = calc_prop_value
    pwm_l = PWM - turn
    pwm_r = PWM + turn
    @left_wheel.power = pwm_l
    @right_wheel.power = pwm_r
  end

end