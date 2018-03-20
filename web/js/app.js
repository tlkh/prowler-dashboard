$(document).ready(function () {
    var devicetable = $('#dataTable').DataTable({
    });

    // main displays
    var devices_total_display = document.getElementById("devices-total-display");
    var devices_ssh_display = document.getElementById("devices-ssh-display");
    var devices_vnc_display = document.getElementById("devices-vnc-display");
    var devices_weak_display = document.getElementById("devices-weak-display");

    var ssh_count = 0;
    var vnc_count = 0;
    var others_count = 0;
    var total_count = 0;
    var weak_count = 0;

    function update_counts() {
        devices_ssh_display.innerHTML = ssh_count;
        devices_vnc_display.innerHTML = vnc_count;
        devices_weak_display.innerHTML = weak_count;
        devices_total_display.innerHTML = total_count;
    }

    update_counts();

    // table
    eel.expose(populate_table);
    function populate_table(hostname, type, ports, status) {
        console.log("Populating table...")
        devicetable.row.add([
            total_count,
            hostname,
            type,
            ports,
            status
        ]).draw(false);
        console.log("splitting ports");
        var ports_split = (ports.toString()).split(",")
        Object.keys(ports_split).forEach(function (key, index) {
            console.log(ports_split[index]);
            if (ports_split[index] == "22/ssh") {
                ssh_count = ssh_count + 1;
            } else if (ports_split[index] == "5900/vnc") {
                vnc_count = vnc_count + 1;
            } else {
                others_count = others_count + 1;
            }
        });
	if (status == "true"){
		weak_count = weak_count + 1;
	}
        total_count = total_count + 1;
        update_counts();
    }
});