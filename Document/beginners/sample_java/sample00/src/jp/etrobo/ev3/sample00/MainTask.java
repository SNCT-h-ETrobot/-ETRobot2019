/*
 *  MainTask.java (for leJOS EV3)
 *  Created on: 2016/06/11
 *  Copyright (c) 2016 Embedded Technology Software Design Robot Contest
 */
package jp.etrobo.ev3.sample00;

import lejos.hardware.Button;
import lejos.hardware.lcd.LCD;
import lejos.hardware.port.MotorPort;
import lejos.hardware.port.TachoMotorPort;
import lejos.utility.Delay;

/**
 * leJOS EV3 用 Java
 */
public class MainTask {

    /**
     * メイン
     */
    public static void main(String[] args) {
        TachoMotorPort leftWheel = MotorPort.C.open(TachoMotorPort.class);
        TachoMotorPort rightWheel = MotorPort.B.open(TachoMotorPort.class);

    	int pwm = TachoMotorPort.MAX_POWER / 6;
    	long duration = 2000;

    	LCD.drawString("MainTask", 0, 2);
        while(true){

        	LCD.drawString("Forwarding...", 0, 4);
        	leftWheel.controlMotor(pwm, TachoMotorPort.PWM_FLOAT);
        	rightWheel.controlMotor(pwm, TachoMotorPort.PWM_FLOAT);
        	Delay.msDelay(duration);

        	LCD.drawString("Backwarding...", 0, 4);
        	leftWheel.controlMotor(-pwm, TachoMotorPort.PWM_FLOAT);
        	rightWheel.controlMotor(-pwm, TachoMotorPort.PWM_FLOAT);
        	Delay.msDelay(duration);

            if (Button.LEFT.isDown()) {
            	break;
            }
        }

        LCD.drawString("Stopped.", 0, 4);
        leftWheel.setPWMMode(TachoMotorPort.STOP);
        rightWheel.setPWMMode(TachoMotorPort.STOP);
        while (Button.LEFT.isDown()) {
        	;
        }
    }
}