class MainTask

  def initialize
    begin
      @WakeupTask = TECS::TsTask.new( 'MrubyWakeupTaskeTaskBridge' )
      @Wakeupper = TECS::TsCyclic.new( 'TaskCyclicWakeuppereCyclicBridge' )
      # C++の__FILE__の代わりにクラス名を表示する
      Util::Display.init("sample04 " + self.class.to_s)
    rescue => e
        EV3RT_TECS::LCD.error_puts e # エラー内容がLCDに表示される
    end
  end

  def execute
    begin
      # 周期ハンドラから起動されるタスクを起動
      @WakeupTask.activate

      # 周期ハンドラ開始
      @Wakeupper.start

      # バックボタンが押されるのを待つ
      EV3RT_TECS::RTOS.sleep

      # 周期ハンドラ停止
      @Wakeupper.stop
    rescue => e
        EV3RT_TECS::LCD.error_puts e # エラー内容がLCDに表示される
    end
  end
end

MainTask.new.execute