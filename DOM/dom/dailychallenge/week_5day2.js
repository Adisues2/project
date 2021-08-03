// daily challenge

 var libButton = document.getElementById('lib-button');


var story = function(){

var  result =document.getElementById('story');
var noun = document.getElementById('noun');
var  Adje = document.getElementById("adjective");
var  verb = document.getElementById('verb');
var  person =document.getElementById('person');
var place = document.getElementById('place');
 
 
  //result.innerHTML =  " my name" + noun.value + " "+ Adje.value+ verb.value+person.value+place.value+ ".";
  result.innerHTML = `My   ${noun.value} is  ${Adje.value} and  ${verb.value} also   ${person.value} in ${place.value}.`;
}

libButton.addEventListener('click',story);
 