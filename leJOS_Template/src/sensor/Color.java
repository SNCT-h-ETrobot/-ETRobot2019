package sensor;

import lejos.hardware.port.Port;
import lejos.hardware.sensor.SensorMode;
import lejos.hardware.sensor.EV3ColorSensor;

public class Color extends EV3ColorSensor {
	protected SensorMode mode;
	
	public Color(Port port) {
		super(port);
	}
	
	public void getRGB(float[] data) {
		SensorMode color = super.getMode(super.COL_COLOR);
		color.fetchSample(data, 0); //get data and store into data[0-2]
	}
	
	public int getID() { //TODO: EV3ColorSensor::getColorID() returns Color ID?
		float[] value = new float[1];
		
		SensorMode  color = super.getMode(super.COL_REFLECT);
		color.fetchSample(value, 0); //get data and store into value[0]
		return (int)value[0];
	}
}