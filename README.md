<div align="center">

  <img src="https://brands.home-assistant.io/_/vektiva_smarwi/logo.png" alt="Vektiva Smarwi Logo" width="300">

  # Vektiva Smarwi – Home Assistant Integration

  [![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)
  [![version](https://img.shields.io/github/v/release/GeroComp/homeassistant-vektiva-smarwi?style=for-the-badge)](https://github.com/GeroComp/homeassistant-vektiva-smarwi/releases)
  [![License](https://img.shields.io/github/license/GeroComp/homeassistant-vektiva-smarwi?style=for-the-badge)](LICENSE)

</div>

---

This custom integration allows you to control the [**Vektiva Smarwi smart window opener**](https://vektiva.com/index.php) directly from [Home Assistant](https://www.home-assistant.io/).

It provides full local control over your windows via your Wi-Fi network, ensuring fast response times and privacy without relying on external clouds.

---

## ✨ Features
* **Full Control:** Open, Close, and Stop the window opener.
* **Live Feedback:** Displays current state (open, closed, opening, closing).
* **Multi-device Support:** Control as many Smarwi devices as you need.
* **Local API:** Works strictly over your local network.

---

## 📦 Installation

### Option 1: Via HACS (Recommended)
The easiest way to install and keep the integration updated.

1.  Open **HACS** in Home Assistant.
2.  Click the **3 dots menu** (top right corner) → Select **Custom repositories**.
3.  Paste the following URL into the Repository field:
    ```text
    https://github.com/GeroComp/homeassistant-vektiva-smarwi.git
    ```
4.  Select category: **Integration**.
5.  Click **Add**, then find "Vektiva Smarwi" in the list and click **Download**.
6.  **Restart Home Assistant**.

### Option 2: Manual Installation
1.  Download the latest release from this repository.
2.  Copy the folder `custom_components/vektiva_smarwi` into your Home Assistant config folder:
    `config/custom_components/vektiva_smarwi`
3.  **Restart Home Assistant**.

---

## ⚙️ Configuration

To add the device, edit your `configuration.yaml` file.

> **⚠️ Important Tip:** It is highly recommended to set a **Static IP address** for your Smarwi device in your router settings. If the IP address changes (via DHCP), Home Assistant will lose connection to the device.

Add the following lines to `configuration.yaml`:

```yaml
cover:
  - platform: vektiva_smarwi
    host: 192.168.1.50    # Replace with your Smarwi's IP address
    name: Kitchen Window  # Name shown in Home Assistant
```
Example for Multiple Devices
If you own multiple Smarwi units, simply list them like this:


```yaml
cover:
  - platform: vektiva_smarwi
    host: 192.168.1.50
    name: Kitchen

  - platform: vektiva_smarwi
    host: 192.168.1.51
    name: Bedroom
```
> **Note:** After editing the configuration.yaml file, you must restart Home Assistant for the changes to take effect.

## 🛠️ Troubleshooting

### Device is unavailable?
- **Check Connection:** Ensure the Smarwi is connected to Wi-Fi and has power.
- **Verify IP:** Confirm the IP address in `configuration.yaml` matches the device's actual IP.
- **Test Access:** Open the device’s IP address in a web browser. If the Smarwi web interface loads, the device is working correctly.

### Window does not respond to commands?
- **Restart Home Assistant:** After editing `configuration.yaml`, always restart Home Assistant.
- **Static IP:** Make sure your router assigns a static IP to the Smarwi device.
- **Network Issues:** Check if your local network firewall or router settings block communication.

### Multiple devices not showing?
- **YAML Formatting:** Ensure each device entry starts with a `-` under `cover:`.
- **Indentation:** Use two spaces for indentation, not tabs.

---

## ❤️ Credits & Acknowledgements

This project exists thanks to the hard work of the original creators and the manufacturer.

- **Original Creator:** Huge thanks to *cvrky* for the initial development of this Home Assistant integration. His work laid the foundation for this project.  
- **Manufacturer:** Special thanks to *Vektiva* for designing the Smarwi hardware and providing an open API that makes integrations like this possible.  
- **Maintenance:** Currently updated and maintained by *GeroComp*.  

> **Community:** Made possible by the Home Assistant community — your ideas and contributions keep this project alive.

## 📜 License

MIT License – see the [LICENSE](LICENSE) file for details.
