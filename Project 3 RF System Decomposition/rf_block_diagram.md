# RF Block Diagram – ESP32

```mermaid
flowchart LR
    MCU[Information Source / MCU + Wi-Fi/Bluetooth Baseband]

    MOD[Modulation]
    DEMOD[Demodulation]

    TX[2.4 GHz RF Transmitter]
    RX[2.4 GHz RF Receiver]

    PA[Power Amplifier (PA)]
    LNA[Low Noise Amplifier (LNA)]

    SW[Balun + TX/RX Switch + RF Filtering / Matching]
    ANT[Antenna Interface]

    PWR[Power Supply / Bias / Regulators]
    CLK[Clock Generator]

    MCU --> MOD --> TX --> PA --> SW --> ANT
    ANT --> SW --> LNA --> RX --> DEMOD --> MCU

    PWR --> TX
    PWR --> RX
    PWR --> PA
    PWR --> LNA
    PWR --> SW

    CLK --> TX
    CLK --> RX
