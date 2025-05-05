import asyncio
import signal
from pymodbus.client import AsyncModbusTcpClient

# Connection parameters
IP = '192.168.137.11'
PORT = 502
REGISTER_ADDRESS = 1
SCALE_FACTOR = 0.000152590218967


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

async def read_pressure():
    # Create the asynchronous client
    client = AsyncModbusTcpClient(IP, port=PORT)
    
    # Try to establish the connection asynchronously
    connected = await client.connect()
    
    if not connected:
        print("Failed to connect to the Modbus server.")
        return
    
    try:
        while True:
            # Read input register (count=1 to read one register)
            # Correcting this call: `count` is passed as a keyword argument
            response = await client.read_input_registers(REGISTER_ADDRESS, count=1)
            
            if response.isError():
                print("Modbus error:", response)
            else:
                raw_value = response.registers[0]
                pressure = raw_value * SCALE_FACTOR
                print(f"Pressure: {pressure:.6f} Torr")
            
            await asyncio.sleep(1)  # Wait 1 second before the next read
    except KeyboardInterrupt:
        print("Exiting.")
    finally:
        # Ensure the client is properly closed
        await client.close()

# Run the asyncio loop to execute the script
asyncio.run(read_pressure())
