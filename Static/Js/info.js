//Checking whether Full Name input is emapty
//The Nat ID Input
let natIdPress = document.getElementById('id_nat_id');
//The Full name Span
let fNSpan = document.getElementById('fNSpan');
//The Full name input
let fullNameInPT = document.getElementById('id_full_name');
//The Age Input
let theAge = document.getElementById('id_age');
//The natid span
let natIdSpan = document.getElementById('natIdSpan');
//The age span
let ageSpan = document.getElementById('ageSpan');
//The drop down gender
let dropGender = document.getElementById('id_gender');
//Gender Span
let gendSpan = document.getElementById('gendSpan');
//The County id picker
let county = document.getElementById('id_county');
//pick email id
let emailClick = document.getElementById('id_email');
//The phoen input border
let phoneBorder = document.getElementById('id_phone');
//Phone span change color
let phoneSColor = document.getElementById('phoneSpan');
//id_address span change color
let id_address = document.getElementById('id_address');
//County span change color
let cSpn = document.getElementById('cSpn');
//Id Postol code get
let id_postal_code = document.getElementById('id_postal_code');
//Span Box
let boxSpan = document.getElementById('boxSpan');
//Span Code post
let codeP = document.getElementById('psCodeSpan');





//The fuction to check which will run after the id input is clicked

//This is the event listener
natIdPress.addEventListener('click', checkFullName);
//The fuction follows

function checkFullName(){

    let fullNameValue = document.getElementById('id_full_name').value;

    if(fullNameValue != null && fullNameValue != ""){

        fNSpan.style.color = 'rgb(17, 197, 107)';
        fullNameInPT.style.borderColor = 'rgb(17, 197, 107)';

    }
    else{

        fNSpan.style.color = 'rgb(197, 17, 17)';
        fullNameInPT.style.borderColor = 'rgb(197, 17, 17)';

    }

}


//Checking whether National Id input is empty

theAge.addEventListener('click', checkNatId);

//The fuction follows

function checkNatId(){

    let natIdValue = document.getElementById('id_nat_id').value;

    if(natIdValue != null && natIdValue != ""){

        natIdSpan.style.color = 'rgb(17, 197, 107)';
        natIdPress.style.borderColor = 'rgb(17, 197, 107)';

    }
    else{

        natIdSpan.style.color = 'rgb(197, 17, 17)';
        natIdPress.style.borderColor = 'rgb(197, 17, 17)';

    }

}


//To check if anational id is valid



function howManyDigits(){

    let natIdLength = document.getElementById('id_nat_id').value;
    let natlengthLog = (''+natIdLength).length;

    if(natlengthLog <= 6){

        natIdSpan.style.color = 'rgb(197, 17, 17)';
        natIdPress.style.borderColor = 'rgb(197, 17, 17)';

    }

    else if(natlengthLog >= 9){

        natIdSpan.style.color = 'rgb(197, 17, 17)';
        natIdPress.style.borderColor = 'rgb(197, 17, 17)';

    }
    else{

        natIdSpan.style.color = 'rgb(17, 197, 107)';
        natIdPress.style.borderColor = 'rgb(17, 197, 107)';

    }
    
}


//Checking whether Age input is empty

dropGender.addEventListener('click',checkAge)

function checkAge(){

    let theAgeInp = document.getElementById('id_age').value;

    if(theAgeInp != null && theAgeInp != ""){

        theAge.style.borderColor = 'rgb(17, 197, 107)';
        ageSpan.style.color = 'rgb(17, 197, 107)';

    }
    else{

        theAge.style.borderColor = 'rgb(197, 17, 17)';
        ageSpan.style.color = 'rgb(197, 17, 17)';

    }

}


//Putting an age limit

let age = document.getElementById('id_age').onkeyup = function() {ageLimit();activeSumit()};

function ageLimit(){

    let ageLim = document.getElementById('id_age').value;

    if(ageLim >= 60){

        theAge.style.borderColor = 'rgb(197, 17, 17)';
        ageSpan.style.color = 'rgb(197, 17, 17)';

    }
    else if(ageLim <= 17){

        theAge.style.borderColor = 'rgb(197, 17, 17)';
        ageSpan.style.color = 'rgb(197, 17, 17)';

    }

    else {

        theAge.style.borderColor = 'rgb(17, 197, 107)';
        ageSpan.style.color = 'rgb(17, 197, 107)';

    }

}


