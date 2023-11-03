class Vehicle {
	constructor() {
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

v.__proto__.user_manual = function () {
	console.log(`This is a helper function for a ${this.model}.`);
};

v.user_manual();
t.user_manual();

v.__proto__.model = "Empty?"

v.user_manual();
t.user_manual();

const pr = {
	pr: "I am here.",
	getGreeting: () => {
		console.log(`${JSON.stringify(this)} is wild.`)
		return this.hello;
	}
}

function f() {
	this.hello = "goodbye";
}

f.prototype = pr;
let ff = new f();
let gg = new f();
/*
f.prototype.getGreeting = function() {
	return this.hello;
}
f.prototype.message = "This is a message."
*/

console.log(f.prototype == ff.__proto__)
console.log(`ff.getGreeting(): ${ff.getGreeting()}`);
console.log(`gg.getGreeting(): ${gg.getGreeting()}`);

ff.__proto__.getGreeting = function () {
	return this.message
}

console.log(`ff.getGreeting(): ${ff.getGreeting()}`);
console.log(`gg.getGreeting(): ${gg.getGreeting()}`);

console.log(f.prototype == ff.__proto__)
console.log(f.prototype == gg.__proto__)
