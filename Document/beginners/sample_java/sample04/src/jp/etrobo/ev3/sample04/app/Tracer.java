/*
 *  Tracer.java (for leJOS EV3)
 *  Created on: 2016/06/11
 *  Copyright (c) 2016 Embedded Technology Software Design Robot Contest
 */
package jp.etrobo.ev3.sample04.app;

import jp.etrobo.ev3.sample04.ColorSensor;
import lejos.hardware.lcd.LCD;
import lejos.hardware.port.MotorPort;
import lejos.hardware.port.SensorPort;
import lejos.hardware.port.TachoMotorPort;

public class Tracer {
    private TachoMotorPort leftWheel;
    private TachoMotorPort rightWheel;
    private ColorSensor    colorSensor;

	private static final int pwm = TachoMotorPort.MAX_POWER / 6;
	private static final float Kp = 83.0F;
	private static final float target = 0.1F;
	private static final float bias = 0.0F;

    public Tracer(){
    	leftWheel = MotorPort.C.open(TachoMotorPort.class);
    	rightWheel = MotorPort.B.open(TachoMotorPort.class);
    	colorSensor = new ColorSensor(SensorPort.S3);
    }

    public void init(){
    	LCD.drawString("Tracer", 0, 2);
    }
    public void run(){
    	LCD.drawString("running...", 0, 4);
    	float diff = colorSensor.getBrightness() - target;
    	float turn = Kp * diff + bias;
        leftWheel.controlMotor((int)(pwm - turn), TachoMotorPort.PWM_FLOAT);
        rightWheel.controlMotor((int)(pwm + turn), TachoMotorPort.PWM_FLOAT);
    }
    public void terminate(){
        LCD.drawString("Stopped.", 0, 4);
        leftWheel.setPWMMode(TachoMotorPort.STOP);
        rightWheel.setPWMMode(TachoMotorPort.STOP);

    }
}
