const getUserChoice = userInput => {
userInput = userInput.toLowerCase();
if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissors'|| userInput === 'bomb'){
  return userInput;
}else{
  console.log('Invalid user choice. Select rock, paper, or scissors!');
}

}

function getComputerChoice(){
  randomNum = Math.floor(Math.random()*3);

  if (randomNum === 0){
    return 'rock';
  }else if (randomNum === 1){
    return 'paper';
  }else{
    return 'scissors';
  } 

}


function determineWinner(userChoice, computerChoice){
  if(userChoice === computerChoice){
    return console.log('The game is a tie!')
  }

  if(userChoice === 'bomb'){
    return console.log('THE USER WINS WITH A BOMB');
  }
  
  if (userChoice === 'rock'){
    if(computerChoice ==='paper'){
      return console.log('The computer won!')
    }else{
      return console.log('You won!')
    }
  }

  if (userChoice === 'paper'){
    if(computerChoice ==='scissors'){
      return console.log('The computer won!')
    }else{
      return console.log('You won!')
    }
  }
  
  if (userChoice === 'scissors'){
    if(computerChoice ==='paper'){
      return console.log('The computer won!')
    }else{
      return console.log('You won!')
    }
  }

}

function playGame(){
  userChoice = getUserChoice('scissors');
  computerChoice = getComputerChoice();
  console.log(`User: ${userChoice}    Computer: ${computerChoice}`);
  determineWinner(userChoice, computerChoice);
}

playGame();
