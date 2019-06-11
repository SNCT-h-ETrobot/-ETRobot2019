package primal;

import lejos.hardware.port.SensorPort;
import sensor.Color;
import sensor.Touch;

import lejos.hardware.lcd.LCD;
import lejos.utility.Delay;

public class Primal {
	public static Touch button1;
	public static Color color;

	//////////////////////////////////////////////////
	//main
	public static void main(String[] args) {
		//////////
		//setup
		LCD.drawString("initializing...", 1, 3);
		float[] RGB = new float[3];
		button1 = new Touch(SensorPort.S1);
		color = new Color(SensorPort.S3);

		//////////
		//stand by
		LCD.clear();
		while(button1.isPress() == false) {
			LCD.drawString("stand by", 1, 3);
			LCD.drawString("push to start", 1, 4);
			Delay.msDelay(20);
		}

		//////////
		//main loop
		while(true) {
			Delay.msDelay(10);
			color.getRGB(RGB); //get RGB data
			
			LCD.drawString("R:" + RGB[0], 1, 1); //print RGB data to LCD
			LCD.drawString("G:" + RGB[1], 1, 2);
			LCD.drawString("B:" + RGB[2], 1, 3);
			
			switch( color.getColorID() ) { //TODO: test EV3ColorSensor::getColorID()
				case 0:  LCD.drawString("Color:Red   ", 1, 5); break;
				case 1:	 LCD.drawString("Color:Green ", 1, 5); break;
				case 2:	 LCD.drawString("Color:Blue  ", 1, 5); break;
				case 3:  LCD.drawString("Color:Yellow", 1, 5); break;
				case 6:  LCD.drawString("Color:White ", 1, 5); break;
				case 7:  LCD.drawString("Color:Black ", 1, 5); break;
				default: LCD.drawString("Color:Unkown", 1, 5); break;
			}
		}
	}
}
