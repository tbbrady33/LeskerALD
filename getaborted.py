import asyncio
import signal
from pymodbus.client import AsyncModbusTcpClient
import sys

# Connection parameters
IP = '192.168.137.11'
PORT = 502
REGISTER_ADDRESS = 218  # The address for the Aborted signal, based on IOID from XML
SCALE_FACTOR = 1  # Scaling factor, if needed


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

async def read_aborted_flag():
    # Create the asynchronous client
    client = AsyncModbusTcpClient(IP, port=PORT)
    
    # Try to establish the connection asynchronously
    connected = await client.connect()
    
    if not connected:
        print("Failed to connect to the Modbus server.")
        return
    
    try:
        while True:
            # Read the "Aborted" flag (one register)
            response = await client.read_input_registers(REGISTER_ADDRESS, count=1)
            
            if response.isError():
                print("Modbus error:", response)
            else:
                aborted_value = response.registers[0]  # Value from the register
                print(f"Aborted Flag: {aborted_value}")
            
            await asyncio.sleep(1)  # Wait 1 second before the next read
    
    finally:
        # Ensure the client is properly closed
        await client.close()

# Run the asyncio loop to execute the script
asyncio.run(read_aborted_flag())
