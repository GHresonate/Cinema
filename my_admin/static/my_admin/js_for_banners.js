const allPhotos = 5;
const inputs = document.getElementsByClassName("field");
const bigForm =document.getElementById("big_form");
const remMain = document.getElementById('rem_main');
const remBanner = document.getElementById('rem_banner');
const reader = new FileReader();
const bannerReader = new FileReader();
const resButt = document.getElementById('main_res')
const smallBatt = document.getElementsByClassName('small_hidden_form');
const smallRem = document.getElementsByClassName('rem_small')
const bigHiddenForm = document.getElementById("main-ph")
const boxes = document.getElementsByClassName('boxes');
const buttAddForm = document.getElementById('big_gal_button_top');
const buttRemForm = document.getElementById('big_gal_button_bottom');
const photo_parent = document.getElementById('photo_parent');
const subButt = document.getElementById('my_submit');
const messageTextOneWord = document.createElement('p');
messageTextOneWord.innerText ="Это поле должно содержать одно слово на английском";
const messageUrl= document.createElement('p');
messageUrl.innerText ="Введите корректный url.";
let fileUploader = document.getElementById('id_main_photo');
let bannerUploader = document.getElementById('id_banner_photo')
let imageGrid = document.getElementById('image_grid');
let bannerImageGrid = document.getElementById('image_banner');
let lastForm = -1;
let form_state = [];
let forms = [];
let order = [];

if (imageGrid.childNodes.length>1){
        imageGrid.removeChild(imageGrid.firstChild);
        imageGrid.removeChild(imageGrid.childNodes[1])
    };

if (bannerImageGrid) {
    if (bannerImageGrid.childNodes.length > 1) {
        bannerImageGrid.removeChild(bannerImageGrid.firstChild);
        bannerImageGrid.removeChild(bannerImageGrid.childNodes[1])
    }
    ;
}
function validate(){
    let is_good = 1;
        let forms_for_check = document.getElementsByClassName('small_hidden_form')
    let photos_form = document.getElementsByClassName('small_ph')
        for (let photo=0; photo< photos_form.length; photo++){
        if (photos_form[photo].innerHTML.length == 0){
                    is_good = 0;
                    photos_form[photo].parentNode.classList.add("error");
        } else {
            photos_form[photo].parentNode.classList.remove("error");
        }
    }
    for (let x=0; x<forms_for_check.length; x++){
        let error = 0;
        if (forms_for_check[x].children[1].value==''){
            is_good = 0;
            error = 1;
        }
        if (forms_for_check[x].children[2].value==''){
            is_good = 0;
            error = 1;
        }
        if (!error){
            forms_for_check[x].classList.remove("error");
        } else {
            forms_for_check[x].classList.add("error");
        }
    }

    let firstForm = getFirstClear();
    if (firstForm==0){
        buttAddForm.parentNode.classList.add("error");
        is_good=0;
    } else{
        buttAddForm.parentNode.classList.remove("error");
        for (let y=0; y<firstForm;y++){
          if (boxes[y].childNodes[1].childNodes.length==0){
              boxes[y].classList.add("error");
              is_good = 0;
          } else {
              boxes[y].classList.remove("error");
          };
        };
    }
    for (let x=0; x<inputs.length; x++){
      if (inputs[x].children[1].value==''){
          inputs[x].classList.add("error");
          is_good = 0;
      } else {
          inputs[x].classList.remove("error");
      }
    };
    if (!imageGrid.children[0]){
        fileUploader.parentElement.parentElement.parentElement.classList.add("error");
        is_good = 0;
    }
    else {
        fileUploader.parentElement.parentElement.parentElement.classList.remove("error");
    };
    if (bannerImageGrid){
    if (!bannerImageGrid.children[0]){
        bannerUploader.parentElement.parentElement.parentElement.classList.add("error");
        is_good = 0;
    }
    else {
        bannerUploader.parentElement.parentElement.parentElement.classList.remove("error");
    };
    }
    if (is_good==1){
        for (let x=0; x<allPhotos; x++){
            let first = getFirstClear();
            if (first!=-2){
                photo_parent.appendChild(forms[first]);
                boxes[first].parentNode.style.display = "none"
                lastForm++;
                form_state[first]=1;
            };
        }
        bigForm.submit();
    }

};
function getFirstClear(){
  let first;
  for (let x=0; x<allPhotos; x++){
      if (form_state[x]==1){
        first = -2;
      };
      if (form_state[x]==0){
          return x;
      };
  };
  return first;
};

