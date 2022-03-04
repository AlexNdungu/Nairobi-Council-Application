//The corse action
let theCourse = document.getElementById('id_course');
//The institute
let theUbiv = document.getElementById('id_institution');
//The level 
let theLevel = document.getElementById('id_level');
//uNI START DATE
let uniStart = document.getElementById('id_uni_start_date');
//uni end date
let uniEnd = document.getElementById('id_uni_finish_date');
//Highschool name 
let highName = document.getElementById('id_institution_high');
//Kcse file input
let kcseFile = document.getElementById('id_kcse_file');
//Secondary start date
let secStartDate = document.getElementById('id_sec_start_date');
//Kcse File name
let kcseNameFile = document.getElementById('kcseFileName');
//Kcse sec Finish date
let kcseFinsh = document.getElementById('id_sec_finish_date');
//Primary name
let priNameput = document.getElementById('id_institution_pri');
//The kcpe file input
let kcpeInputFile = document.getElementById('id_kcpe_file');
//Primary start 
let kcpeDateStart = document.getElementById('id_start_date');
//Kcpe file name
let kcpeFileName = document.getElementById('kcpeFileName');
//Kcpe end date
let kcpeEndDate = document.getElementById('id_finish_date');
//Another start kcpe
let kcpeDateStartValue = document.getElementById('id_start_date');


//Check Instiution value
theCourse.addEventListener('click',cheUniv);

function cheUniv(){

    let uniValue = document.getElementById('id_institution').value;

    if(uniValue != null && uniValue != ''){

        theUbiv.style.borderColor = 'rgb(17, 197, 107)';

    }
    else{

       
        theUbiv.style.borderColor = 'rgb(197, 17, 17)';


    }

}

//Check Course value

theLevel.addEventListener('click',checkCourse);

function checkCourse(){

    let courseValue = document.getElementById('id_course').value;

    if(courseValue != null && courseValue != ''){

        theCourse.style.borderColor = 'rgb(17, 197, 107)';

    }
    else{

       
        theCourse.style.borderColor = 'rgb(197, 17, 17)';


    }

}

//Level check

uniStart.addEventListener('click',checkLevel);

function checkLevel(){

    theLevel.style.borderColor = 'rgb(17, 197, 107)';

}


//Check uni start date

uniEnd.addEventListener('click',cheStarDate);

function cheStarDate(){

    let startDateUni = document.getElementById('id_uni_start_date').value;

    if(startDateUni != null && startDateUni != ''){

        uniStart.style.borderColor = 'rgb(17, 197, 107)';


    }
    else{

       
        uniStart.style.borderColor = 'rgb(197, 17, 17)';


    }

}

//To check date end secondary

highName.addEventListener('click',checkUniEnd);

function checkUniEnd(){

    let endUniDate = document.getElementById('id_uni_finish_date').value;

    if(endUniDate != null && endUniDate != ''){

        uniEnd.style.borderColor = 'rgb(17, 197, 107)';


    }
    else{

       
        uniEnd.style.borderColor = 'rgb(197, 17, 17)';


    }


}


//End date check
kcseFile.addEventListener('click',checkSecName);

function checkSecName(){

    let highSchool = document.getElementById('id_institution_high').value;

    if(highSchool != null && highSchool != ''){

        highName.style.borderColor = 'rgb(17, 197, 107)';


    }
    else{

       
        highName.style.borderColor = 'rgb(197, 17, 17)';


    }

}

//KCSE null

secStartDate.addEventListener('click',checkKcseFile);

function checkKcseFile(){

    let kcseFileValue = document.getElementById('id_kcse_file').value;

    if(kcseFileValue != null && kcseFileValue != ''){

        kcseNameFile.style.color = 'rgb(17, 197, 107)';


    }
    else{

       
        kcseNameFile.style.color = 'rgb(197, 17, 17)';


    }

}

//Check sec start

kcseFinsh.addEventListener('click',checkFinSecondary);

function checkFinSecondary(){

    let secStartValue = document.getElementById('id_sec_start_date').value;

    if(secStartValue != null && secStartValue != ''){

        secStartDate.style.borderColor = 'rgb(17, 197, 107)';


    }
    else{

       
        secStartDate.style.borderColor = 'rgb(197, 17, 17)';


    }

}

