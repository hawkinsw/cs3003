const VehicleC = {
	model: "Nothing",
	start: function () {
		console.log("Starting a " + this.model + ".\n");
	},
}
const TeslaC = {
	__proto__: VehicleC
}
const RivianC = {
	__proto__: VehicleC,
	start: function () {
		console.log("Not starting a " + this.model + ".\n");
	},
}

vc = Object.create(VehicleC);
rc = Object.create(RivianC);

vc.start()
rc.start()
