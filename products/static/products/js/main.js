(function ($) {
    "use strict";
     /*==================================================================
    [ Focus input ]*/
    $('.input100').each(function(){
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })    
    })
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
})(jQuery);

// set the cart in local storage
function set_cart() {
    var cart;  // Declaring the cart variable
    if (localStorage.getItem("cart") === null) {  // Corrected the condition
      cart = {};
    } else {
      cart = JSON.parse(localStorage.getItem("cart"));
    }
    return cart
}
// Add and Update cart
function update(id,name,quantity,price,img) {
    var cart =JSON.parse(localStorage.getItem("cart")) || {};// parse the cart variable and get the inner html 
    let ItemExist=false
    for(item in cart){
        if (item==id) {
            console.log("id match");
            alert(`${name} already exists. Current quantity is ${quantity}. Do you want to increase the quantity?
            `);
            ItemExist=true
            break
        }else{
            console.log("id not match");
        }
}
    // Add the item
if(!ItemExist){
    // simply add the item

    cart[id]=[name,quantity,price,img]
    
    // console.log("Done!");
}
    // Save the Changes
json_date=JSON.stringify(cart)
localStorage.setItem("cart",json_date)
location.reload();
}

// Stripe payment integration
function senity_check() {
    console.log("Sanity check!");
    // Get Stripe publishable key
    fetch("/product/config/")
    .then((result) => { return result.json(); })
    .then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);
    // Event handler
    fetch("/product/create-checkout-session/")
    .then((result) => { return result.json(); })
    .then((data) => {
        console.log(data);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({ sessionId: data.sessionId });
    })
    .then((res) => {
        console.log(res);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
 
    });
 }