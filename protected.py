import subprocess
import webbrowser

def get_connected_devices():
    """
    Muestra la lista de dispositivos conectados a la red WiFi.
    Usa el comando 'arp -a' para obtener las direcciones IP y MAC de los dispositivos conectados.
    """
    try:
        print("Buscando dispositivos conectados...")
        devices = subprocess.run("arp -a", shell=True, capture_output=True, text=True)
        if devices.returncode == 0:
            print("Dispositivos Conectados:\n", devices.stdout)
        else:
            print("Error obteniendo dispositivos:", devices.stderr)
    except Exception as e:
        print("Error ejecutando el comando ARP:", e)   
        

def open_router_panel():
    """
    Abre el panel de administración del router en el navegador web predeterminado.
    Esto permite al usuario gestionar la configuración de su red, como cambiar la contraseña WiFi o bloquear dispositivos.
    """
    print("Abriendo el panel de administración del router...")
    webbrowser.open("http://192.168.1.1")

def block_devices(mac_address):
    """
    Indica al usuario cómo bloquear un dispositivo específico en la red.
    Dado que en Windows no se pueden bloquear dispositivos por MAC directamente desde la terminal,
    se sugiere hacerlo desde el panel del router.
    """
    print(f"Para bloquear el dispositivo con dirección MAC {mac_address}, ingrese al panel del router y realice el bloqueo manualmente.")
    open_router_panel()

def secure_wifi():
    """
    Realiza tareas básicas de seguridad en la red WiFi:
    1. Muestra los dispositivos conectados.
    2. Da la opción de cambiar la contraseña WiFi accediendo al panel del router.
    3. Da la opción de bloquear dispositivos sospechosos.
    """
    print("Asegurando tu conexión WiFi...\n") 
     
    # Paso 1: Mostrar los dispositivos conectados
    get_connected_devices()      
    
    # Paso 2: Cambiar la contraseña WiFi si el usuario lo desea
    change_password = input("\n¿Quieres cambiar la contraseña del WiFi? (si/no): ").strip().lower()
    if change_password == "si":
        print("Accediendo al panel de administración del router...")
        open_router_panel()
    
    # Paso 3: Bloquear dispositivos sospechosos si el usuario lo solicita
    block_option = input("\n¿Quieres bloquear dispositivos sospechosos? (si/no): ").strip().lower()
    if block_option == "si":
        mac_address = input("Inserta la dirección MAC del dispositivo para bloquear: ").strip()
        block_devices(mac_address)

    print("\nMedidas de seguridad aplicadas. Asegúrate de que la configuración de tu router esté actualizada.")  

# Ejecuta la función principal para iniciar el proceso de seguridad WiFi
secure_wifi()
