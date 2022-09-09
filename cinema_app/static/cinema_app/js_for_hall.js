const PlaceWidth = 600;
const maxPlace=50;
const minPlace = 20;
const Background = document.getElementById("Background");


function getRow(){
    let row = document.createElement('div')
    row.classList.add('row');
    return row;
};

function getBasePlace(place_for_one, number){
    place_for_one=place_for_one+"px";
    let base_place = document.createElement('div');
    base_place.classList.add('base-place_stat')
    base_place.innerText = number;
    base_place.style.width = place_for_one;
    base_place.style.margin="2px;"
    let col = getCol()
    col.append(base_place);
    col.style.width = place_for_one;
    col.style.margin="2px;"
    return col;
};

function getVipePlace(place_for_one, number){
    place_for_one=place_for_one+"px";
    let vip_place = document.createElement('div');
    vip_place.classList.add('vip-place_stat')
    vip_place.innerText = number;
    vip_place.style.width = place_for_one;
    vip_place.style.margin="2px;"
    let col = getCol()
    col.append(vip_place);
    col.style.width = place_for_one;
    col.style.margin="2px;"
    return col;
};

function getCol(){
    let col = document.createElement('div');
    col.classList.add('col');
    return col;
}

function getLeftCol(value){
    let left_col = document.createElement('div');
    left_col.style.maxWidth='60px';
    let p = document.createElement('p');
    p.style.float='left';
    p.style.fontSize='20px';
    p.style.fontFamily="'Andale Mono', monospace";
    p.innerText=value;
    left_col.append(p)
    return left_col
};

function getClearCol(place_for_one){
    let col = getBasePlace(place_for_one,"")
    col.style.opacity="0";
    return col;
}



$.ajax({
    url: document.location+"/get_scheme",
    success: SchemePaint
});

function SchemePaint(result, status, xhr){
    let max=0;

    for (let x in result){
        let rowOfNumbers = result[x];
        for (let y=0; y<rowOfNumbers.length; y++){
        };
        if (max<rowOfNumbers.length){
            max=rowOfNumbers.length;
        };
    }

    let max_marg_length = 5*max;
    let max_place_for_one = (PlaceWidth-max_marg_length)/max;
    let place_for_one = max_place_for_one;
    if (max_place_for_one>maxPlace){
        place_for_one=maxPlace;
    } else {
        if (max_place_for_one<minPlace){
            place_for_one = minPlace;
        };
    };


    for (let x in result){
        let rowOfNumbers = result[x];
        let row = getRow();
        let left_col = getLeftCol(x);
        row.append(left_col)

        let sit_number = 0;
        for (let y=0; y<rowOfNumbers.length; y++){
            if (rowOfNumbers.charAt(y)!="0"){
                sit_number++;
            };
            if (rowOfNumbers.charAt(y)=="1"){
                let this_col = getBasePlace(place_for_one, sit_number);
                row.append(this_col);
            };
            if (rowOfNumbers.charAt(y)=="0"){
                let this_col = getClearCol(place_for_one);
                row.append(this_col);
            };
            if (rowOfNumbers.charAt(y)=="2"){
                row.children[0].style.marginTop="16px";
                let this_col = getVipePlace(place_for_one, sit_number);
                row.append(this_col);
            };

        };

        Background.append(row);
    };
};

