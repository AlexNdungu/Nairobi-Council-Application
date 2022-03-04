//Choosing the cv
function chooseCV()
{

    let idFileCv = document.getElementById('id_cv_file');
    idFileCv.click()
}
   
//Replace Name
let idFileCv = document.getElementById('id_cv_file');
let nameFileCv = document.getElementById("cvName");

idFileCv.addEventListener('change', function(event){
    let uploadFileName = event.target.files[0].name;
    nameFileCv.textContent = uploadFileName;

    const submit = document.getElementById('submitBtn');
    

    //Checking file extension
    const [extension, ...nameParts] = uploadFileName.split('.').reverse();
    console.log('extension:', extension);

    if(extension != 'pdf' && extension != 'PDF'){
        nameFileCv.style.color = 'rgb(197, 17, 17)';

        idFileCv.value = null;

        //disable button
    }
    else{
        nameFileCv.style.color = 'rgb(17, 197, 107)';
    
    }

})




//Choosing letter
function choseLetter()
{
    let idFileLetter = document.getElementById('id_aP_file');
    idFileLetter.click()
}
   
//Replace Name
let idFileLetter = document.getElementById('id_aP_file');
let nameFileLetter = document.getElementById("letterName");

idFileLetter.addEventListener('change', function(event){
    let uploadFileName = event.target.files[0].name;
    nameFileLetter.textContent = uploadFileName;

    const submit = document.getElementById('submitBtn');


    //Checking file extension
    const [extension, ...nameParts] = uploadFileName.split('.').reverse();
    console.log('extension:', extension);

    if(extension != 'pdf' && extension != 'PDF'){
        nameFileLetter.style.color = 'rgb(197, 17, 17)';

        //disable button

        idFileLetter.value = null;

    }
    else{
        nameFileLetter.style.color = 'rgb(17, 197, 107)';
       
    }


})


//Choose Good Conduct

function choseGc()
{
    let idFileGc = document.getElementById('id_gD_file');
    idFileGc.click()
}
   
//Replace Name
let idFileGc = document.getElementById('id_gD_file');
let nameFileGcr = document.getElementById("gcName");

idFileGc.addEventListener('change', function(event){
    let uploadFileName = event.target.files[0].name;
    nameFileGcr.textContent = uploadFileName;

    const submit = document.getElementById('submitBtn');


    //Checking file extension
    const [extension, ...nameParts] = uploadFileName.split('.').reverse();
    console.log('extension:', extension);

    if(extension != 'pdf' && extension != 'PDF'){
        nameFileGcr.style.color = 'rgb(197, 17, 17)';

        //disable button

        idFileGc.value = null;
    }
    else{
        nameFileGcr.style.color = 'rgb(17, 197, 107)';
       
    }


})


//Choose school letter

function choseScLetter()
{
    let idFileSl = document.getElementById('id_sL_file');
    idFileSl.click()
}
   
//Replace Name
let idFileSl = document.getElementById('id_sL_file');
let nameFileSl = document.getElementById("schoolL");

idFileSl.addEventListener('change', function(event){
    let uploadFileName = event.target.files[0].name;
    nameFileSl.textContent = uploadFileName;

    const submit = document.getElementById('submitBtn');


    //Checking file extension
    const [extension, ...nameParts] = uploadFileName.split('.').reverse();
    console.log('extension:', extension);

    if(extension != 'pdf' && extension != 'PDF'){
        nameFileSl.style.color = 'rgb(197, 17, 17)';

        //disable button

        idFileSl.value = null;

    }
    else{
        nameFileSl.style.color = 'rgb(17, 197, 107)';
        
    }



})


//Choose National Id Image

function natIdChoose()
{
    let idFileNatId = document.getElementById('id_natID_file');
    idFileNatId.click()
}
   
//Replace Name
let idFileNatId = document.getElementById('id_natID_file');
let nameFileNatId = document.getElementById("natIdImage");

