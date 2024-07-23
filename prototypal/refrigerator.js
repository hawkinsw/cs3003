const refrigerator = {
  chill: function (item) {
    console.log(`Chilling a(n) ${item} at ${this.default_temperature} degrees.`);
  },
};

refrigerator.default_temperature = 33;
refrigerator.chill("onions");

commercial_refrigerator = Object.create(refrigerator);
commercial_refrigerator.default_temperature = 32;

refrigerator.chill = function(item) {
  console.log("WHAT?");
}
commercial_refrigerator.chill("salad");
