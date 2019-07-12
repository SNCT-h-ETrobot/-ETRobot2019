/*
 *  Walker.java (for leJOS EV3)
 *  Created on: 2016/06/11
 *  Copyright (c) 2016 Embedded Technology Software Design Robot Contest
 */
package jp.etrobo.ev3.sample01;

import lejos.hardware.Button;
import lejos.hardware.lcd.LCD;
import lejos.hardware.port.MotorPort;
import lejos.hardware.port.TachoMotorPort;
import lejos.utility.Delay;

public class Walker {
    private TachoMotorPort leftWheel;
    private TachoMotorPort rightWheel;

	private final int pwm = TachoMotorPort.MAX_POWER / 6;
	private final long duration = 2000;

    Walker(){
    	leftWheel = MotorPort.C.open(TachoMotorPort.class);
    	rightWheel = MotorPort.B.open(TachoMotorPort.class);
    }

    public void run(){
    	LCD.drawString("Walker", 0, 2);
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
