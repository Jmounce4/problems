let raceNumber = Math.floor(Math.random() * 1000);
let registeredEarly = false;
let runnerAge = 20;

if (registeredEarly && runnerAge >= 18){
  raceNumber += 1000;

}

if (registeredEarly && runnerAge >= 18){
  console.log(`${raceNumber} will race at 9:30am`);

} else if (!registeredEarly && runnerAge >= 18){
  console.log(`${raceNumber} will race at 11:00am`);

} else {
console.log(`${raceNumber} will race at 12:30am`);
}
