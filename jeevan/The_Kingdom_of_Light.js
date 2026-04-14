function getData(){
    url  = "https://fakestoreapi.com/products/";
    return fetch(url)
}

getData()
.then(response => response.json())
.then(data => console.log(data))
.catch((err) => console.error(err))