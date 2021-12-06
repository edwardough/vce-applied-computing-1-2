// Declare the array 'myTeam' with enhanced readability
var myTeam = [
  "Franklin", // Notes on 'Franklin' -> The next GOAT
  "Jack",
  "McVeigh",
  "Lockett", // Notes on 'Lockett' -> GOAT
  "Cappa",
  "Grundy",
  "Barry",
  "Hall",
  "Roberts-Thompson",
  "Bird" ];

var nextGreatestSwan = prompt("Who is the next greatest swanny? ");
myTeam.push(nextGreatestSwan);

for( let i = 1; i < myTeam.length; i++ ){
    var temp = document.createElement("li");
    temp.innerHTML = myTeam[i];
    document.getElementById('list').appendChild(temp); 
}
