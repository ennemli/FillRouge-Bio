const navbar = document.querySelector("#navbar");
const product = document.querySelector("#product");
let loaded=false;
function delay(ms){
    return new Promise((res)=>{setTimeout(res,ms)});
}
let observerOptions = {
    threshold: 0,
}
let observer = new IntersectionObserver(scrollingObserver, observerOptions);
function scrollingObserver(entries) {
    entries.forEach(entry => {

        if (entry.boundingClientRect.bottom<=0) {
            if(!loaded){
            
                loaded=true;
            }
        }

    });
}
// observer.observe(product)