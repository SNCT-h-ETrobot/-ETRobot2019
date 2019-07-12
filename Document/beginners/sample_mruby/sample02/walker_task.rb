class WalkerTask

  def initialize
    begin
      @walker = Walker.new(:port_c, :port_b, true)
      @walker.init
      @maintask = TECS::TsTask.new('MrubyMainTaskeTaskBridge')
    rescue => e
      EV3RT_TECS::LCD.error_puts e
    end
  end
  
  def execute
    begin
      loop do
        if EV3RT_TECS::Button[:left ].pressed?
          @maintask.wakeup
          break
        else
          @walker.run
          # 周期ハンドラから起床されるのを待つ
          EV3RT_TECS::RTOS.sleep
        end
      end #loop
      @walker.terminate
    rescue => e
      EV3RT_TECS::LCD.error_puts e
    end
  end

end

WalkerTask.new.execute
