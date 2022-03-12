function cardLoading() {
    const card_div=document.createElement("div");
    const img_div=document.createElement("div");
    const div_para=document.createElement("div");
    const card_header=document.createElement('div');
    card_div.classList.add("card-loading","col-4");
    img_div.classList.add("l-img");
    card_header.classList.add("l-header")
    for(let i=0;i<3;i++){
        let card_paragraph=document.createElement("span");
        card_paragraph.classList.add("l-paragraph");
        div_para.appendChild(card_paragraph);
    }
    card_div.append(img_div,card_header,div_para)
    return card_div;
    
}
async function delay(ms){
    return new Promise(res=>setTimeout(res,ms));
}
function makeLoading(element) {
    let loading_cards=[]
    for (let i = 0; i < 4; i++) {
        loading_cards.push(cardLoading());
    }   
    element.replaceChildren(...loading_cards)
}