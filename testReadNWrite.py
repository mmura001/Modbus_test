from pymodbus.client import ModbusTcpClient

# PLC Configuration
PLC_IP = "192.168.0.101"  # PLC's IP address
PLC_PORT = 502            # Modbus TCP port
REGISTER_ADDRESS = 0      # Starting address for register operations

def read_register(client, register_address):
    
    # Read register
    
    try:
        response = client.read_holding_registers(register_address, count=10)
        if response.isError():
                print(f"Error reading from PLC: {response}")
        else:
            print(f"Holding Registers: {response.registers}")
    except Exception as e:
        print(f"Exception during read: {e}")

def write_register(client, register_address, value):
    
   # Writes a value to a single register on the PLC.
    
    try:
        response = client.write_register(register_address, value)
        if response.isError():
            print(f"Error writing to PLC: {response}")
        else:
            print(f"Successfully wrote {value} to register {register_address}.")
    except Exception as e:
        print(f"Exception during write: {e}")

def main():
    """
    Handle user input for read  10 registers or write input - register address and value
    """
    # Initialize Modbus client
    client = ModbusTcpClient(PLC_IP, port=PLC_PORT)
    
    if not client.connect():
        print(f"Failed to connect to PLC at {PLC_IP}:{PLC_PORT}.")
        return

    print(f"Connected to PLC at {PLC_IP}:{PLC_PORT}.")

    while True:
        # input - read or write
        operation = input("Enter 'read' or 'write' or 'exit' to quit: ").strip().lower()

        if operation == "read":
            register_address = 0
            # register_address = int(input("Enter the register address to read: "))
            read_register(client, register_address)
        elif operation == "write":
            register_address = int(input("Enter the register address to write: "))
            value = int(input("Enter the value to write: "))
            write_register(client, register_address, value)
        elif operation == "exit":
            print("Exiting program.")
            break
        else:
            print("Invalid operation. Please enter 'read', 'write', or 'exit'.")

    # Close connection
    client.close()
    print("Connection to PLC closed.")

if __name__ == "__main__":
    main()
