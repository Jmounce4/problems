let userName = '';

userName ? console.log(`Hello, ${userName}!`) : 
console.log('hello');

let userQuestion = 'Will today be a good day?';
console.log(userQuestion);

let randomNumber = Math.floor(Math.random() * 8);

let eightBall = '';

switch(randomNumber){
  case 0:
    eightBall = 'It is certain';
    break;
  case 1:
    eightBall = 'Yes';
    break;
  case 2:
    eightBall = 'Of course';
    break;
  case 3:
    eightBall = 'It is decidedly so';
    break;
  case 4:
    eightBall = 'Signs point to yes';
    break;
  case 5:
    eightBall = 'Always';
    break;
  case 6:
    eightBall = 'You know its yes';
    break;
  case 7:
    eightBall = 'Obviously';
    break;
  default:
    eightBall = 'YES!';
    break;
}

console.log(eightBall);
