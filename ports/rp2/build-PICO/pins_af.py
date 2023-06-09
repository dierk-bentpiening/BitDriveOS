PINS_AF = (
  ('GP0', (1, 'SPI0_RX'), (2, 'UART0_TX'), (3, 'I2C0_SDA'), (4, 'PWM0_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_OVCUR_DET'), ),
  ('GP1', (1, 'SPI0_CS'), (2, 'UART0_RX'), (3, 'I2C0_SCL'), (4, 'PWM0_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_DET'), ),
  ('GP2', (1, 'SPI0_SCK'), (2, 'UART0_CTS'), (3, 'I2C1_SDA'), (4, 'PWM1_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_EN'), ),
  ('GP3', (1, 'SPI0_TX'), (2, 'UART0_RTS'), (3, 'I2C1_SCL'), (4, 'PWM1_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_OVCUR_DET'), ),
  ('GP4', (1, 'SPI0_RX'), (2, 'UART1_TX'), (3, 'I2C0_SDA'), (4, 'PWM2_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_DET'), ),
  ('GP5', (1, 'SPI0_CS'), (2, 'UART1_RX'), (3, 'I2C0_SCL'), (4, 'PWM2_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_EN'), ),
  ('GP6', (1, 'SPI0_SCK'), (2, 'UART1_CTS'), (3, 'I2C1_SDA'), (4, 'PWM3_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_OVCUR_DET'), ),
  ('GP7', (1, 'SPI0_TX'), (2, 'UART1_RTS'), (3, 'I2C1_SCL'), (4, 'PWM3_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_DET'), ),
  ('GP8', (1, 'SPI1_RX'), (2, 'UART1_TX'), (3, 'I2C0_SDA'), (4, 'PWM4_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_EN'), ),
  ('GP9', (1, 'SPI1_CS'), (2, 'UART1_RX'), (3, 'I2C0_SCL'), (4, 'PWM4_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_OVCUR_DET'), ),
  ('GP10', (1, 'SPI1_SCK'), (2, 'UART1_CTS'), (3, 'I2C1_SDA'), (4, 'PWM5_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_DET'), ),
  ('GP11', (1, 'SPI1_TX'), (2, 'UART1_RTS'), (3, 'I2C1_SCL'), (4, 'PWM5_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_EN'), ),
  ('GP12', (1, 'SPI1_RX'), (2, 'UART0_TX'), (3, 'I2C0_SDA'), (4, 'PWM6_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_OVCUR_DET'), ),
  ('GP13', (1, 'SPI1_CS'), (2, 'UART0_RX'), (3, 'I2C0_SCL'), (4, 'PWM6_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_DET'), ),
  ('GP14', (1, 'SPI1_SCK'), (2, 'UART0_CTS'), (3, 'I2C1_SDA'), (4, 'PWM7_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_EN'), ),
  ('GP15', (1, 'SPI1_TX'), (2, 'UART0_RTS'), (3, 'I2C1_SCL'), (4, 'PWM7_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_OVCUR_DET'), ),
  ('GP16', (1, 'SPI0_RX'), (2, 'UART0_TX'), (3, 'I2C0_SDA'), (4, 'PWM0_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_DET'), ),
  ('GP17', (1, 'SPI0_CS'), (2, 'UART0_RX'), (3, 'I2C0_SCL'), (4, 'PWM0_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_EN'), ),
  ('GP18', (1, 'SPI0_SCK'), (2, 'UART0_CTS'), (3, 'I2C1_SDA'), (4, 'PWM1_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_OVCUR_DET'), ),
  ('GP19', (1, 'SPI0_TX'), (2, 'UART0_RTS'), (3, 'I2C1_SCL'), (4, 'PWM1_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_DET'), ),
  ('GP20', (1, 'SPI0_RX'), (2, 'UART1_TX'), (3, 'I2C0_SDA'), (4, 'PWM2_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (8, 'GPCK_GPIN0'), (9, 'USB_VBUS_EN'), ),
  ('GP21', (1, 'SPI0_CS'), (2, 'UART1_RX'), (3, 'I2C0_SCL'), (4, 'PWM2_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (8, 'GPCK_GPOUT0'), (9, 'USB_OVCUR_DET'), ),
  ('GP22', (1, 'SPI0_SCK'), (2, 'UART1_CTS'), (3, 'I2C1_SDA'), (4, 'PWM3_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (8, 'GPCK_GPIN1'), (9, 'USB_VBUS_DET'), ),
  ('GP25', (1, 'SPI1_CS'), (2, 'UART1_RX'), (3, 'I2C0_SCL'), (4, 'PWM4_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (8, 'GPCK_GPOUT3'), (9, 'USB_VBUS_DET'), ),
  ('GP26', (1, 'SPI1_SCK'), (2, 'UART1_CTS'), (3, 'I2C1_SDA'), (4, 'PWM5_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_EN'), ),
  ('GP27', (1, 'SPI1_TX'), (2, 'UART1_RTS'), (3, 'I2C1_SCL'), (4, 'PWM5_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_OVCUR_DET'), ),
  ('GP28', (1, 'SPI1_RX'), (2, 'UART0_TX'), (3, 'I2C0_SDA'), (4, 'PWM6_A'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (9, 'USB_VBUS_DET'), ),
  ('LED', (1, 'SPI1_CS'), (2, 'UART1_RX'), (3, 'I2C0_SCL'), (4, 'PWM4_B'), (5, 'SIO'), (6, 'PIO0'), (7, 'PIO1'), (8, 'GPCK_GPOUT3'), (9, 'USB_VBUS_DET'), ),
)
