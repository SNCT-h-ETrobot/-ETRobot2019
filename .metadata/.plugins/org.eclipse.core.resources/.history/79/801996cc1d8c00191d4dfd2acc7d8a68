package sensor;

import lejos.hardware.port.Port;
import lejos.hardware.sensor.SensorConstants;
import lejos.hardware.sensor.SensorMode;
import lejos.hardware.sensor.EV3TouchSensor;
import lejos.utility.Delay;

public class Touch {
	protected EV3TouchSensor touchSensor;
	protected SensorMode mode;
	
	public Touch(Port port) {
		touchSensor = new EV3TouchSensor(port);               //make instance
		mode = touchSensor.getMode(SensorConstants.MODE_RAW); //set sensor mode
	}
	
	//integrated to constructor
	/*public void init() {
		mode = touch.getMode(SensorConstants.MODE_RAW);
	}*/
	
	public boolean isPress() {
		//dynamic allocation of array, which has only 1 element
		float value[] = new float[touchSensor.sampleSize()];
		
		mode.fetchSample(value, 0); //get data and store into value[0]
		if(value[0] == 1.0) {
			return true;
		} else {
			return false;
		}
	}
	
	public boolean isPress_s() { //prevention chattering
		Delay.msDelay(10);
		return isPress();
	}
}
