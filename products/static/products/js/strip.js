function senity_check() {
   console.log("Sanity check!");

   // Get Stripe publishable key
   fetch("/product/config/")
   .then((result) => { return result.json(); })
   .then((data) => {
   // Initialize Stripe.js
   const stripe = Stripe(data.publicKey);

   // new
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
   // click the address save button:
   // document.getElementById("address").click()
}