/*
 *  TracerTask.java (for leJOS EV3)
 *  Created on: 2016/06/11
 *  Copyright (c) 2016 Embedded Technology Software Design Robot Contest
 */
package jp.etrobo.ev3.sample05;

import java.util.concurrent.CountDownLatch;

import jp.etrobo.ev3.sample05.app.Tracer;
import lejos.hardware.Button;

/**
 * Tracer を制御するタスク。
 */
public class TracerTask implements Runnable {
	private Tracer tracer;
    private CountDownLatch countDownLatch;

    /**
	 * コンストラクタ。
	 */
	public TracerTask(Tracer tracer, CountDownLatch countDownLatch) {
		this.tracer = tracer;
		this.countDownLatch = countDownLatch;
	}

    /**
     * Tracerの制御。
     */
    @Override
    public void run() {
        if (Button.LEFT.isDown()) {
        	countDownLatch.countDown();
        }else{
        	tracer.run();
        }
    }
}