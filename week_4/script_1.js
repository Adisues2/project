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

  function infoAboutPerson(personname,personAge, personFavoriteColor,personHobbies){

    console.log("your name is " + personname + "  you are " + personAge + " years old " + "your favorite color is  " + personFavoriteColor + "   " + personHobbies);

  }
infoAboutPerson("jones" ,40, "yellow" ," book");

infoAboutPerson("David", 45, "blue", ["tennis", "painting"]);
infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"]);