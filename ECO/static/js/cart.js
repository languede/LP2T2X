$(function () {
    $(".addButton").click(function () {
        var barcode = $("#id_barcode").val();
        console.log(barcode);
        $.ajax({
            type: "GET",
            url: "{% url 'get_product' %}?barcode=" + barcode,
            // url: "http://127.0.0.1:8000/get_product/?barcode=" + barcode,
            cache: false,
            success: function (response) {
                if (response.status === 200) {
                    alert(response.result);
                    console.log(response.product[0].image);
                    console.log(response.product[0].barcode);
                    console.log(response.product[0].price);
                    $(".kong").hide();
                    addItemToCart(response.product[0].barcode, response.product[0].price, response.product[0].image);
                    console.log($(".cart-item"));
                    getSum();
                    $(".input").find("input").val("");
    
                } else {
                    alert(response.result);
                }
            }
        })
    });
    
    function addItemToCart(barcode, price, img) {
        var cartRow = document.createElement('div');
        cartRow.classList.add('cart-item');
        var cartItems = document.getElementsByClassName('cart-item-list')[0];
        // 相同商品数量+1
        var cartItemNames = cartItems.getElementsByClassName('p-msg');
        for (var j = 0; j < cartItemNames.length; j++) {
            if (cartItemNames[j].innerText === barcode) {
                // console.log(cartItemNames[j]);
                // alert('This item in the cart');
                var block = $(cartItemNames[j]).siblings(".p-num").children(".itxt");
                // console.log(block);
                // console.log(block.val());
                var count = parseInt(block.val())+1;
                // console.log(count);
                block.val(count);
                return;
            }
        }
        cartRow.innerHTML = `
        <div class="cart-item">
        <div class="p-img">
          <img src="${img}" alt="" />
        </div>
        <div class="p-goods">
          <div class="p-msg">${barcode}</div>
          <div class="p-num">
            <a href="javascript:;" class="decrement">-</a>
            <input type="text" class="itxt" value="1" />
            <a href="javascript:;" class="increment">+</a>
          </div>
        </div>
        <div class="p-price">$${price}</div>
        <div class="eco-img">
          <img src="Images/Eco icon.png" alt="" />
        </div>
        <div class="p-action"><a href="javascript:;">×</a></div>
    </div>`;
        cartItems.append(cartRow);
    }

    // plus+1数量
    $(document).on("click",".increment",function () {
        var n = $(this).siblings(".itxt").val();
        // console.log(n);
        n++;
        $(this).siblings(".itxt").val(n);
        getSum();
    });

    // minus-1数量
    // $(".decrement").click(function () {
    $(document).on("click",".decrement",function () {
        var n = $(this).siblings(".itxt").val();
        if (n === 1) {
            return false;
        }
        // console.log(n);
        n--;
        $(this).siblings(".itxt").val(n);
        getSum();
    });

    // 直接修改数量
    // $(".itxt").change(function () {
    $(document).on("change",".itxt",function () {
        var n = $(this).val();
        // console.log($(this));
        getSum();
    })

    // 删除商品
    // $(".p-action a").click(function () {
    $(document).on("click",".p-action a",function () {
        $(this).parents(".cart-item").fadeTo("fast", 0.2, function () {
            $(this).slideUp("fast", function() {
              $(this).remove();
              // console.log($(".cart-item"));
              getSum();
              // empty cart or not
              if ($(".cart-item").length === 0) {
                $(".kong").show();
            }
            });
          });
        // $(this).parents(".cart-item").remove();
        // getSum();
        // 检查购物车是否为空，如果空，要让kong回来
        // if ($(".cart-item").length == 0) {
        //     $(".kong").show();
        // }
    });

    // 总商品数（numTotal）和总价 （moneyTotal）
    function getSum() {
        var money = 0;
        var num = 0;
        var priceArray = new Array();
        var numArray = new Array();
        var moneyTotal = 0;
        var numTotal = 0;
        $(".p-price").each(function (i, ele) {
            money = parseFloat($(ele).text().substr(1));
            priceArray.push(money);
        });

        $(".itxt").each(function (i, ele) {
            num = parseInt($(ele).val());
            numArray.push(num);
            numTotal += parseInt($(ele).val());
        });
        // console.log(priceArray);
        // console.log(priceArray[1]);
        // console.log(numArray);
        // console.log(sum(numArray));
        for (var j = 0; j < numArray.length; j++) {
            moneyTotal += numArray[j] * priceArray[j];
        }
        // console.log(moneyTotal);
        $(".amount-sum em").text(numTotal);
        $(".price-sum em").text("$" + moneyTotal.toFixed(2));
    }

})
