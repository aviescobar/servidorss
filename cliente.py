import socket
import pyautogui
from PIL import Image
import io
import time

# Configuramos el cliente
server_ip = "172.168.2.25"  # Cambia a la IP del servidor
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
