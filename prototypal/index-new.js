class Vehicle {
	constructor() {
		this.model = "Nothing";
	}
	start() {
		console.log("Start me up!\n");
	}
}

class Tesla extends Vehicle {
	constructor() {
		super();
		this.model = "Tesla";
	}
}

v = new Vehicle();
t = new Tesla();

v.start();

v.__proto__.help = function () {
	console.log("This is a helper function.");
};

v.help();
t.help();