//Checking end secondary value

priNameput.addEventListener('click',checkSecEndValue);

function checkSecEndValue(){

    let borderEndSec = document.getElementById('id_sec_finish_date').value;

    if(borderEndSec != null && borderEndSec != ''){

        kcseFinsh.style.borderColor = 'rgb(17, 197, 107)';


    }
    else{

       
        kcseFinsh.style.borderColor = 'rgb(197, 17, 17)';


    }

}

//Checking Indtutute primaty

kcpeInputFile.addEventListener('click',chePriname);

function chePriname(){

    let priInName = document.getElementById('id_institution_pri').value;

    if(priInName != null && priInName != ''){

        priNameput.style.borderColor = 'rgb(17, 197, 107)';

    }
    else{

        priNameput.style.borderColor = 'rgb(197, 17, 17)';

    }

}

//Check Kcpe File Value

kcpeDateStart.addEventListener('click',kcpeFileValue);

function kcpeFileValue(){

    let kcpeFileValue = document.getElementById('id_kcpe_file').value;

    if(kcpeFileValue != null && kcpeFileValue != ''){

        kcpeFileName.style.color = 'rgb(17, 197, 107)';


    }
    else{

       
        kcpeFileName.style.color = 'rgb(197, 17, 17)';


    }

}

//Start kcpe date
kcpeEndDate.addEventListener('click',checkStartPri);

function checkStartPri(){

    let kpeStart = document.getElementById('id_start_date').value;

    if(kpeStart != null && kpeStart != ''){

        kcpeDateStart.style.borderColor = 'rgb(17, 197, 107)';

    }
    else{

        kcpeDateStart.style.borderColor = 'rgb(197, 17, 17)';

    }

}

//Start kcpe end date
kcpeDateStartValue.addEventListener('click',checkStartPri);

function checkStartPri(){

    let kpeStartEnd = document.getElementById('id_finish_date').value;

    if(kpeStartEnd != null && kpeStartEnd != ''){

        kcpeEndDate.style.borderColor = 'rgb(17, 197, 107)';

    }
    else{

        kcpeEndDate.style.borderColor = 'rgb(197, 17, 17)';

    }

}


//The submit logic

let uplBtn = document.getElementById('subBtnIt');

document.addEventListener('input', function(e) {
    if (!e.target.matches('#id_institution, #id_course, #id_uni_start_date, #id_uni_finish_date,#id_institution_high,#id_kcse_file,#id_sec_start_date,#id_sec_finish_date,#id_institution_pri,#id_kcpe_file,#id_start_date,#id_finish_date')) return;
    //your code here


    let uniName = document.getElementById('id_institution').value;
    let uniCorse = document.getElementById('id_course').value;
    let uniFro = document.getElementById('id_uni_start_date').value;
    let uniTo = document.getElementById('id_uni_finish_date').value;
    let highSchoolName = document.getElementById('id_institution_high').value;
    let kcseFileUpload = document.getElementById('id_kcse_file').value;
    let sceStart = document.getElementById('id_sec_start_date').value;
    let secEndStop = document.getElementById('id_sec_finish_date').value;
    let PriSchoolName = document.getElementById('id_institution_pri').value;
    let kcpeFileUpload = document.getElementById('id_kcpe_file').value;
    let priStart = document.getElementById('id_start_date').value;
    let priEndStop = document.getElementById('id_finish_date').value;

    
    
   if(uniName != null && uniName != '' && uniCorse != null && uniCorse != '' && uniFro != null && uniFro != '' && uniTo != null && uniTo != '' && highSchoolName != null && highSchoolName != '' && kcseFileUpload != null && kcseFileUpload != '' && sceStart != null && sceStart != '' && priEndStop != null && priEndStop != '' && priStart != null && priStart != '' && kcpeFileUpload != null && kcpeFileUpload != '' && PriSchoolName != null && PriSchoolName != '' && secEndStop != null && secEndStop != ''){
       
        uplBtn.classList.remove('inactive');
        uplBtn.classList.add('active');
        uplBtn.disabled = false;

        console.log('test');

   }


    else{

        uplBtn.classList.remove('active')
        uplBtn.classList.add('inactive');

        uplBtn.disabled = true;

    }

});


