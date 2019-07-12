package primal;

import lejos.hardware.port.SensorPort;
import sensor.Color;
import sensor.Touch;
import movement.DefCycle;

import lejos.hardware.lcd.LCD;
import lejos.utility.Delay;

public class Primal {
	public static Touch button1;
	public static Touch button2;
	public static Color color;
	public static DefCycle tire;

	//////////////////////////////////////////////////
	//main
	public static void main(String[] args) {
		//////////
		//setup
		LCD.drawString("initializing...", 1, 3);
		float[] RGB = new float[3];
		
		button1 = new Touch(SensorPort.S1);
		button2 = new Touch(SensorPort.S4);
		color = new Color(SensorPort.S2);
		
		int value[] = new int[2];
		tire = new DefCycle(DefCycle.port.D, DefCycle.port.A);

		//////////
		//stand by
		LCD.clear();
		while( button1.isPress() ) {
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
			
			switch( color.getColorID() ) {
				case 0:  LCD.drawString("Color:Red   ", 1, 5); break;
				case 1:	 LCD.drawString("Color:Green ", 1, 5); break;
				case 2:	 LCD.drawString("Color:Blue  ", 1, 5); break;
				case 3:  LCD.drawString("Color:Yellow", 1, 5); break;
				case 6:  LCD.drawString("Color:White ", 1, 5); break;
				case 7:  LCD.drawString("Color:Black ", 1, 5); break;
				default: LCD.drawString("Color:Unkown", 1, 5); break;
			}
			
			if( button1.isPress_s() ) {
				value[0] = 25;
			} else {
				value[0] = 0;
			}

			if( button2.isPress_s() ) {
				value[1] = 25;
			} else {
				value[1] = 0;
			}
			
			tire.move(value[1], value[0]);
		}
	}
}
