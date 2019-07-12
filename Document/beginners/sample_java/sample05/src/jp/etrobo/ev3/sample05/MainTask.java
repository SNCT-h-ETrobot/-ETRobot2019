/*
 *  MainTask.java (for leJOS EV3)
 *  Created on: 2016/06/11
 *  Copyright (c) 2016 Embedded Technology Software Design Robot Contest
 */
package jp.etrobo.ev3.sample05;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

import jp.etrobo.ev3.sample05.app.Tracer;

/**
 * leJOS EV3 用 Java
 */
public class MainTask {
    private Tracer         tracer;

    // スケジューラ
    private ScheduledExecutorService scheduler;
    private ScheduledFuture<?> futureTracer;
    private CountDownLatch countDownLatch;
    // タスク
    private TracerTask  tracerTask;

    /**
     * コンストラクタ。
     * スケジューラとタスクオブジェクトを作成。
     */
    public MainTask() {
        tracer = new Tracer();
        scheduler  = Executors.newScheduledThreadPool(1);
        countDownLatch = new CountDownLatch(1);
        tracerTask  = new TracerTask(tracer, countDownLatch);
    }

    /**
     * 終了待機
     */
    public void sleep() {
    	try{
    		countDownLatch.await();
    	}catch (InterruptedException ex){

    	}
    }

    /**
     * 走行開始時の作業スケジューリング。
     */
    public void start() {
    	tracer.init();
        futureTracer = scheduler.scheduleAtFixedRate(tracerTask, 0, 50, TimeUnit.MILLISECONDS);
    }

    /**
     * 走行終了時のタスク終了後処理。
     */
    public void stop () {
        if (futureTracer != null) {
            futureTracer.cancel(true);
        }
        tracer.terminate();
    }

    /**
     * スケジューラのシャットダウン。
     */
    public void shutdown() {
        scheduler.shutdownNow();
    }

    /**
     * メイン
     */
    public static void main(String[] args) {
    	MainTask mainTask = new MainTask();
        mainTask.start();
    	mainTask.sleep();
        mainTask.stop();
    	mainTask.shutdown();
    }
}