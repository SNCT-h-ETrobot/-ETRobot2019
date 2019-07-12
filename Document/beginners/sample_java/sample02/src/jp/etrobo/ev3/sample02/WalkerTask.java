/*
 *  WalkerTask.java (for leJOS EV3)
 *  Created on: 2016/06/11
 *  Copyright (c) 2016 Embedded Technology Software Design Robot Contest
 */
package jp.etrobo.ev3.sample02;

import java.util.concurrent.CountDownLatch;

import lejos.hardware.Button;

/**
 * Walker を制御するタスク。
 */
public class WalkerTask implements Runnable {
	private Walker walker;
    private CountDownLatch countDownLatch;

	/**
	 * コンストラクタ。
	 */
	public WalkerTask(Walker walker, CountDownLatch countDownLatch) {
		this.walker = walker;
		this.countDownLatch = countDownLatch;
	}

    /**
     * Walkerの制御。
     */
    @Override
    public void run() {
        if (Button.LEFT.isDown()) {
        	countDownLatch.countDown();
        }else{
            walker.run();
        }
    }
}