function getPlace(position){
    if (position==-3){
        position=allPhotos-1;
    };
    const parent = smallBatt[position].parentNode.parentNode;
    return parent.firstElementChild;
};

function getRealPosition(position){
    for (let x=0; x<allPhotos; x++){
        if (order[x]==position){
            return x;
        };
    };
};

function changeOrder(position){
    let form = forms[position];
    let form_number = order[position];
    for (let x =position; x<(allPhotos-1);x++){
        order[x] = order[x+1];
        form_state[x] = form_state[x+1];
        forms[x] = forms[x+1];
    };
    forms[allPhotos-1] = form;
    order[allPhotos-1] = form_number;
    form_state[allPhotos-1] = 0;
};

subButt.addEventListener('click', validate);

fileUploader.addEventListener('change', (event) => {
  const files = event.target.files;
  let file = files[0];
  reader.readAsDataURL(file);
  reader.addEventListener('load', (event) => {
    let img = document.createElement('img');
    img.height=144;
    img.width = 194;
    if (imageGrid.firstChild){
        imageGrid.removeChild(imageGrid.firstChild);
    };
    imageGrid.appendChild(img);
    img.src = event.target.result;
    img.alt = file.name;
  });

});
if (bannerUploader) {
    bannerUploader.addEventListener('change', (event) => {
        const files = event.target.files;
        let file = files[0];
        bannerReader.readAsDataURL(file);
        bannerReader.addEventListener('load', (event) => {
            let img = document.createElement('img');
            img.height = 144;
            img.width = 194;
            if (bannerImageGrid.firstChild) {
                bannerImageGrid.removeChild(bannerImageGrid.firstChild);
            }
            ;
            bannerImageGrid.appendChild(img);
            img.src = event.target.result;
            img.alt = file.name;
        });

    });
}
if (remMain){
remMain.addEventListener('click', (event)=>{
    if (imageGrid.firstChild) {
      imageGrid.removeChild(imageGrid.firstChild);
    };
    fileUploader.value = '';
});}

if (remBanner){
    remBanner.addEventListener('click', (event)=>{
        if (bannerImageGrid.firstChild) {
            bannerImageGrid.removeChild(bannerImageGrid.firstChild);
        };
        bannerUploader.value = '';
});
}

for (let x=0; x<allPhotos; x++) {
    smallBatt[x].children[1].addEventListener('change', (event) => {
        let realPos = getRealPosition(x);
        const files = event.target.files;
        let file = files[0];
        smallBatt[realPos].reader.readAsDataURL(file);
        smallBatt[realPos].reader.addEventListener('load',(event)=>{
            let place = getPlace(realPos);
            let img = document.createElement('img');
            img.height = 124;
            img.width = 174;
            if (place.firstChild){
                place.removeChild(place.firstChild);
            };
            place.appendChild(img);
            img.src = event.target.result;
            img.alt = file.name;
            smallBatt[realPos].reader = new FileReader();
        });
    },);

    smallRem[x].addEventListener('click', (event)=>{
        let realPlace = getRealPosition(x);
        smallBatt[realPlace].firstChild.value = '';
        let place = getPlace(realPlace);
        if (place.firstChild){
          place.removeChild(place.firstChild);
        }
        else {
            if (lastForm==(allPhotos-1)){
                buttAddForm.style.opacity="1";
            }
            else {
                buttAddForm.style.opacity="1";
                if (lastForm==0){
                    buttRemForm.style.opacity="0.5";
                }

            }
            photo_parent.removeChild(forms[realPlace]);
            changeOrder(realPlace);
            lastForm--;
        };
    });
};

buttRemForm.addEventListener('click', (event) =>{
    let first = getFirstClear();
    let place = getPlace(first-1);

    if (place.firstChild){
          place.removeChild(place.firstChild);
        };

    switch (first){
        case 1:{
            smallBatt[first-1].firstChild.value = '';
            buttRemForm.style.opacity = "0.5";
            photo_parent.removeChild(forms[first-1]);
            form_state[first-1] = 0;
            lastForm--;
        break;
    };
        case (-2): {
            smallBatt[allPhotos-1].firstChild.value = '';
            buttAddForm.style.opacity = "1";
            photo_parent.removeChild(forms[allPhotos - 1]);
            form_state[allPhotos - 1] = 0;
            lastForm--;
            break;
        };
        case (-1): {
            break;
        };
        default:{
            smallBatt[first-1].firstChild.value = '';
            photo_parent.removeChild(forms[first-1]);
            form_state[first-1] = 0;
            lastForm--;
        };
    };
});

