def verificar_vlan(vlan):
    if 1 <= vlan <= 1005:
        print(f"La VLAN {vlan} está en el rango normal.")
    elif 1006 <= vlan <= 4094:
        print(f"La VLAN {vlan} está en el rango extendido.")
    else:
        print(f"La VLAN {vlan} no está en un rango válido.")

if __name__ == "__main__":
    vlan = int(input("Introduce el número de VLAN: "))
    verificar_vlan(vlan)