//Approve gender

phoneBorder.addEventListener('click',trueSex);

function trueSex(){

    dropGender.style.borderColor = 'rgb(17, 197, 107)';
    gendSpan.style.color = 'rgb(17, 197, 107)';

}

//Approve County

id_address.addEventListener('click',trueCounty);

function trueCounty(){

    county.style.borderColor = 'rgb(17, 197, 107)';
    cSpn.style.color = 'rgb(17, 197, 107)';
    id_postal_code.style.borderColor = 'rgb(197, 17, 17)';

}


//To check if po box is empty
id_postal_code.addEventListener('click',checkPOBox)

function checkPOBox(){

    let valAddress = document.getElementById('id_address').value;

    if(valAddress != null && valAddress != ""){

        id_address.style.borderColor = 'rgb(17, 197, 107)';
        boxSpan.style.color = 'rgb(17, 197, 107)';

    }
    else{

        id_address.style.borderColor = 'rgb(197, 17, 17)';
        boxSpan.style.color = 'rgb(197, 17, 17)';

    }

}


//Postol Code check

let postCodChec = document.getElementById('id_postal_code').onkeydown = function() {postPresent()};


function postPresent(){

    let postValGet = document.getElementById('id_postal_code').value;
    let postValGetLegth = (''+postValGet).length;

    if(postValGetLegth == 4){

        id_postal_code.style.borderColor = 'rgb(17, 197, 107)';
        codeP.style.color = 'rgb(17, 197, 107)';


    }
    else{

        id_postal_code.style.borderColor = 'rgb(197, 17, 17)';
        codeP.style.color = 'rgb(197, 17, 17)';
    }


}


//Submit button action

let subFull = document.getElementById('id_full_name').onkeyup = function() {activeSumit()};
//let subAge = document.getElementById('id_age').onkeyup = function() {activeSumit()};
let subNatId = document.getElementById('id_nat_id').onkeyup = function() {activeSumit();howManyDigits()};
let subFullid_phone = document.getElementById('id_phone').onkeyup = function() {activeSumit()};
let subFullid_email = document.getElementById('id_email').onkeyup = function() {activeSumit()};
let subFullid_address = document.getElementById('id_address').onkeyup = function() {activeSumit()};
let subFullid_postal_code = document.getElementById('id_postal_code').onkeyup = function() {activeSumit()};


function activeSumit(){

    let subFullName = document.getElementById('id_full_name').value;
    let itAge = document.getElementById('id_age').value;
    let itNatId = document.getElementById('id_nat_id').value;
    let itPhone = document.getElementById('id_phone').value;
    let itemail = document.getElementById('id_email').value;
    let itAdress = document.getElementById('id_address').value;
    let itcode = document.getElementById('id_postal_code').value;

    let postValGet = document.getElementById('id_postal_code').value;
    let postValGetLegth = (''+postValGet).length;

    //Email
    var theemail = document.getElementById('id_email').value;
    var partten = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    //Phpne
    let phoneval = document.getElementById('id_phone').value;     
    let phonePtn = /^[+]*[(]{0,1}[0-9]{1,3}[)]{0,1}[-\s\./0-9]*$/g;


    if(subFullName != "" && itAge != "" && itNatId != "" && itPhone != "" && itemail != "" && itAdress != "" && itcode != "" && postValGetLegth == 5 && theemail.match(partten) && phoneval.match(phonePtn)){

        let submitBtnMan = document.getElementById('subBtnIt');

        submitBtnMan.removeAttribute('disabled');

        submitBtnMan.classList.add('active');

        submitBtnMan.classList.remove('inactive');

    }

    else{

        let submitBtnMan = document.getElementById('subBtnIt');

        submitBtnMan.setAttribute('disabled','disabled');

        submitBtnMan.classList.remove('active');

        submitBtnMan.classList.add('inactive');

    }


}