buttAddForm.addEventListener('click', (event) =>{
    let first = getFirstClear();
        buttRemForm.style.opacity = "1";
    if (first!=-2){
        photo_parent.appendChild(forms[first]);
        smallRem[first].style.top = "-410px"
        lastForm++;
        form_state[first]=1;
        if (first==(allPhotos-1)){
            buttAddForm.style.opacity = "0.5";
        };
    };

});

resButt.addEventListener('click', (event)=>{
    if (fileUploader){
        if (imageGrid.firstChild){
            imageGrid.removeChild(imageGrid.firstChild);
        }
        fileUploader.value = '';
      };
    if (bannerUploader){
        bannerUploader.value=''
        if (bannerImageGrid.firstChild){
            bannerImageGrid.removeChild(bannerImageGrid.firstChild);
        };
    }
    let first = getFirstClear();
    if (first==-2){
        first=allPhotos;
    }
    for (let x=0; x<first; x++){
        let place = getPlace(0);
        if (place.firstChild){
            place.removeChild(place.firstChild);
        };
        smallBatt[0].firstChild.value = '';
        form_state[x] = 0;
        $(boxes[0]).remove();
    };

    let errors=document.getElementsByClassName("error");
    let length = errors.length;
    for (let x=0;x<length;x++){
        errors[0].classList.remove("error");
    };

    let urlErrors=document.getElementsByClassName("url_error");
    let urlLength = urlErrors.length;
    for (let x=0;x<urlLength;x++){
        urlErrors[0].classList.remove("url_error");
    };

    if (inputs[3].children.length==3){
        inputs[3].removeChild(messageUrl);
    };

    if (inputs[5].children.length==3){
        inputs[5].removeChild(messageTextOneWord);
    };

    lastForm = -1;
    buttAddForm.style.opacity="1";
    buttRemForm.style.opacity="0.5";
});

let preload_img = 0;

for (let x=0; x<allPhotos; x++){
    order[x] = x;
    smallBatt[x].reader = new FileReader();
};

let deletedCheckboxes = []

buttRemForm.style.opacity="0.5";
for (let x=0; x<allPhotos; x++){
    forms[x] = boxes[preload_img];
    if (smallBatt[preload_img].children.length<=10){
        boxes[preload_img].children[1].children[1].childNodes[0].remove();
        for (let x=0; x<4;x++){
            boxes[preload_img].children[1].children[1].children[x].remove()
        };
        boxes[preload_img].children[1].children[1].children[3].style.display = "none"
        boxes[preload_img].children[1].children[1].children[0].classList.add("small_photo_form")
        $(boxes[preload_img]).remove();
        form_state[x]=0;

    } else {
        buttRemForm.style.opacity="1";
        form_state[x]=1;
        let href = smallBatt[preload_img].children[1].href;
        let img = document.createElement('img');
        img.height = 124;
        img.width = 174;
        boxes[preload_img].children[0].appendChild(img);
        img.src =href;
        for (let x=0; x<6; x++){
            boxes[preload_img].children[1].children[1].childNodes[0].remove();
        }
        boxes[preload_img].children[1].children[1].children[1].remove()
        boxes[preload_img].children[1].children[1].children[2].remove()
        boxes[preload_img].children[1].children[1].children[3].remove()
        boxes[preload_img].children[1].children[1].children[0].classList.add("small_photo_form")

        if (preload_img == allPhotos-1){
            buttAddForm.style.opacity="0.5";
        }

        deletedCheckboxes[preload_img] = boxes[preload_img].children[1].children[1].children[3]
       boxes[preload_img].children[1].children[1].children[3].style.display = "none"
        smallRem[x].style.top = "-410px"
        preload_img++;
    };
};

for (let x=0; x<deletedCheckboxes.length; x++) {
    smallBatt[x].children[0].addEventListener('change', (event) => {
        let realPos = getRealPosition(x);
        const files = event.target.files;
        let file = files[0];
        smallBatt[realPos].reader.readAsDataURL(file);
        smallBatt[realPos].reader.addEventListener('load', (event) => {
            let place = getPlace(realPos);
            let img = document.createElement('img');
            img.height = 124;
            img.width = 174;
            if (place.firstChild) {
                place.removeChild(place.firstChild);
            }
            ;
            place.appendChild(img);
            img.src = event.target.result;
            img.alt = file.name;
            smallBatt[realPos].reader = new FileReader();
            deletedCheckboxes[x].checked = false

        });
    },);
    smallRem[x].addEventListener('click', (event) => {
        let realPlace = getRealPosition(x);
        let place = getPlace(realPlace);
        if (place) {
            deletedCheckboxes[x].checked = true
        }
        ;
    });
}