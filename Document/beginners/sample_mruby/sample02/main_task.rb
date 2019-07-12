# C++ 教材との違い
# C++の教材ではWalkerクラスのインスタンスをグローバル変数として作成していますが、
# mruby ではWalkerタスクの中でインスタンス変数として作成します。

class MainTask

  def initialize
    # C++の__FILE__の代わりにクラス名を表示する
    Util::Display.init("sample02 " + self.class.to_s)
  end

  def execute
    @WakeupTask = TECS::TsTask.new( 'MrubyWakeupTaskeTaskBridge' )
    @Wakeupper = TECS::TsCyclic.new( 'TaskCyclicWakeuppereCyclicBridge' )
    # 周期ハンドラから起動されるタスクを起動
    @WakeupTask.activate

    # 周期ハンドラ開始
    @Wakeupper.start

    # Walkerタスクより起床されるまで待つ
    RTOS.sleep

    # 周期ハンドラ停止
    @Wakeupper.stop
  end

end

MainTask.new.execute
