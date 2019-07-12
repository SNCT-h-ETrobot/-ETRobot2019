/*
 *  MainTask.java (for leJOS EV3)
 *  Created on: 2016/06/11
 *  Copyright (c) 2016 Embedded Technology Software Design Robot Contest
 */
package jp.etrobo.ev3.sample01;

/**
 * leJOS EV3 用 Java
 */
public class MainTask {

    /**
     * メイン
     */
    public static void main(String[] args) {

    	Walker walker = new Walker();
    	walker.run();
    }
}