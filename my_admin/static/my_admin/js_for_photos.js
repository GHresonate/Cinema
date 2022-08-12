const allPhotos = 5;
const fileUploader = document.getElementById('id_main_photo');
const remMain = document.getElementById('rem_main');
const reader = new FileReader();
const resButt = document.getElementById('main_res')
const smallBatt = document.getElementsByClassName('small_hidden_form');
const smallRem = document.getElementsByClassName('rem_small')
const boxes = document.getElementsByClassName('boxes');
const buttAddForm = document.getElementById('big_gal_button_top');
const buttRemForm = document.getElementById('big_gal_button_bottom');
const photo_parent = document.getElementById('photo_parent');
let imageGrid = document.getElementById('image_grid');
let lastForm = -1;
let form_state = [];
let forms = [];
let order = [];


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

remMain.addEventListener('click', (event)=>{
    fileUploader.value = '';
  if (imageGrid.firstChild) {
      imageGrid.removeChild(imageGrid.firstChild);
  };
});

for (let x=0; x<allPhotos; x++) {
    smallBatt[x].firstChild.addEventListener('change', (event) => {
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
                if (lastForm==0){
                    buttAddForm.style.opacity="1";
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
    smallBatt[first-1].firstChild.value = '';
    switch (first){
        case 1:{
        buttRemForm.style.opacity = "0.5";
        photo_parent.removeChild(forms[first-1]);
        form_state[first-1] = 0;
        lastForm--;
        break;
    };
        case (-2): {
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
        lastForm++;
        form_state[first]=1;
        if (first==(allPhotos-1)){
            buttAddForm.style.opacity = "0.5";
        };
    };

});

resButt.addEventListener('click', (event)=>{
    if (imageGrid.firstChild){
        imageGrid.removeChild(imageGrid.firstChild);
    };
    fileUploader.value = '';
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

    lastForm = -1;
    buttAddForm.style.opacity="1";
    buttRemForm.style.opacity="0.5";
});


for (let x=0; x<allPhotos; x++){
    order[x] = x;
    smallBatt[x].reader = new FileReader();
};
buttRemForm.style.opacity="0.5";
for (let x=0; x<allPhotos; x++){
    forms[x] = boxes[0];
    form_state[x]=0;
    $(boxes[0]).remove();
};