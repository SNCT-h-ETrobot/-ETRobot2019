/*
 *  MainTask.java (for leJOS EV3)
 *  Created on: 2016/06/11
 *  Copyright (c) 2016 Embedded Technology Software Design Robot Contest
 */
package jp.etrobo.ev3.sample02;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

/**
 * leJOS EV3 用 Java
 */
public class MainTask {
    private Walker         walker;

    // スケジューラ
    private ScheduledExecutorService scheduler;
    private ScheduledFuture<?> futureWalker;
    private CountDownLatch countDownLatch;

    // タスク
    private WalkerTask  walkerTask;

    /**
     * コンストラクタ。
     * スケジューラとタスクオブジェクトを作成。
     */
    public MainTask() {
        walker = new Walker();

        scheduler  = Executors.newScheduledThreadPool(1);
        walkerTask  = new WalkerTask(walker, countDownLatch);
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
    	walker.init();
        futureWalker = scheduler.scheduleAtFixedRate(walkerTask, 0, 2000, TimeUnit.MILLISECONDS);
    }

    /**
     * 走行終了時のタスク終了後処理。
     */
    public void stop () {
        if (futureWalker != null) {
            futureWalker.cancel(true);
        }
        walker.terminate();
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