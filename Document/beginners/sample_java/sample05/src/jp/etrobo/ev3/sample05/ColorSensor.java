/*
 *  ColorSensor.java (for leJOS EV3)
 *  Created on: 2016/06/11
 *  Copyright (c) 2016 Embedded Technology Software Design Robot Contest
 */
package jp.etrobo.ev3.sample05;

import lejos.hardware.port.Port;
import lejos.hardware.sensor.EV3ColorSensor;
import lejos.hardware.sensor.SensorMode;

public class ColorSensor {
    private EV3ColorSensor colorSensor;
    private SensorMode redMode;           // 輝度検出モード
    private float[] sampleLight;

	public ColorSensor(Port port){
        colorSensor = new EV3ColorSensor(port);
        redMode = colorSensor.getRedMode();     // 輝度検出モード
        sampleLight = new float[redMode.sampleSize()];
    }

    /*
     * カラーセンサーから輝度値を取得する。
     * @return 輝度値。
     */
    public float getBrightness() {
        redMode.fetchSample(sampleLight, 0);
        return sampleLight[0];
    }
}
