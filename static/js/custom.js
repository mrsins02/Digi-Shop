function productImageChanger(imageURL) {
    $("#product-main-image").attr("src", imageURL)

}

function addToFavorites(productId) {
    var productId = productId;
    $.get("/favorites/add-to-favorites/", {
        product_id: productId,
    }).then(res => {
        if (res.status === 200) {
            Swal.fire({
                icon: 'success', text: 'محصول به مورد علاقه ها اضافه شد!',
            })
        }
        ;
        if (res.status === 400) {
            Swal.fire({
                icon: 'warning', text: 'محصول قبلا به مورد علاقه ها اضافه شده است!',
            })
        }
        ;
        if (res.status === 404) {
            Swal.fire({
                icon: 'error', text: 'محصول یافت نشد!',
            })
        }
        ;
    })
}

function deleteFromFavorites(productId) {
    var productId = productId;
    $.get("/favorites/delete-from-favorites/", {
        product_id: productId,
    }).then(res => {
        $("#cart_items").html(res)
        if (res.status === 404) {
            Swal.fire({
                icon: 'error', text: 'محصول یافت نشد!',
            })
        }
        ;
    })
}

function cleanFavorites() {
    $.get("/favorites/clean-favorites/", {}).then(res => {
        console.log(res);
        swal.fire("لیست مورد علاقه ها خالی شد!")
        $("#cart_items").html(res)
    })
}

function addProductComment(productId) {
    var text = $("#comment-text").val();
    var parentId = $("#parent-id").val();
    $.get("/shop/product-add-comment/", {
        "parent_id": parentId, "product_id": productId, "text": text,
    }).then(res => {
        console.log(res);
        $("#comment-text").val("");
        $("#parent-id").val("none");

        if (res.status === 200) {
            Swal.fire({
                icon: 'success', text: res.message,
            })
        }
        ;
        if (res.status === 302) {
            Swal.fire({
                icon: 'warning', text: res.message,
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.replace("/users/login/");
                }
            });

        }
        ;
        if (res.status === 400) {
            Swal.fire({
                icon: 'warning', text: res.message,
            })
        }
        ;
        if (res.status === 404) {
            Swal.fire({
                icon: 'error', text: res.message,
            })
        }
        ;$("#comment-area").html(res.html);
    })
}
function addPostComment(postId) {
    var text = $("#comment-text").val();
    var parentId = $("#parent-id").val();
    $.get("/blog/post-add-comment/", {
        "parent_id": parentId, "post_id": postId, "text": text,
    }).then(res => {
        console.log(res);
        $("#comment-text").val("");
        $("#parent-id").val("none");

        if (res.status === 200) {
            Swal.fire({
                icon: 'success', text: res.message,
            })
        }
        ;
        if (res.status === 302) {
            Swal.fire({
                icon: 'warning', text: res.message,
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.replace("/users/login/");
                }
            });

        }
        ;
        if (res.status === 400) {
            Swal.fire({
                icon: 'warning', text: res.message,
            })
        }
        ;
        if (res.status === 404) {
            Swal.fire({
                icon: 'error', text: res.message,
            })
        }
        ;$("#comment-area").html(res.html);
    })
}
function fillParentId(parentId) {
    $("#parent-id").val(parentId);
    document.getElementById("comment-form").scrollIntoView({behavior: "smooth"});
}