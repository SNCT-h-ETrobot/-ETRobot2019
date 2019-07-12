class Walker

  PWM_MAX = 100
  PWM = PWM_MAX / 6
  DURATION = 2000

  # コンストラクタ
  #
  # 引数でポートを渡せる、省略時はデフォルトのポートを使う
  def initialize(left_motor_port=:port_c,
                 right_motor_port=:port_b,
                 direction)
    @left_wheel = EV3RT_TECS::Motor.new(left_motor_port)
    @right_wheel = EV3RT_TECS::Motor.new(right_motor_port)
    @forwarding = direction
  end

  def init
    Util::Display.init("sample02 " + self.class.to_s)
  end

  def terminate
    Util::Display.message("Stopped", 2)
    @right_wheel.stop
    @left_wheel.stop
  end
  
  def run
    if @forwarding
      Util::Display.message("Forwarding...", 2)
      @left_wheel.power = PWM
      @right_wheel.power = PWM
      @forwarding = false
    else
      Util::Display.message("Backwarding...", 2)
      @left_wheel.power = -PWM
      @right_wheel.power = -PWM
      @forwarding = true
    end
  end

end
