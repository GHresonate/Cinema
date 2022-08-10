const allPhotos = 5;
const fileUploader = document.getElementById('id_main_photo');
const remMain = document.getElementById('rem_main');
const reader = new FileReader();
const readers = [new FileReader(),new FileReader(),new FileReader(),new FileReader(),new FileReader()];
const resButt = document.getElementById('main_res')
const mainImgForm = document.getElementById('main-ph');
const smallBatt = document.getElementsByClassName('small_hidden_form');
const smallRem = document.getElementsByClassName('rem_small')
const boxes = document.getElementsByClassName('boxes');
const buttAddForm = document.getElementById('big_gal_button_top');
const buttRemForm = document.getElementById('big_gal_button_bottom')
let imageGrid = document.getElementById('image_grid');
let lastForm = 0;

buttRemForm.style.opacity="0.5";

for (let x=0; x<allPhotos; x++){
    boxes[x].style.display="none";
}

buttAddForm.addEventListener('click', (event) =>{
    if (lastForm<allPhotos){
        boxes[lastForm].style.display = "initial";
        lastForm++;
        if (lastForm==allPhotos){
            buttAddForm.style.opacity = "0.5";
        };
    };
    if (lastForm!=0){
        buttRemForm.style.opacity = "1";
    };
});

buttRemForm.addEventListener(('click'), (event) =>{
    if (lastForm!=0){
        boxes[lastForm-1].style.display = "none";
        lastForm--;
        if (lastForm==0){
            buttRemForm.style.opacity = "0.5";
        };
    };
    if (lastForm!=allPhotos){
        buttAddForm.style.opacity = "1";
    };
    const parent = smallBatt[lastForm].parentNode.parentNode;
    let place = parent.firstElementChild;
    if (place.firstChild){
        place.removeChild(place.firstChild);
    };
});

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


for (let x=0; x<allPhotos; x++) {
    smallBatt[x].firstChild.addEventListener('change', (event) => {
        const files = event.target.files;
        let file = files[0];
        readers[x].readAsDataURL(file);
        const parent = smallBatt[x].parentNode.parentNode;
        let place = parent.firstElementChild;
        readers[x].addEventListener('load',(event)=>{
            let img = document.createElement('img');
            img.height = 124;
            img.width = 174;
            if (place.firstChild){
                place.removeChild(place.firstChild);
            };
            place.appendChild(img);
            img.src = event.target.result;
            img.alt = file.name;
        });
    });

    smallRem[x].addEventListener('click', (event)=>{
        const parent = smallBatt[x].parentNode.parentNode;
        let place = parent.firstElementChild;
        smallBatt[x].firstChild.value = '';
        if (place.firstChild){
          place.removeChild(place.firstChild);
        };
    });
};

resButt.addEventListener('click', (event)=>{
    if (imageGrid.firstChild){
        imageGrid.removeChild(imageGrid.firstChild);
    };
    for (let x=1; x<allPhotos; x++){
        const parent = smallBatt[x].parentNode.parentNode;
        let place = parent.firstElementChild;
        if (place.firstChild){
            place.removeChild(place.firstChild);
        };
    };
    for (let x=0; x<allPhotos; x++){
        boxes[x].style.display="none";
    };
    lastForm = 0;
    buttAddForm.style.opacity="1";
    buttRemForm.style.opacity="0.5";
});

remMain.addEventListener('click', (event)=>{
    fileUploader.value = '';
  if (imageGrid.firstChild) {
      imageGrid.removeChild(imageGrid.firstChild);
  };
});