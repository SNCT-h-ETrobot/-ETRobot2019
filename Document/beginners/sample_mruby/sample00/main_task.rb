class MainTask

  PWM_MAX = 100
  PWM = PWM_MAX / 6
  DURATION = 2000

  def initialize
    @left_wheel = EV3RT_TECS::Motor.new(:port_c)
    @right_wheel = EV3RT_TECS::Motor.new(:port_b)
    # C++の__FILE__の代わりにクラス名を表示する
    Util::Display.init("sample00 " + self.class.to_s)
  end

  def execute
   loop do
      Util::Display.message("Forwarding...", 2)
      @left_wheel.power = PWM
      @right_wheel.power = PWM
      EV3RT_TECS::RTOS.delay(DURATION)

      Util::Display.message("Backwarding...", 2)
      @left_wheel.power = -PWM
      @right_wheel.power = -PWM
      EV3RT_TECS::RTOS.delay(DURATION)

      # 左ボタンを長押し、それを捕捉する
      break if EV3RT_TECS::Button[:left].pressed?      
    end

    Util::Display.message("Stopped.", 2)
    @left_wheel.stop
    @right_wheel.stop
    # 左ボタンの長押しが終わるまで待つ
    while EV3RT_TECS::Button[:left].pressed?
    end
  end

end

MainTask.new.execute
