const id_item = $("#id_item")
$(document).ready(function () {
    console.log(id_item.children().length);
    if (id_item.children().length === 0) {
        let temp = ""
        temp += "<img id='id_cart_image' src='/media/checkout/y4.png' alt='art2'>";
        temp += " <p id='id_cart_empty' class='empty-cart'>Oops! Your Cart is empty</p>";
        id_item.append(temp);
    }
});
$(function () {
    $(".addButton").click(function () {
        let barcode = $("#id_barcode").val();
        console.log(barcode);
        $.ajax({
            type: "GET",
            url: "get_product?barcode=" + barcode,
            cache: false,
            success: function (response) {
                $(".kong").hide();
                let temp = "<div id='id_item' class='cart-item-list' <!-- 购物车商品 --> </div>"
                $(".c").append(temp);
                addItemToCart(response.product[0].name, response.product[0].barcode,
                    response.product[0].price, response.product[0].image,
                    response.product[0].is_eco, response.product[0].green_point);
                getSum();
                document.getElementById('id_barcode').value = ''; // clear input
            },
            error: function () {
                alert("Please enter a valid barcode")
            }
        })
    });

    function addItemToCart(name, barcode, price, img, is_eco, green_point) {
        let cartRow = document.createElement('div');
        cartRow.classList.add('cart-item');
        let cartItems = document.getElementsByClassName('cart-item-list')[0];
        // 相同商品数量+1
        let cartItemNames = cartItems.getElementsByClassName('p-barcode');
        for (let j = 0; j < cartItemNames.length; j++) {
            if (cartItemNames[j].innerText == barcode) {
                let block = $(cartItemNames[j]).siblings(".p-num").children(".itxt");
                let count = parseInt(block.val()) + 1;
                block.val(count);
                return;
            }
        }

        let startHTML = `
            <div class="cart-item">
            <div class="p-img">
              <img src="/media/${img}" alt="" />
            </div>
            <div class="p-goods">
              <div class="p-msg">${name}</div>
                <div class="p-barcode" style="opacity: 0; height: 0; width: 0">${barcode}</div>
              <div class="p-num">
                <a href="javascript:;" class="decrement"><span>-</span></a>
                <input type="text" class="itxt" value="1" />
                <a href="javascript:;" class="increment"><span>+</span></a>
              </div>
            </div>
            <div class="price">$ ${price}</div>`

        let isEco = `
            <div class="eco-img">
                <span id="id_point" class="green-point">
                    ${green_point}
                </span>
                <img id="id_eco_image" src="/media/eco_logo_1.png" alt=""/>
            </div>`
        let notEco = `
            <div class="eco-img">
                <span id="id_point" class="green-point" style="opacity: 0">
                    ${green_point}
                </span>
            </div>`
        let endHTML = `<div class="p-action"><a href="javascript:;"><span id="close">×<span></a></div></div>`;
        if (is_eco == false) {
            cartRow.innerHTML = startHTML + notEco + endHTML
        } else {
            cartRow.innerHTML = startHTML + isEco + endHTML
        }
        cartItems.append(cartRow);
    }

    // plus+1数量
    $(document).on("click", ".increment", function () {
        let n = $(this).siblings(".itxt").val();
        n++;
        $(this).siblings(".itxt").val(n);
        getSum();
    });

    // minus-1数量
    // $(".decrement").click(function () {
    $(document).on("click", ".decrement", function () {
        let n = $(this).siblings(".itxt").val();
        if (n == 1) {
            return false;
        }
        // console.log(n);
        n--;
        $(this).siblings(".itxt").val(n);
        getSum();
    });

    // 直接修改数量
    $(document).on("change", ".itxt", function () {
        let n = $(this).val();
        getSum();
    })

    // 删除商品
    $(document).on("click", ".p-action a", function () {
        $(this).parents(".cart-item").fadeTo("fast", 0, function () {
            $(this).slideUp("fast", function () {
                $(this).remove();
                getSum();
                // empty cart or not
                if ($(".cart-item").length == 0) {
                    $(".kong").show();
                }
            });
        });
    });

    // 总商品数（numTotal）和总价 （moneyTotal）
    function getSum() {
        let money = 0;
        let point = 0;
        let num = 0;
        let priceArray = [];
        let greenPointArray = [];
        let numArray = [];
        let moneyTotal = 0;
        let numTotal = 0;
        let pointTotal = 0;

        $(".price").each(function (i, ele) {
            money = parseFloat($(ele).text().substr(1));
            priceArray.push(money);
        });
        $(".green-point").each(function (i, ele) {
            point = parseInt($(ele).text().substr(1));
            greenPointArray.push(point);
        });

        $(".itxt").each(function (i, ele) {
            num = parseInt($(ele).val());
            numArray.push(num);
            numTotal += parseInt($(ele).val());
        });
        for (let i = 0; i < numArray.length; i++) {
            moneyTotal += numArray[i] * priceArray[i];
            pointTotal += numArray[i] * greenPointArray[i];
        }
        $(".amount-sum em").text(numTotal);
        $("#id_total_price em").text("$ " + moneyTotal.toFixed(2));
        $("#id_total_points em").text("Green: " + pointTotal);
    }

    document.getElementById("id_finish").onclick = function () {
        console.log($(".cart-item").length);
        if ($(".cart-item").length == 0) {
            alert("Your cart is empty");
        } else {
            location.href = "{% url 'payment_method'%}";
        }

    };
})