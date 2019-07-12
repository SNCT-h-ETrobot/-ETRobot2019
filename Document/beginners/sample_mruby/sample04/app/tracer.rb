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
  
  def run
    kp = 0.83        # 比例係数
    target = 10      # 白・黒の中間値
    bias = 0

    Util::Display.message("running...", 2)
    diff = @color_sensor.reflect - target
    turn = kp * diff + bias
    @left_wheel.power = PWM - turn
    @right_wheel.power = PWM + turn
  end

end