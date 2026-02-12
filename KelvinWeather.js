//constant kelvin
const kelvin = 293;

//constant celsius
const celsius = kelvin - 273;

// fahrenheit, can be changed
let fahrenheit = (celsius * (9/5) + 32);

// rounds down 
fahrenheit = Math.floor(fahrenheit);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit`);
