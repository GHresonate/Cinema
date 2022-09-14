const PlaceWidth = 600;
const maxPlace=50;
const minPlace = 20;
const Background = document.getElementById("Background");
const readyButt = document.getElementById('ready')
let price = -1;
let ordered = {}
ordered[0]=[]
let sum_places = 0
let sum = 0
const csrftoken = get_cookie('csrftoken');

$.ajax({
    url: document.location+"/get_scheme",
    success: SchemePaint
});


$.ajax({
            url: document.location+"/price",
            success: setPrice
        });
let place = ''+window.location.href
let cut_href = place.split('/')
let sc_id = cut_href[cut_href.length-1]


        const chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/chat/'
            + sc_id
            + '/'
        );

chatSocket.onmessage = function (result){
    let ordered = JSON.parse(result.data)
    ordered = ordered['message']
    for (let row in ordered){
       for (let place in ordered[row]){
           setPlaceAsBusy(row+'__'+ordered[row][place])
       }
    }
    clearOrder()
}

function getRow(){
    let row = document.createElement('div')
    row.classList.add('row');
    return row;
};

function clearOrder(){
    for (let row in ordered){
        ordered[row]=[]
    }
}

function getEmptyPlace(place_for_one){
    place_for_one=place_for_one+"px";
    let base_place = document.createElement('div');
    base_place.classList.add('empty-place')
    base_place.innerText = '';
    base_place.style.width = place_for_one;
    base_place.style.margin="2px;"
    let col = getCol()
    col.append(base_place);
    col.style.width = place_for_one;
    col.style.margin="2px;"
    return col;
};

function getBasePlace(place_for_one, number){
    place_for_one=place_for_one+"px";
    let base_place = document.createElement('div');
    base_place.classList.add('base-place')
    base_place.innerText = number;
    base_place.style.width = place_for_one;
    base_place.style.margin="2px;"
    let col = getCol()
    col.append(base_place);
    col.style.width = place_for_one;
    col.style.margin="2px;"
    return col;
};

function get_ordered(){
    return ordered
}

function get_cookie ( cookie_name )
{
  let results = document.cookie.match ( '(^|;) ?' + cookie_name + '=([^;]*)(;|$)' );

  if ( results )
    return ( unescape ( results[2] ) );
  else
    return null;
}

function addId(place, row, col){

    place.id=row+'__'+col;
}

function getVipePlace(place_for_one, number){
    place_for_one=place_for_one+"px";
    let vip_place = document.createElement('div');
    vip_place.classList.add('vip-place')
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
    let col = getEmptyPlace(place_for_one)
    col.style.opacity="0";
    return col;
}

function setPlaceAsBusy(place_id){
    let place = document.getElementById(place_id);
    place.classList = ['ordered-place']
    $('#'+place_id).off('click')
}

function setPrice(result, status, xhr){
    price=Number(result['price'])
}

function paintReserved(result, status=200, xhr=undefined){
    let ordered = JSON.parse(result)
    for (let row in ordered){
        for (let place in ordered[row]){
            setPlaceAsBusy(row+'__'+ordered[row][place])
        }
    }
}

function SchemePaint(result, status, xhr){
    let max=0;

    for (let x in result){
        ordered[x]=[]
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
        row.append(left_col);
        row.id = x;

        let sit_number = 0;
        for (let y=0; y<rowOfNumbers.length; y++){
            if (rowOfNumbers.charAt(y)!="0"){
                sit_number++;
            };
            if (rowOfNumbers.charAt(y)=="1"){
                let this_col = getBasePlace(place_for_one, sit_number);
                addId(this_col.children[0], x, sit_number)
                row.append(this_col);
            };
            if (rowOfNumbers.charAt(y)=="0"){
                let this_col = getClearCol(place_for_one);
                row.append(this_col);
            };
            if (rowOfNumbers.charAt(y)=="2"){
                row.children[0].style.marginTop="16px";
                let this_col = getVipePlace(place_for_one, sit_number);
                addId(this_col.children[0], x, sit_number)
                row.append(this_col);
            };

        };

        Background.append(row);
    };
    $(".base-place").click(chose_base);
    $(".vip-place").click(chose_vip);

    $.ajax({
        url: document.location+"/get_reserved",
        success: paintReserved
});
};




function add_place() {
      sum_places+=1;
      document.getElementById("indicator").innerHTML = `Выбрано: ${sum_places}`;
    }

function rem_place() {
      sum_places-=1;
      document.getElementById("indicator").innerHTML = `Выбрано: ${sum_places}`;
    }

function add_sum(price) {
      sum+=price;
      document.getElementById("sum").innerHTML = `Сумма: ${sum}`;
    }

function rem_sum(price) {
      sum-=price;
      document.getElementById("sum").innerHTML = `Сумма: ${sum}`;
    }

    function chose_base(){
        let row = this.parentNode.parentNode.children[0].children[0].innerText
        let value = this.innerText
      if ($(this).hasClass("chosen")){
        $(this).removeClass("chosen");
        rem_place();
        rem_sum(price);
        if (value in ordered[row]){
            ordered[row].slice(ordered[row].indexOf(value))
        }
      }else{
        ordered[row].push(value)
        $(this).addClass("chosen");
        add_place();
        add_sum(price);
      }
    }

    function chose_vip(){
        let row = this.parentNode.parentNode.children[0].children[0].innerText
        let value = this.innerText
      if ($(this).hasClass("chosen")){
        $(this).removeClass("chosen");
        rem_place();
        rem_sum(price*2);
            ordered[row].splice(ordered[row].indexOf(value), 1)
      }else{
        ordered[row].push(value)
        $(this).addClass("chosen");
        add_place();
        add_sum(price*2);
      }
    }

function GoodOrder(result, status, xhr){
    let ready_ordered = get_ordered()
        paintReserved(result,status,xhr);
        chatSocket.send(JSON.stringify({
                'message': ready_ordered
            }));
    sum=0;
    sum_places=0;
    document.getElementById("sum").innerHTML = `Сумма: ${sum}`;
          document.getElementById("indicator").innerHTML = `Выбрано: ${sum_places}`;
        clearOrder();
}

function sendPlaces(){
    $.ajax({
        beforeSend: function(xhr, settings) {
        if (!this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            xhr.setRequestHeader("content-type", "application/json");
        }},
      type: "POST",
      url: document.location+"/ready",
      data: JSON.stringify(ordered),
      success: GoodOrder,
      dataType: 'json'
});
}


readyButt.addEventListener('click', sendPlaces)