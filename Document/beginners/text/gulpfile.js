// gulpプラグインの読みこみ
var gulp = require('gulp');
var gulp_asciitocor = require('gulp-asciidoctor');

// browser-syncのプラグインの読み込み
var browserSync = require("browser-sync");

// タスクの設定
gulp.task("browserSyncTask", function () {
    browserSync({
        server: {
            baseDir: "." // ルートとなるディレクトリを指定
        }
    });

    // srcフォルダ以下のファイルを監視
    gulp.watch("*.html", function() {
        browserSync.reload();   // ファイルに変更があれば同期しているブラウザをリロード
    });
});

// asciidoctor -T ~/github/asciidoctor-deck.js/templates/haml/
// のためのタスクを作りたい（コマンドラインの-Tオプションの渡し方がわからん）
