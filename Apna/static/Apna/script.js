$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml= this.parentNode.children[5];
    // console.log(eml)
    // console.log("pid=",id)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id

        },
        success:function(data){
            console.log("data=",data);
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            // document.getElementById("totalamount").innerText=data.totalamount

        }

    })

});
$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml= this.parentNode.children[5];
        // console.log(eml)
    // console.log("pid=",id)
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id

        },
        success:function(data){
            console.log("data=",data);
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            // document.getElementById("totalamount").innerText=data.totalamount

        }

    })

});
$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml= this
    // console.log(eml)
    // console.log("pid=",id)
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id

        },
        success:function(data){
            console.log("data=",data);
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
            // document.getElementById("totalamount").innerText=data.totalamount

        }

    })

});




// $('.submit_button').click(function(){
    
//     // console.log(eml)
//     // console.log("pid=",id)
//     $.ajax({
//         type:"GET",
//         url:"/checkout",
        
        

//     })

// });


