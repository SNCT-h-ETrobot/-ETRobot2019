package movement;

import java.lang.Math;

import lejos.hardware.port.BasicMotorPort;
//import lejos.hardware.motor.Motor;
import lejos.hardware.port.MotorPort;
import lejos.hardware.port.TachoMotorPort;

import java.lang.Exception;

public class DefCycle {
	protected TachoMotorPort MotorL;
	protected TachoMotorPort MotorR;
	
	public enum port{ A, B, C, D };
	
	public DefCycle(port l, port r) {
		try {
			if(l == r) throw new IllegalArgumentException("Same port was set to both motor.");
			switch(l) {
				case A: MotorL = MotorPort.A.open(TachoMotorPort.class); break;
				case B: MotorL = MotorPort.B.open(TachoMotorPort.class); break;
				case C: MotorL = MotorPort.C.open(TachoMotorPort.class); break;
				case D: MotorL = MotorPort.D.open(TachoMotorPort.class); break;
				default: throw new IllegalArgumentException("Unknown port was set to left motor.");
			}
			switch(r) {
				case A: MotorR = MotorPort.A.open(TachoMotorPort.class); break;
				case B: MotorR = MotorPort.B.open(TachoMotorPort.class); break;
				case C: MotorR = MotorPort.C.open(TachoMotorPort.class); break;
				case D: MotorR = MotorPort.D.open(TachoMotorPort.class); break;
				default: throw new IllegalArgumentException("Unknown port was set to right motor.");
			}
		} catch(Exception e) {
			System.out.println("Exception detected.");
			System.out.println(e);
		}
	}
	
	public void move(int l, int r) { //simple
		try {
			if(Math.abs(l) > 100 || Math.abs(r) > 100)
				throw new IllegalArgumentException("Argument value is out of range.");
			
			if( l < 0 ) {
				MotorL.controlMotor(-l, BasicMotorPort.FORWARD);
			} else {
				MotorL.controlMotor(l, BasicMotorPort.BACKWARD);
			}

			if( r < 0 ) {
				MotorR.controlMotor(-r, BasicMotorPort.FORWARD);
			} else {
				MotorR.controlMotor(r, BasicMotorPort.BACKWARD);
			}
			
		} catch(Exception e) {
			System.out.println("Exception detected.");
			System.out.println(e);
		}
	}
}
