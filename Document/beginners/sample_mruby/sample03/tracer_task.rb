include EV3RT_TECS

class TracerTask

  def initialize
    begin
      @tracer = Tracer.new(:port_c, :port_b, :port_3)
      @tracer.init
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
          @tracer.run

          # 周期ハンドラから起床されるのを待つ
          EV3RT_TECS::RTOS.sleep
        end
      end #loop
      @tracer.terminate

    rescue => e
      EV3RT_TECS::LCD.error_puts e # エラー内容がLCDに表示される
    end
  end
end

TracerTask.new.execute
