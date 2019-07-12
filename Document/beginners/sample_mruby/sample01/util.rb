# 演習用のユーティリティモジュール
# 
# Displayクラスのみの場合はファイル名もdisplay.rb が適当ですが、
# C++の教材に合わせるためと、ユーティリティとして使えるクラスを追加
# して使えるようutil.rbとしてます

module Util
  # 画面にメッセージを表示する
  class Display

    EV3_LCD_WIDTH = 178
    
    # 初期処理用
    # @params str String
    def self.init(str = "")
      EV3RT_TECS::LCD.font = :medium
      EV3RT_TECS::LCD.draw(str, 0, 1)
    end

    # 行単位で引数の文字列を表示
    # @params str String 表示する文字列
    # @params line Integer 20ドットごとの行番号（1から5）
    def self.message(str, line)
      line_height = 16
      EV3RT_TECS::LCD.fill_rect(0, line * line_height, EV3_LCD_WIDTH, line_height, :white)
      EV3RT_TECS::LCD.draw(str, 0, line)
    end
  end
end
