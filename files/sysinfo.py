rename_process("sysinfo")
be.based.run("uname -a")
term.write()
if "network" in be.devices.keys():
    vr("ipconf", be.devices["network"][0].get_ipconf())
    if be.devices["network"][0].connected:
        term.write(
            "Connected to STA: "
            + vr("ipconf")["ssid"]
            + " | IPv4 Address: "
            + str(vr("ipconf")["ip"])
        )
    if be.devices["network"][0].ap_connected:
        term.write(
            "AP Started: "
            + cptoml.fetch("SSID", "IWD-AP")
            + " | IPv4 AP Address: "
            + str(vr("ipconf")["ip_ap"])
        )
    term.nwrite(
        "TelNet: "
        + ("UP | Port: 23 | " if "ttyTELNET0" in pv[0]["consoles"] else "DOWN | ")
    )
    term.write("Active console: " + pv[0]["console_active"] + "\n")
    gc.collect()
    gc.collect()

vr("free", gc.mem_free())
if vr("free") > 1024:
    vr("free", str(vr("free") // 1024) + "k")
else:
    vr("free", str(vr("free")))
term.write(vr("free") + " bytes free.")

be.api.setvar("return", "0")
