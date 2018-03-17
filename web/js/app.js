eel.expose(get_devices_status); // Expose this function to Python
function get_devices_status(devices_ssh, devices_vnc, devices_weak, devices_total) {
    console.log("returning device counts")
    devices_ssh_display.innerHTML = devices_ssh;
    devices_vnc_display.innerHTML = devices_vnc;
    devices_weak_display.innerHTML = devices_weak;
    devices_total_display.innerHTML = devices_total;
    
}

// main displays
var devices_total_display = document.getElementById("devices-total-display");
var devices_ssh_display = document.getElementById("devices-ssh-display");
var devices_vnc_display = document.getElementById("devices-vnc-display");
var devices_weak_display = document.getElementById("devices-weak-display");

get_devices_status();
//eel.say_hello_py("Javascript World!"); // Call a Python function
