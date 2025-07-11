async function addToCart(book_id) {
    const response = await fetch("/cart/add", {
        method: "POST",
        body: JSON.stringify({ book_id: book_id }),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookieValue('csrftoken')
        }
    })
    
    if (response.status == 200) {
        window.alert("Item has been added!")
    } else {
        text = await response.text();
        window.alert(`Error ${response.status}: ${text}`)
    }
}

async function placeOrder() {
    const response = await fetch("/place_order/", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookieValue('csrftoken')
        }
    })
    
    if (response.status == 200) {
        window.alert("Order has been placed!!!")
        window.href = "/books"
    } else {
        text = await response.text();
        window.alert(`Error ${response.status}: ${text}`)
    }
    
    
}

function getCookieValue(name) {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        cookie = cookie.trim();
        if(cookie.startsWith(name + '=')) {
            return cookie.substring(name.length + 1);
        }
    }
    return null;
}