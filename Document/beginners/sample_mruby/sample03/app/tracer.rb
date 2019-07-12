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
    Util::Display.message("running...", 2)
    if @color_sensor.reflect >= THRESHOLD
      @left_wheel.power = 0
      @right_wheel.power = PWM
    else
      @left_wheel.power = PWM
      @right_wheel.power = 0
    end
  end

end