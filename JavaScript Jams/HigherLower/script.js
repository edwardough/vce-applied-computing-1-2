function myFunction() {
    var answer =  42;
    var gameRunning = true;
    let playerGuess = document.getElementById("guess").value;
    let resultText;
    // Here is the 'logic' of the game using if/else statements
    if( answer == playerGuess ) {  
        resultText = "How did you know I was lying?? Well done!";
        let winPic = document.createElement('img');
        winPic.src = 'stock-chart.png';
        document.querySelector('body').appendChild(winPic);
        gameRunning = false;
    } else if( playerGuess < answer ) {
        resultText = "Too low, bozo!";
    } else if( playerGuess > 10 ) {
        resultText = "You know I am being tricky . . . but still wrong!";
    } else if( isNaN(playerGuess)) {
        resultText = "Did you even type a number in??";
    }
    document.getElementById('result').innerHTML = resultText;
}

