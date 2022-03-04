//Take Kin Id 
let kinNatId = document.getElementById('id_kin_nat_id');
//Take Full Name input
let kinFullname = document.getElementById('id_kin_name');
//Take name span
let kinNameSpan = document.getElementById('kinName');
//Take phone number input
let kinPhoneIn = document.getElementById('id_kin_phone');
//Id span for kin
let kinId = document.getElementById('kinId');
//get kin email input
let kinEmail = document.getElementById('id_kin_email');
//Kin phone span
let kinSpanPhone = document.getElementById('kinPhone');


//Give Nat Id input action

kinNatId.addEventListener('click',checkFullName);

function checkFullName(){

    let id_kin_name = document.getElementById('id_kin_name').value;

    if(id_kin_name != null && id_kin_name != ""){

        kinNameSpan.style.color = 'rgb(17, 197, 107)';
        kinFullname.style.borderColor = 'rgb(17, 197, 107)';

    }
    else{

        kinNameSpan.style.color = 'rgb(197, 17, 17)';
        kinFullname.style.borderColor = 'rgb(197, 17, 17)';

    }

}


//Giving phone number action on click

kinPhoneIn.addEventListener('click',kinIdCheck);

function kinIdCheck(){

    let kinIdInput = document.getElementById('id_kin_nat_id').value;

    if(kinIdInput != null && kinIdInput != ""){

        kinId.style.color = 'rgb(17, 197, 107)';
        kinNatId.style.borderColor = 'rgb(17, 197, 107)';

    }
    else{

        kinId.style.color = 'rgb(197, 17, 17)';
        kinNatId.style.borderColor = 'rgb(197, 17, 17)';

    }


}

//Check How many id digits

function howManyDigits(){

    let natIdLength = document.getElementById('id_kin_nat_id').value;
    let natlengthLog = (''+natIdLength).length;

    if(natlengthLog <= 6){

        kinId.style.color = 'rgb(197, 17, 17)';
        kinNatId.style.borderColor = 'rgb(197, 17, 17)';

    }

    else if(natlengthLog >= 9){

        kinId.style.color = 'rgb(197, 17, 17)';
        kinNatId.style.borderColor = 'rgb(197, 17, 17)';

    }
    else{

        kinId.style.color = 'rgb(17, 197, 107)';
        kinNatId.style.borderColor = 'rgb(17, 197, 107)';

    }
    
}


//Checking if phone is filled

kinEmail.addEventListener('click',phoneKinCheck);

function phoneKinCheck(){

    let kinPhoneInput = document.getElementById('id_kin_phone').value;

    if(kinPhoneInput != null && kinPhoneInput != ""){

        kinSpanPhone.style.color = 'rgb(17, 197, 107)';
        kinPhoneIn.style.borderColor = 'rgb(17, 197, 107)';

    }
    else{

        kinSpanPhone.style.color = 'rgb(197, 17, 17)';
        kinPhoneIn.style.borderColor = 'rgb(197, 17, 17)';

    }

}

//Submit button logic

let subFullid_name = document.getElementById('id_kin_name').onkeyup = function() {activeSumit()};
let subFullid_id = document.getElementById('id_kin_nat_id').onkeyup = function() {activeSumit();howManyDigits()};
let subFullid_phone = document.getElementById('id_kin_phone').onkeyup = function() {activeSumit()};
let subFullid_mail = document.getElementById('id_kin_email').onkeyup = function() {activeSumit()};


function activeSumit(){

    let subFullName = document.getElementById('id_kin_name').value;
    let itAge = document.getElementById('id_kin_nat_id').value;
    let itNatId = document.getElementById('id_kin_phone').value;


    //Email
    var theemail = document.getElementById('id_kin_email').value;
    var partten = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    //Phpne
    let phoneval = document.getElementById('id_kin_phone').value;     
    let phonePtn = /^[+]*[(]{0,1}[0-9]{1,3}[)]{0,1}[-\s\./0-9]*$/g;


    if(subFullName != "" && itAge != "" && itNatId != "" && theemail.match(partten) && phoneval.match(phonePtn)){

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