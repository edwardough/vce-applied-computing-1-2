console.log("Welcome to the solverera. Version 0.0.1");
body = document.querySelector('body');

function removeSpaces( targetData ) {
    targetData = targetData.map( (item) => {
        if( item != ' ' ){ return item }
        // return item != " " ? item : console.log("Skipped space");
    });
    /* MAP is a higher order array method that replaces the code below.
    let newResult = [];
    for( i = 0; i < targetData.length; i++ ){
        if( targetData[i] == ' ' ){
            console.log('Found space. Skipping.')
        }
        else {
            newResult.push(targetData[i]);
        }
    }
    targetData = newResult;
    */
}

function addEquationToPage( equation ){
    let newElement = document.createElement('div');
    newElement.innerHTML = `<p style="color: blue">${equation.join(' ')}</p>`;
    body.appendChild(newElement);
}

let arrTypedInput = []; // our final equation container
let arrTerm = []; // our current term container

window.addEventListener('keydown', (e) => {
    // console.log(e);
    if( e.key != 'Shift' ){
        if( e.key == ' ' ) {
            // handle what we want to happen when spacebar is pressed.
            strTerm = arrTerm.join('');
            arrTypedInput.push(strTerm); // add this term to 'typedInput'
            arrTerm.splice(0) // clear arrTerm
        }
        else if( e.key == 'q' ){
            strTerm = arrTerm.join(''); // create a string version of the array arrTerm
            arrTerm.splice(0) // clear arrTerm for the next equation
            arrTypedInput.push(strTerm); // add to typedInput
            removeSpaces( arrTypedInput ); // remove any spaces from typedInput
            addEquationToPage( arrTypedInput ); // display equation on the actual page
            arrTypedInput.splice(0) // clear typedInput for next equation
            // console.log("Final result: " + typedInput.toString());
        }
        else { // for anything that isn't a space bar or q
            arrTerm.push(e.key);
            // console.log("arrTerm contains " + arrTerm.toString());
        }
    }
});