idFileNatId.addEventListener('change', function(event){
    let uploadFileName = event.target.files[0].name;
    nameFileNatId.textContent = uploadFileName;

    const submit = document.getElementById('submitBtn');


    //Checking file extension
    const [extension, ...nameParts] = uploadFileName.split('.').reverse();
    console.log('extension:', extension);

    if(extension != 'jpg' && extension != 'jpeg' && extension != 'PNG' && extension != 'png'){
        nameFileNatId.style.color = 'rgb(197, 17, 17)';

        //disable button

        idFileNatId.value = null;

    }
    else{
        nameFileNatId.style.color = 'rgb(17, 197, 107)';
        
    }

})


//Choose passport image

function choosePp()
{
    let idFilePp = document.getElementById('id_pP_file');
    idFilePp.click()
}
   
//Replace Name
let idFilePp = document.getElementById('id_pP_file');
let nameFilePp = document.getElementById("ppName");

idFilePp.addEventListener('change', function(event){
    let uploadFileName = event.target.files[0].name;
    nameFilePp.textContent = uploadFileName;

    const submit = document.getElementById('submitBtn');


    //Checking file extension
    const [extension, ...nameParts] = uploadFileName.split('.').reverse();
    console.log('extension:', extension);

    if(extension != 'jpg' && extension != 'jpeg' && extension != 'PNG' && extension != 'png'){
        nameFilePp.style.color = 'rgb(197, 17, 17)';

        //disable button

        idFilePp.value = null;
    }
    else{
        nameFilePp.style.color = 'rgb(17, 197, 107)';
        
    }


})





//Choose Personal accidental cover


function chooeCover()
{
    let idFileCover = document.getElementById('id_personalAcc_file');
    idFileCover.click()
}
   
//Replace Name
let idFileCover = document.getElementById('id_personalAcc_file');
let nameFileCover = document.getElementById("accCoverName");

idFileCover.addEventListener('change', function(event){
    let uploadFileName = event.target.files[0].name;
    nameFileCover.textContent = uploadFileName;

    const submit = document.getElementById('submitBtn');


    //Checking file extension
    const [extension, ...nameParts] = uploadFileName.split('.').reverse();
    console.log('extension:', extension);

    if(extension != 'pdf' && extension != 'PDF'){
        nameFileCover.style.color = 'rgb(197, 17, 17)';

        //disable button

        idFileCover.value = null;

    }
    else{
        nameFileCover.style.color = 'rgb(17, 197, 107)';
       
    }


})


//dealing with the submit button

//let cvActive = document.getElementById('id_cv_file id_aP_file').oninput = function() {uploadFile()};

let uplBtn = document.getElementById('submitBtn');

document.addEventListener('change', function(e) {
    if (!e.target.matches('#id_cv_file, #id_aP_file, #id_gD_file, #id_sL_file,#id_natID_file,#id_pP_file,#id_personalAcc_file')) return;
    //your code here


    let cvInput = document.getElementById('id_cv_file').value;
    let upLetter = document.getElementById('id_aP_file').value;
    let goodCondUp = document.getElementById('id_gD_file').value;
    let schoolLetUp = document.getElementById('id_sL_file').value;
    let natIdUp = document.getElementById('id_natID_file').value;
    let passUpl = document.getElementById('id_pP_file').value;
    let pasnCoverUp = document.getElementById('id_personalAcc_file').value;

    
    
   if(cvInput != null && cvInput != '' && upLetter != null && upLetter != '' && goodCondUp != null && goodCondUp != '' && schoolLetUp != null && schoolLetUp != '' && natIdUp != null && natIdUp != '' && passUpl != null && passUpl != '' && pasnCoverUp != null && pasnCoverUp != ''){
       
        uplBtn.classList.remove('inactive');
        uplBtn.classList.add('active')
        uplBtn.disabled = false;

        console.log('test');

   }


    else{

        uplBtn.classList.remove('active')
        uplBtn.classList.add('inactive');

        uplBtn.disabled = true;

    }

});



