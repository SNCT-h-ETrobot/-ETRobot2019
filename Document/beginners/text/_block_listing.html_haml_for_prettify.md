asciidoctor-deck.js/templates/haml

block_listing.html.haml
は、Prettify の行番号の開始行を調整する部分を修正してある。

その後、
linenums,start=XX
linenums=XX
のどちらのタイプの書式にマッチするよう、再度修正した

      - when 'prettify'
        - nums = attr :linenums
        - pre_class = ['prettyprint']
        - pre_class << "linenums:#{nums}" if attr? :linenums
        - pre_class << language if language
        - pre_class << "language-#{language}" if language
        - code_class = nil


      - when 'prettify'
        - nums = attr :linenums
        - nums = attr :start
        - pre_class = ['prettyprint']
        - pre_class << "linenums:#{nums}" if attr? :start
        - pre_class << language if language
        - pre_class << "language-#{language}" if language
        - code_class = nil
