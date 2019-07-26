package primal;

import lejos.hardware.Bluetooth;
import lejos.remote.nxt.NXTCommConnector;
import lejos.remote.nxt.NXTConnection;

public class BT_Ctrl {
	//Bluetooth bt;
	NXTCommConnector nxtcomm;
	NXTConnection nxtconn;
	
	private final int WAIT_MS = 0;
	private final int DATA_LENGTH = 16;
	private final int FAIL_COUNT = 20;
	private final byte PACKET_HEADER = 'F';
	
	public BT_Ctrl() {
		//bt = new Bluetooth();
		nxtcomm = Bluetooth.getNXTCommConnector();
		nxtconn = nxtcomm.waitForConnection(WAIT_MS, NXTConnection.RAW); //maybe "wait" has no significance
	}
	
	public boolean getData(byte[] array) {
		byte data[] = new byte[DATA_LENGTH];
		
		do { //data get
			nxtconn.read(data, data.length);
		} while(data[0] == 0);
		
		if(data[0] == PACKET_HEADER && data[15] == SUM(data)) { //check sum & header
			return true;
		} else {
			return false;
		}
	}
	
	private byte SUM(byte[] data) {
		byte temp = 0;
		for(int i=0; i<data.length-1; ++i) temp += data[i];
		return temp;
	}
}

/*
data assign
byte 0    : header
byte 2~14 : load
byte 15   : check sum

*/