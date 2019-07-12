/*
 *  Walker.java (for leJOS EV3)
 *  Created on: 2016/06/11
 *  Copyright (c) 2016 Embedded Technology Software Design Robot Contest
 */
package jp.etrobo.ev3.sample02;

import lejos.hardware.lcd.LCD;
import lejos.hardware.port.MotorPort;
import lejos.hardware.port.TachoMotorPort;

public class Walker {
    private TachoMotorPort leftWheel;
    private TachoMotorPort rightWheel;

	private final int pwm = TachoMotorPort.MAX_POWER / 6;
	private boolean isForwarding = true;

    Walker(){
    	leftWheel = MotorPort.C.open(TachoMotorPort.class);
    	rightWheel = MotorPort.B.open(TachoMotorPort.class);
    }

    public void init(){
    	LCD.drawString("Walker", 0, 2);
    }
    public void run(){
        if(isForwarding == true){
        	LCD.drawString("Forwarding...", 0, 4);
        	leftWheel.controlMotor(pwm, TachoMotorPort.PWM_FLOAT);
        	rightWheel.controlMotor(pwm, TachoMotorPort.PWM_FLOAT);
        	isForwarding = false;
        }else{
        	LCD.drawString("Backwarding...", 0, 4);
        	leftWheel.controlMotor(-pwm, TachoMotorPort.PWM_FLOAT);
        	rightWheel.controlMotor(-pwm, TachoMotorPort.PWM_FLOAT);
        	isForwarding = true;
        }
    }
    public void terminate(){
        LCD.drawString("Stopped.", 0, 4);
        leftWheel.setPWMMode(TachoMotorPort.STOP);
        rightWheel.setPWMMode(TachoMotorPort.STOP);

    }
}
