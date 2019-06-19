# Bedsite_Raspberrypi_unit
This git include 2 python program <br/>
-MQTT_Handle.py	<br/>
This program will waiting message from MQTT Broker <br/>
-SIP_Handle.py	<br/>
This program will control Twinkle SIP Phone program <br/>
# Setup environment
Speaker/Microphone<br/>
/etc/asound.conf <br/>

pcm.!default { <br/>
  type asym <br/>
  capture.pcm "mic" <br/>
  playback.pcm "speaker" <br/>
} <br/>
pcm.mic { <br/>
  type plug <br/>
  slave { <br/>
    pcm "hw:<card number>,<device number>" <br/>
  } <br/>
} <br/>
pcm.speaker { <br/>
  type plug <br/>
  slave { <br/>
    pcm "hw:<card number>,<device number>" <br/>
  } <br/>
} <br/>



