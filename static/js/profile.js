let list_pop = false;

$(document).on("input", "input:file", function () {
  readURL(this);
});

function readURL(input) {
  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.onload = function (e) {
      $("#user-img").attr("src", e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
  }
}

function on_toggle() {
  //list 목록
  if (list_pop) {
    $("#list").addClass("hidden");
    list_pop = false;
  } else {
    $("#list").removeClass("hidden");
    list_pop = true;
  }
}

function on_list_select(e) {
  const replace_text = e.children[0].children[0].innerHTML;
  const text = document.querySelector("#main-text");
  const picture = document.querySelector("#picture-img");
  text.innerHTML = replace_text;
  if (replace_text.replace(/\s/g, "") == "불") {
    picture.src =
      "https://bondar-bucket.s3.ap-northeast-2.amazonaws.com/picture/Fire.jpeg";
  } else if (replace_text.replace(/\s/g, "") == "물") {
    picture.src =
      "https://bondar-bucket.s3.ap-northeast-2.amazonaws.com/picture/water.png";
  } else if (replace_text.replace(/\s/g, "") == "밀레") {
    picture.src =
      "https://bondar-bucket.s3.ap-northeast-2.amazonaws.com/picture/Millet.jpeg";
  } else if (replace_text.replace(/\s/g, "") == "반고흐") {
    picture.src =
      "https://bondar-bucket.s3.ap-northeast-2.amazonaws.com/picture/vanGogh.png";
  } else if (replace_text.replace(/\s/g, "") == "이중섭") {
    picture.src =
      "https://bondar-bucket.s3.ap-northeast-2.amazonaws.com/picture/leejungsub.jpeg";
  }
  on_toggle();
}
