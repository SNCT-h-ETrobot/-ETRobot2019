package sensor;

import lejos.hardware.port.Port;
import lejos.hardware.sensor.EV3GyroSensor;

import lejos.robotics.SampleProvider;

public class Gyro extends EV3GyroSensor {
	
	public Gyro(Port port) {
		super(port);
	}
	
	public float getAngle() {
		float data[] = new float[2];
		
		SampleProvider gyro = super.getAngleMode();
		gyro.fetchSample(data, 0);
		return data[0];
	}

	public float getRate() {
		float data[] = new float[2];
		
		SampleProvider gyro = super.getRateMode();
		gyro.fetchSample(data, 0);
		return data[0];
	}

	public void getAngleRate(float[] data) {
		SampleProvider gyro = super.getAngleAndRateMode();
		gyro.fetchSample(data, 0); //get data and store into data[0-1]
	}
	
}
