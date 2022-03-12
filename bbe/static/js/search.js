const product_search_inp = document.getElementById("product_search");
const product_element = document.getElementById("product");
const carousel = document.getElementById("carousel")
const loading_element = document.getElementById("loading")
const model_shadow = document.querySelector(".model-shadow")
const search_results = document.getElementById("search_results")

let is_loading = false;

product_search_inp.addEventListener("input", function (event) {
    (async function () {
        await searchElementList(event.target.value);
    })()

});
async function search_for_product(product_name) {
    let results = [];
    if (product_name.length > 0) {
        try {
            const res = await fetch(`api/product/search/${product_name}`);
            results = await res.json();
        } catch {
            results = []
        }
    } else {
        results = []
    }

    return results;
}
async function searchElementList(product_name) {
    search_results.innerHTML = ""

    if (!!product_name) {
        const results = await search_for_product(product_name);

        if (results.length > 0) {
            let link
            search_results.classList.remove("text-center")

            const links = []
            console.log(results)

            for (product of results) {
                link=document.createElement("a");
                link.href = "#"+product.product_name;
                link.classList.add("list-group-item", "list-group-action", "fs-5")
                link.innerText = product.product_name;
                links.push(link);
            }
            search_results.replaceChildren(...links)


        } else {
            search_results.classList.add("text-center", "text-danger")

            const msg = document.createElement('h5');
            msg.innerHTML = "Rien n'a été trouvé.";
            search_results.replaceChildren(msg);
        }
    }
}


product_search_inp.addEventListener("click", () => {

    model_shadow.classList.add("model-shadow-active")
    search_results.classList.add("c-model-active")
    document.body.style.overflow = "hidden"

});
model_shadow.addEventListener("click", () => {
    model_shadow.classList.remove("model-shadow-active");
    search_results.classList.remove("c-model-active");
    document.body.style.overflow = "auto"

});