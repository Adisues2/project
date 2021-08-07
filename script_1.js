// var arr =  [1, 2, 3, 4, 5];
//  
// for (var i = arr.length + 1; i >= 0; i++) {
//     console.log(arr[i]);
// }
// var n = 5;
// let string = "";
// for(let k =0; k<=n; k++){
    
//     for(let j = 0; j<k; j++){
//         string+= " * ";

//     }
//     string+= "\n";
// }
// console.log(string);

// const numbers = [5,0,9,1,7,4,2,6,3,8];

//  console.log(numbers.toString());
//  console.log(numbers.join(``))
//  console.log(numbers.sort().reverse());

//  for (var l= numbers.length - 1; l>=0; l--){
//      console.log(numbers[l]);
//  }

//         function calculus (a,b) {
//             console.log(a+b)
//         }

// calculus(4,5)

// function familyAge(myAge){
// let mum = myAge*2;
    
//     console.log(" my    mum  is " + mum + " my  dad  is "+ (mum)*1.2);
// }
//      familyAge(20);

// const myadd = " blue";
// function test(){
//     console.log(myadd);
//     if(6===6){
//         var label = "goog";

//     }
// }
// test();

function displayfamilyAge(myAge){
    const  mum = myAge*2
    return myAge*2    
}
let myage = displayfamilyAge(20);

console.log(myage)


function ration(decimal) {
    console.log(10+ decimal);
}
ration(10)

// const sumofTotal = (a,b) =>{
//     console.log(a+b)
// }
// sumofTotal(2,3);

// function excercise

// const infoAboutMe = (name ,hobbies) =>{
//     console.log("my name is  " + name   + "  and "+ "my hobbies is to read " + hobbies);
// }
// infoAboutMe("smith" ,  "book");

// function infoAboutPerson(personname,personAge, personFavoriteColor){
//      console.log("your name is " + personname + "  you are " + personAge + " years old " + "your favorite color is " + personFavoriteColor);
// }

//   infoAboutPerson("john" ,34, "blue");
//   infoAboutPerson("smith" ,20, "brown");

//   function infoAboutPerson(personname,personAge, personFavoriteColor,personHobbies){

//     console.log("your name is " + personname + "  you are " + personAge + " years old " + "your favorite color is  " + personFavoriteColor + "   " + personHobbies);

//   }
// infoAboutPerson("jones" ,40, "yellow" ," book");

// infoAboutPerson("David", 45, "blue", ["tennis", "painting"]);
// infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"]);


// keyless car

// let age = 18;
// //  var age = prompt("enter your age");
//  const  CheckDriverAge = (age) =>{

//     if(age ===18)
//     {
//       console.log("Sorry, you are too young to drive this car. Powering off");
//     }
//     else if(age>18){
//       console.log("You are old enough to drive, Powering On. Enjoy the ride!");
//     }
//     else
//     {
//       console.log("Congratulations on your first year of driving. Enjoy the ride!");
//     }
// CheckDriverAge();
// var arr = [1,2,-4,56];
// var max = arr;
// console.log(Math.max(1,2,-4,56));


 //words of star
// // const letter = mywords.splice(" ");
// var mywords = ["Hello","World", "in" , "a" , "frame"];
//   //console.log(mywords.join(" "));
//  for (i =0; i<mywords.length; i++){
//    mywords[i] = mywords[i].toUpperCase() + mywords[i].substr(1);
//  }
//  mywords.join(" ");
// function framework(mywords){
//   let border = " *".repeat(mywords.length+4)
//    return `${border}\n *
//     ${mywords}*
//     \n${border}`
// }

// console.log(framework(mywords));



// let words = prompt("enter a words ").split('.');
// words = words.map(word =>word.trim());

// function playTheGame() {
//   if (!confirm("Would you like to play a game")) {
//       alert("No problem, Goodbye.")
//   }
//   else {
//       let number = parseInt(prompt("Enter a number between 0-10", " "))
//       if (!number) {
//           alert("Sorry Not a number,Goodbye.")
//       }
//       else if ((number > 10) || (number < 0)) {
//           alert("Please enter a valid number")
//           while ((number > 10) || number < 0) {
//               number = prompt("Enter a number between 0-10",

 
//  function playTheGame(){
//  var game =  confirm('would like to play the game');
//   if(game = false){
//  alert('no problem ,goodbye');
//  return;
//   }
//   else{
//     var computerNumber = Math.floor(Math.random()*11);
//     console.log(computerNumber);
//     var random = parseInt(prompt("enter number 1~10"))
//     if(random>10 || random>0)
//     alert("sorry not a number,googbye");
//   }
//   if(!random){
//     alert("sorry its not good number ,goodbye");
//   }
// else{
//   for(var i =0; i<3; i++){
//     if(!usernum);
//       return;
      
    
//       test(usernum,computerNumber)
//       return;
    
//   }
  
// }
// alert("out of chance");
//  }
 
//  function text(usernum ,computerNumber){
//    if(usernum===computerNumber){
//      alert("WIINER" + "and stop  the game");
//      return true;
//    }
//    else{
//      var user = prompt("ask new number ");
//      if(rand >computerNumber){
//        return false;
//      }
//      if(random<computerNumber){
//        let newNumber = prompt("use new number");
//        alert("your number is smaller then the computer,s");
//        return false;
//      }
    
//    }
//  }

// even or odd
// function chekNumber() 
// {
//   for(i=0; i<=100; i++)
//   {
//     console.log(i)
//     if(i%2 ==0){
// console.log('numbef si even')
//     }
  
//   else(!i)
//   {
//     console.log('number is odd');
//   }
// }
// }
// chekNumber()

// divisible
//let num =500;
//function isDivisible(num){
//   for(i =0; i<=500; i++){
//     //console.log(i);
  
//   if(i%23 ==0){
//     console.log(i)
//   }
// }


// var array = [ ];
// for(i =0; i<num; i++){
//   if(i%23 ==0){
// array.push(i);
//   }
// }
// console.log(array)

// var sum = array.reduce(function(a,b){
//   return a+b;
// },0);
// console.log(sum);
// }
// isDivisible(500)
// let num =500;
// function isDivisble(num){

// var array = [ ];

// for(i =0; i<num; i++){
//   if(i%3 == 0){
// array.push(i);
//   }
// }
// console.log(array);

// var sum = array.reduce(function(a,b){
//   return a+b;
//  },0);
//  console.log(sum);
// }
// isDivisble(500);
// let num =500;
// function isDivisble(num){

// var array = [ ];

// for(i =0; i<num; i++){
//   if(i%45 == 0){
// array.push(i);
//   }
// }
// console.log(array);

// var sum = array.reduce(function(a,b){
//   return a+b;
//  },0);
//  console.log(sum);
// }
// isDivisble(500)

//shopping list

let shoppingList = ["banana","orange", "apple"];

let stock = {
  "banana": 6,
  "apple": 0,
  "pear": 12,
  "orange": 32,
  "blueberry": 6
}

let prices = {
  "banana": 4,
  "apple": 2,
  "pear": 1,
  "orange": 1.5,
  "blueberry": 10
}

function myBill()
{
  for( let prices in stock){
    console.log(`${shoppingList}: ${stock[prices]}`);
  }
}
myBill()