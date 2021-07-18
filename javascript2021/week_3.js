console.log("hello world");
console.log("welcom to javascript");
let str = "Hello Everyone, please say hello to the class";
let posUppercaseHello = str.indexOf("Hello"); // case sensitive
let posLowercaseHello = str.indexOf("hello");
console.log(posUppercaseHello) // 0
console.log(posLowercaseHello) // 27

let secondstr = "hello Everyone, please say hello to the class";
let secondStrPosHello = secondstr.indexOf("hello"); 
console.log(secondStrPosHello) // 0
let adisu = "wow";
let adisus = "hey";
console.log(adisu);


let text = "welcome \weldone\  weljob";
console.log(text);
let Text = "Hello Everyone please say hello";
console.log(Text.substring(0,2));

let addressNumber = 45;
let addressStreet = "allenby";
let country = "israel";
let global_address = "i live " + addressStreet + addressNumber + country;

console.log(global_address);


 let birth = 1992;
 let year = 2021;
 let myBirthYear = "i will be in "  + (year - birth) + " in " + "2021";
 console.log( myBirthYear);
 let array = ["papaya" , "banana" ," orange"];
 console.log(array);
 console.log(array[0]);
 array[2] = "lemon";
 console.log(array);
  let sampleArray = [
    [1, 2, 5],
    [7, 6, 10, 11, 12],
    [3]
];

console.log(sampleArray);
console.log(sampleArray[1][4]);


let num=+5;
console.log(num);
console.log(typeof(sampleArray));
console.log(sampleArray.length);
console.log(sampleArray.push("5"));
console.log(sampleArray);
console.log(sampleArray.pop([1][2]));
console.log(sampleArray);
console.log(sampleArray.splice([1]));

let pets = ["cat", "dog" ,"fish" ,"rabbit" , "cow"];
 console.log(pets[1]);
 let pet = "horse";
 console.log(pets.push(pet));
 console.log(pets);

//  excercise 1

let fruits = ["banana","apples" , "oranges","blueberries"];
console.log(fruits.splice([1]));
console.log(fruits);
